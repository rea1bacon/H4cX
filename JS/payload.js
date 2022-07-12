/* PAYLOAD BY @realbacon */



var infos = {}

// Get ip, country, time, region
let apiKey = '9ad10f21209c4a3f890f84c81579aede';
 $.ajaxSetup({
   async: false
 });
$.getJSON('https://ipgeolocation.abstractapi.com/v1/?api_key=' + apiKey, function(data) {
    infos["ip"] = data["ip_address"];
    infos["country"] = data["country"];
    infos["region"] = data["region"];
    infos["current_time"] = data["timezone"]["current_time"]
});

// Get user agent
var UA = window.navigator.userAgent;
infos["user_agent"] = UA


//Getting web browser
var web_Browser;
// Opera 8.0+
var isOpera = (!!window.opr && !!opr.addons) || !!window.opera || navigator.userAgent.indexOf(' OPR/') >= 0;
if(isOpera){
  web_Browser = "Opera";
}
// Firefox 1.0+
var isFirefox = typeof InstallTrigger !== 'undefined';
if(isFirefox){
  web_Browser = "Firefox";
}
// Safari 3.0+ "[object HTMLElementConstructor]"
var isSafari = /constructor/i.test(window.HTMLElement) || (function (p) { return p.toString() === "[object SafariRemoteNotification]"; })(!window['safari'] || (typeof safari !== 'undefined' && window['safari'].pushNotification));
if(isSafari){
  web_Browser = "Safari";
}
// Internet Explorer 6-11
var isIE = /*@cc_on!@*/false || !!document.documentMode;
if(isIE){
  web_Browser = "IE";
}
// Edge 20+
var isEdge = !isIE && !!window.StyleMedia;
if(isEdge){
  web_Browser = "Edge";
}
// Chrome 1 - 79
var isChrome = !!window.chrome && (!!window.chrome.webstore || !!window.chrome.runtime);
if(isChrome){
  web_Browser = "Chrome";
}
// Edge (based on chromium) detection
var isEdgeChromium = isChrome && (navigator.userAgent.indexOf("Edg") != -1);
if(isEdgeChromium){
  web_Browser = "EdgeChromium";
}
// Blink engine detection
var isBlink = (isChrome || isOpera) && !!window.CSS;
infos["web_Browser"] = web_Browser;

// Get OS
function getOS() {
  var userAgent = window.navigator.userAgent,
      platform = window.navigator.platform,
      macosPlatforms = ['Macintosh', 'MacIntel', 'MacPPC', 'Mac68K'],
      windowsPlatforms = ['Win32', 'Win64', 'Windows', 'WinCE'],
      iosPlatforms = ['iPhone', 'iPad', 'iPod'],
      os = null;

  if (macosPlatforms.indexOf(platform) !== -1) {
    os = 'Mac OS';
  } else if (iosPlatforms.indexOf(platform) !== -1) {
    os = 'iOS';
  } else if (windowsPlatforms.indexOf(platform) !== -1) {
    os = 'Windows';
  } else if (/Android/.test(userAgent)) {
    os = 'Android';
  } else if (!os && /Linux/.test(platform)) {
    os = 'Linux';
  }

  return os;
}

infos["OS"] = getOS();
for (const [key, value] of Object.entries(infos)) {
  if (value == null) {
    infos[key] = "Not detected";
  }
}
console.table(infos)
