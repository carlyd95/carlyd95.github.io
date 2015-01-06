<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML Basic 1.1//EN" "http://www.w3.org/TR/xhtml-basic/xhtml-basic11.dtd"><html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
    <head><script type="text/javascript">(window.NREUM||(NREUM={})).loader_config={xpid:"Vg4DUV9WGwIGV1hTBAE="};window.NREUM||(NREUM={}),__nr_require=function(t,e,n){function r(n){if(!e[n]){var o=e[n]={exports:{}};t[n][0].call(o.exports,function(e){var o=t[n][1][e];return r(o?o:e)},o,o.exports)}return e[n].exports}if("function"==typeof __nr_require)return __nr_require;for(var o=0;o<n.length;o++)r(n[o]);return r}({QJf3ax:[function(t,e){function n(t){function e(e,n,a){t&&t(e,n,a),a||(a={});for(var c=s(e),u=c.length,f=i(a,o,r),d=0;u>d;d++)c[d].apply(f,n);return f}function a(t,e){u[t]=s(t).concat(e)}function s(t){return u[t]||[]}function c(){return n(e)}var u={};return{on:a,emit:e,create:c,listeners:s,_events:u}}function r(){return{}}var o="nr@context",i=t("gos");e.exports=n()},{gos:"7eSDFh"}],ee:[function(t,e){e.exports=t("QJf3ax")},{}],3:[function(t){function e(t,e,n,i,s){try{c?c-=1:r("err",[s||new UncaughtException(t,e,n)])}catch(u){try{r("ierr",[u,(new Date).getTime(),!0])}catch(f){}}return"function"==typeof a?a.apply(this,o(arguments)):!1}function UncaughtException(t,e,n){this.message=t||"Uncaught error with no additional information",this.sourceURL=e,this.line=n}function n(t){r("err",[t,(new Date).getTime()])}var r=t("handle"),o=t(4),i=t("ee"),a=window.onerror,s=!1,c=0;t("loader").features.err=!0,window.onerror=e,NREUM.noticeError=n;try{throw new Error}catch(u){"stack"in u&&(t(5),t(3),"addEventListener"in window&&t(1),window.XMLHttpRequest&&XMLHttpRequest.prototype&&XMLHttpRequest.prototype.addEventListener&&t(2),s=!0)}i.on("fn-start",function(){s&&(c+=1)}),i.on("fn-err",function(t,e,r){s&&(this.thrown=!0,n(r))}),i.on("fn-end",function(){s&&!this.thrown&&c>0&&(c-=1)}),i.on("internal-error",function(t){r("ierr",[t,(new Date).getTime(),!0])})},{1:4,2:7,3:5,4:18,5:6,ee:"QJf3ax",handle:"D5DuLP",loader:"G9z0Bl"}],4:[function(t,e){function n(t){i.inPlace(t,["addEventListener","removeEventListener"],"-",r)}function r(t){return t[1]}var o=(t(1),t("ee").create()),i=t(2)(o),a=t("gos");if(e.exports=o,n(window),"getPrototypeOf"in Object){for(var s=document;s&&!s.hasOwnProperty("addEventListener");)s=Object.getPrototypeOf(s);s&&n(s);for(var c=XMLHttpRequest.prototype;c&&!c.hasOwnProperty("addEventListener");)c=Object.getPrototypeOf(c);c&&n(c)}else XMLHttpRequest.prototype.hasOwnProperty("addEventListener")&&n(XMLHttpRequest.prototype);o.on("addEventListener-start",function(t){if(t[1]){var e=t[1];"function"==typeof e?this.wrapped=t[1]=a(e,"nr@wrapped",function(){return i(e,"fn-",null,e.name||"anonymous")}):"function"==typeof e.handleEvent&&i.inPlace(e,["handleEvent"],"fn-")}}),o.on("removeEventListener-start",function(t){var e=this.wrapped;e&&(t[1]=e)})},{1:18,2:19,ee:"QJf3ax",gos:"7eSDFh"}],5:[function(t,e){var n=(t(2),t("ee").create()),r=t(1)(n);e.exports=n,r.inPlace(window,["requestAnimationFrame","mozRequestAnimationFrame","webkitRequestAnimationFrame","msRequestAnimationFrame"],"raf-"),n.on("raf-start",function(t){t[0]=r(t[0],"fn-")})},{1:19,2:18,ee:"QJf3ax"}],6:[function(t,e){function n(t,e,n){var r=t[0];"string"==typeof r&&(r=new Function(r)),t[0]=o(r,"fn-",null,n)}var r=(t(2),t("ee").create()),o=t(1)(r);e.exports=r,o.inPlace(window,["setTimeout","setInterval","setImmediate"],"setTimer-"),r.on("setTimer-start",n)},{1:19,2:18,ee:"QJf3ax"}],7:[function(t,e){function n(){c.inPlace(this,d,"fn-")}function r(t,e){c.inPlace(e,["onreadystatechange"],"fn-")}function o(t,e){return e}var i=t("ee").create(),a=t(1),s=t(2),c=s(i),u=s(a),f=window.XMLHttpRequest,d=["onload","onerror","onabort","onloadstart","onloadend","onprogress","ontimeout"];e.exports=i,window.XMLHttpRequest=function(t){var e=new f(t);try{i.emit("new-xhr",[],e),u.inPlace(e,["addEventListener","removeEventListener"],"-",function(t,e){return e}),e.addEventListener("readystatechange",n,!1)}catch(r){try{i.emit("internal-error",[r])}catch(o){}}return e},window.XMLHttpRequest.prototype=f.prototype,c.inPlace(XMLHttpRequest.prototype,["open","send"],"-xhr-",o),i.on("send-xhr-start",r),i.on("open-xhr-start",r)},{1:4,2:19,ee:"QJf3ax"}],8:[function(t){function e(t){if("string"==typeof t&&t.length)return t.length;if("object"!=typeof t)return void 0;if("undefined"!=typeof ArrayBuffer&&t instanceof ArrayBuffer&&t.byteLength)return t.byteLength;if("undefined"!=typeof Blob&&t instanceof Blob&&t.size)return t.size;if("undefined"!=typeof FormData&&t instanceof FormData)return void 0;try{return JSON.stringify(t).length}catch(e){return void 0}}function n(t){var n=this.params,r=this.metrics;if(!this.ended){this.ended=!0;for(var i=0;c>i;i++)t.removeEventListener(s[i],this.listener,!1);if(!n.aborted){if(r.duration=(new Date).getTime()-this.startTime,4===t.readyState){n.status=t.status;var a=t.responseType,u="arraybuffer"===a||"blob"===a||"json"===a?t.response:t.responseText,f=e(u);if(f&&(r.rxSize=f),this.sameOrigin){var d=t.getResponseHeader("X-NewRelic-App-Data");d&&(n.cat=d.split(", ").pop())}}else n.status=0;r.cbTime=this.cbTime,o("xhr",[n,r,this.startTime])}}}function r(t,e){var n=i(e),r=t.params;r.host=n.hostname+":"+n.port,r.pathname=n.pathname,t.sameOrigin=n.sameOrigin}if(window.XMLHttpRequest&&XMLHttpRequest.prototype&&XMLHttpRequest.prototype.addEventListener&&!/CriOS/.test(navigator.userAgent)){t("loader").features.xhr=!0;var o=t("handle"),i=t(2),a=t("ee"),s=["load","error","abort","timeout"],c=s.length,u=t(1);t(4),t(3),a.on("new-xhr",function(){this.totalCbs=0,this.called=0,this.cbTime=0,this.end=n,this.ended=!1,this.xhrGuids={}}),a.on("open-xhr-start",function(t){this.params={method:t[0]},r(this,t[1]),this.metrics={}}),a.on("open-xhr-end",function(t,e){"loader_config"in NREUM&&"xpid"in NREUM.loader_config&&this.sameOrigin&&e.setRequestHeader("X-NewRelic-ID",NREUM.loader_config.xpid)}),a.on("send-xhr-start",function(t,n){var r=this.metrics,o=t[0],i=this;if(r&&o){var u=e(o);u&&(r.txSize=u)}this.startTime=(new Date).getTime(),this.listener=function(t){try{"abort"===t.type&&(i.params.aborted=!0),("load"!==t.type||i.called===i.totalCbs&&(i.onloadCalled||"function"!=typeof n.onload))&&i.end(n)}catch(e){try{a.emit("internal-error",[e])}catch(r){}}};for(var f=0;c>f;f++)n.addEventListener(s[f],this.listener,!1)}),a.on("xhr-cb-time",function(t,e,n){this.cbTime+=t,e?this.onloadCalled=!0:this.called+=1,this.called!==this.totalCbs||!this.onloadCalled&&"function"==typeof n.onload||this.end(n)}),a.on("xhr-load-added",function(t,e){var n=""+u(t)+!!e;this.xhrGuids&&!this.xhrGuids[n]&&(this.xhrGuids[n]=!0,this.totalCbs+=1)}),a.on("xhr-load-removed",function(t,e){var n=""+u(t)+!!e;this.xhrGuids&&this.xhrGuids[n]&&(delete this.xhrGuids[n],this.totalCbs-=1)}),a.on("addEventListener-end",function(t,e){e instanceof XMLHttpRequest&&"load"===t[0]&&a.emit("xhr-load-added",[t[1],t[2]],e)}),a.on("removeEventListener-end",function(t,e){e instanceof XMLHttpRequest&&"load"===t[0]&&a.emit("xhr-load-removed",[t[1],t[2]],e)}),a.on("fn-start",function(t,e,n){e instanceof XMLHttpRequest&&("onload"===n&&(this.onload=!0),("load"===(t[0]&&t[0].type)||this.onload)&&(this.xhrCbStart=(new Date).getTime()))}),a.on("fn-end",function(t,e){this.xhrCbStart&&a.emit("xhr-cb-time",[(new Date).getTime()-this.xhrCbStart,this.onload,e],e)})}},{1:"XL7HBI",2:9,3:7,4:4,ee:"QJf3ax",handle:"D5DuLP",loader:"G9z0Bl"}],9:[function(t,e){e.exports=function(t){var e=document.createElement("a"),n=window.location,r={};e.href=t,r.port=e.port;var o=e.href.split("://");return!r.port&&o[1]&&(r.port=o[1].split("/")[0].split(":")[1]),r.port&&"0"!==r.port||(r.port="https"===o[0]?"443":"80"),r.hostname=e.hostname||n.hostname,r.pathname=e.pathname,"/"!==r.pathname.charAt(0)&&(r.pathname="/"+r.pathname),r.sameOrigin=!e.hostname||e.hostname===document.domain&&e.port===n.port&&e.protocol===n.protocol,r}},{}],gos:[function(t,e){e.exports=t("7eSDFh")},{}],"7eSDFh":[function(t,e){function n(t,e,n){if(r.call(t,e))return t[e];var o=n();if(Object.defineProperty&&Object.keys)try{return Object.defineProperty(t,e,{value:o,writable:!0,enumerable:!1}),o}catch(i){}return t[e]=o,o}var r=Object.prototype.hasOwnProperty;e.exports=n},{}],D5DuLP:[function(t,e){function n(t,e,n){return r.listeners(t).length?r.emit(t,e,n):(o[t]||(o[t]=[]),void o[t].push(e))}var r=t("ee").create(),o={};e.exports=n,n.ee=r,r.q=o},{ee:"QJf3ax"}],handle:[function(t,e){e.exports=t("D5DuLP")},{}],XL7HBI:[function(t,e){function n(t){var e=typeof t;return!t||"object"!==e&&"function"!==e?-1:t===window?0:i(t,o,function(){return r++})}var r=1,o="nr@id",i=t("gos");e.exports=n},{gos:"7eSDFh"}],id:[function(t,e){e.exports=t("XL7HBI")},{}],loader:[function(t,e){e.exports=t("G9z0Bl")},{}],G9z0Bl:[function(t,e){function n(){var t=p.info=NREUM.info;if(t&&t.agent&&t.licenseKey&&t.applicationID&&c&&c.body){p.proto="https"===d.split(":")[0]||t.sslForHttp?"https://":"http://",a("mark",["onload",i()]);var e=c.createElement("script");e.src=p.proto+t.agent,c.body.appendChild(e)}}function r(){"complete"===c.readyState&&o()}function o(){a("mark",["domContent",i()])}function i(){return(new Date).getTime()}var a=t("handle"),s=window,c=s.document,u="addEventListener",f="attachEvent",d=(""+location).split("?")[0],p=e.exports={offset:i(),origin:d,features:{}};c[u]?(c[u]("DOMContentLoaded",o,!1),s[u]("load",n,!1)):(c[f]("onreadystatechange",r),s[f]("onload",n)),a("mark",["firstbyte",i()])},{handle:"D5DuLP"}],18:[function(t,e){function n(t,e,n){e||(e=0),"undefined"==typeof n&&(n=t?t.length:0);for(var r=-1,o=n-e||0,i=Array(0>o?0:o);++r<o;)i[r]=t[e+r];return i}e.exports=n},{}],19:[function(t,e){function n(t){return!(t&&"function"==typeof t&&t.apply&&!t[i])}var r=t("ee"),o=t(1),i="nr@wrapper",a=Object.prototype.hasOwnProperty;e.exports=function(t){function e(t,e,r,a){function nrWrapper(){var n,i,s,u;try{i=this,n=o(arguments),s=r&&r(n,i)||{}}catch(d){f([d,"",[n,i,a],s])}c(e+"start",[n,i,a],s);try{return u=t.apply(i,n)}catch(p){throw c(e+"err",[n,i,p],s),p}finally{c(e+"end",[n,i,u],s)}}return n(t)?t:(e||(e=""),nrWrapper[i]=!0,u(t,nrWrapper),nrWrapper)}function s(t,r,o,i){o||(o="");var a,s,c,u="-"===o.charAt(0);for(c=0;c<r.length;c++)s=r[c],a=t[s],n(a)||(t[s]=e(a,u?s+o:o,i,s,t))}function c(e,n,r){try{t.emit(e,n,r)}catch(o){f([o,e,n,r])}}function u(t,e){if(Object.defineProperty&&Object.keys)try{var n=Object.keys(t);return n.forEach(function(n){Object.defineProperty(e,n,{get:function(){return t[n]},set:function(e){return t[n]=e,e}})}),e}catch(r){f([r])}for(var o in t)a.call(t,o)&&(e[o]=t[o]);return e}function f(e){try{t.emit("internal-error",e)}catch(n){}}return t||(t=r),e.inPlace=s,e.flag=i,e}},{1:18,ee:"QJf3ax"}]},{},["G9z0Bl",3,8]);</script>
    <title>Secure Payment Form</title>
    <meta name="viewport" content="width=device-width; initial-scale=1.0; maximum-scale=1.0; user-scalable=0;"/>
    </head>
<body onload="setTimeout(function() { window.scrollTo(0, 1) }, 100);">
<div class="main">
    <style>
    html, body, div, span, a, img, b, u, i, ol, ul, li,form, label{ margin: 0; padding: 0; border: 0; outline: 0; vertical-align: baseline; background: transparent; font-family: arial;} input, textarea, select {font-family:arial; font-size:12px} body { font-size:11px; font-style:normal;font-variant:normal;font-weight:normal;margin:0;} ol, ul { list-style: none } a { cursor:pointer; text-decoration:none; color:#2d2d2d} :focus { outline: 0 } .clearfix:after { content: " "; display: block; clear: both; visibility: hidden; line-height: 0; height: 0;} .clearfix { display: inline-block; } html .clearfix { display: block;} .mainContainer{width:320px; margin:0 auto;} .hdrMain{background:#000; border-bottom:solid 1px #ededed;height:45px;} .logo{float:left; padding:6px 0 0 6px;} .secure{float:right; padding:3px 8px 0 0;} .hHeading{text-align:center; font-size:14px; font-weight:bold; padding:5px 0 0 0;} .hSubHeading{text-align:center; font-size:12px; padding:1px 0 0 0; color:#6c6c6c;} .hError{padding: 0 0 0 1px; color:#ff0000; text-align:center; font-size:13px; height:35px; line-height:34px; float:left; width:100%; border-style:solid; border-width:1px; border-color:#848484 #c0c0c0 #e1e1e1;} .form{padding:0 5px;} .eachRow{padding:0 0 8px 0;} .cell-1{float:left; width:145px; font-weight:bold; font-size:13px; margin:1px 0 0 0;} .cell-2{float:left; width:165px;} .cell-2 input[type=text]{border-style:solid; border-width:1px; border-color:#848484 #c0c0c0 #e1e1e1; height:17px; line-height:17px; padding:0 0 0 1px; width:145px;-webkit-box-shadow: inset 0px 1px 0px 0px #d4d4d4;box-shadow: inset 0px 1px 0px 0px #d4d4d4;} .cell-2 select{height:19px; line-height:18px;} .countryRow .cell-1{width:70px;} .countryRow .cell-2{width:240px;} .countryRow .cell-2 select{width:223px;} .expDate{float:left; width:80px;} .expYear{float:left; width:60px; margin-left:8px;} .cvvRow{padding-bottom:16px;} .cvvRow .cell-2{position:relative;} .cvvRow input[type=text]{width:40px; margin-right:4px;} .cvvAlt{float:left; width:118px; position:absolute; left:47px;} .zipRow input[type=text]{width:70px;} .usrConfirm input{float:left; width:13px;} .usrConfirm label{float:left; width:275px; margin:1px 0 0 5px;} .gray, .gray a{color:#858585;} .btmMain input{width:310px; border-style:solid; border-width:2px; border-color:#c0c0c0 #6d6d6d #6d6d6d #c0c0c0; padding:3px 0 4px 0; margin:8px 0 5px 0; color:#fff; font-family:Tahoma; font-size:17px; font-weight:bold;text-shadow: 0px 2px 2px rgba(0, 0, 0, 0.9);-webkit-border-radius: 10px;-moz-border-radius: 10px;border-radius: 10px;background: #3490db;background: -moz-linear-gradient(top,  #3490db 0%, #2068a3 100%);background: -webkit-gradient(linear, left top, left bottom, color-stop(0%,#3490db), color-stop(100%,#2068a3));background: -webkit-linear-gradient(top,  #3490db 0%,#2068a3 100%);background: -o-linear-gradient(top,  #3490db 0%,#2068a3 100%);background: -ms-linear-gradient(top,  #3490db 0%,#2068a3 100%);background: linear-gradient(to bottom,  #3490db 0%,#2068a3 100%);filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#3490db', endColorstr='#2068a3',GradientType=0 );} .btmTxt-2{margin:6px 0 6px 0;} label.error{color:#F00; display:block; margin:5px 0 -2px;} .cvvRow label.error{margin:10px 0 -10px;} .expDateRow{position:relative;} .expDateRow .cell-2 label.error{position:absolute; top:18px;} .expDate.error, .expYear.error{margin-bottom:16px;} .logoTxt-1{color:#fff; font-size:14px; font-weight:bold; padding:2px 0 0 0;} .logoTxt-2{color:#f4fb93; font-size:10px; font-weight:bold;} .hdrHTSpcr{height:53px;}
    .ech-cell-2{font-size:13px; margin-bottom:3px;} .ech-cell-2-1{float:left;} .ech-cell-2-2{float:left; margin:3px 0 0 3px;}
</style>

<form method="post" action="/index.php?s=billing.netBridgeUserRegister" name="joinpayform" id="joinpayform">
    <input type="hidden" id="token" name="token" value=""  />
    <div class="hdrMain">
        <div class="mainContainer">
            <div class="header clearfix">
                <div class="logo">
                    <div class="logoTxt-1">SECURE SSL PURCHASE FORM</div>
                    <div class="logoTxt-2">ANONYMOUS AND SAFE SSL TRANSACTION</div>
                </div>
                <div class="secure"><img src="/images/slutload/secure.png"></div>
            </div>
        </div>
    </div>
    <div class="mainContainer">
        <div class="hdrHTSpcr">
            <div class="hHeading">CollegeRules Mobile</div>
            <div class="hSubHeading">Fill out this form to join and get unlimited access now!</div>
        </div>
        <div class="form">
                <div class="frmHolder">
                                            <div class="eachRow clearfix">
                            <div class="cell-1">First name:</div>
                            <div class="cell-2">
                                <input type="text" id="firstName" name="firstName" value=""  />                                                            </div>
                        </div>
                                                                <div class="eachRow clearfix">
                            <div class="cell-1">Last name:</div>
                            <div class="cell-2">
                                <input type="text" id="lastName" name="lastName" value=""  />                                                            </div>
                        </div>
                                                                <div class="eachRow clearfix">
                            <div class="cell-1">Email Address:</div>
                            <div class="cell-2">
                                <input type="text" id="email" name="email" value=""  />                                                            </div>
                        </div>
                                        <div class="eachRow countryRow clearfix">
                        <div class="cell-1">Country:</div>
                        <div class="cell-2">
                            <select id="country" name="country" >
<option value="US">United States</option>
<option value="AF">Afghanistan</option>
<option value="AL">Albania</option>
<option value="DZ">Algeria</option>
<option value="AS">American Samoa</option>
<option value="AD">Andorra</option>
<option value="AO">Angola</option>
<option value="AI">Anguilla</option>
<option value="AQ">Antarctica</option>
<option value="AG">Antigua and Barbuda</option>
<option value="AR">Argentina</option>
<option value="AM">Armenia</option>
<option value="AW">Aruba</option>
<option value="AU">Australia</option>
<option value="AT">Austria</option>
<option value="AZ">Azerbaijan</option>
<option value="BS">Bahamas</option>
<option value="BH">Bahrain</option>
<option value="BD">Bangladesh</option>
<option value="BB">Barbados</option>
<option value="BY">Belarus</option>
<option value="BE">Belgium</option>
<option value="BZ">Belize</option>
<option value="BJ">Benin</option>
<option value="BM">Bermuda</option>
<option value="BT">Bhutan</option>
<option value="BO">Bolivia</option>
<option value="BA">Bosnia and Herzegovina</option>
<option value="BW">Botswana</option>
<option value="BV">Bouvet Island</option>
<option value="BR">Brazil</option>
<option value="IO">British Indian Ocean Territory</option>
<option value="BN">Brunei Darussalam</option>
<option value="BG">Bulgaria</option>
<option value="BF">Burkina Faso</option>
<option value="BI">Burundi</option>
<option value="KH">Cambodia</option>
<option value="CM">Cameroon</option>
<option value="CA">Canada</option>
<option value="CV">Cape Verde</option>
<option value="KY">Cayman Islands</option>
<option value="CF">Central African Republic</option>
<option value="TD">Chad</option>
<option value="CL">Chile</option>
<option value="CN">China</option>
<option value="CX">Christmas Island</option>
<option value="CC">Cocos (Keeling) Islands</option>
<option value="CO">Colombia</option>
<option value="KM">Comoros</option>
<option value="CG">Congo</option>
<option value="CD">Congo, the Democratic Republic of the</option>
<option value="CK">Cook Islands</option>
<option value="CR">Costa Rica</option>
<option value="CI">Cote D'Ivoire</option>
<option value="HR">Croatia</option>
<option value="CU">Cuba</option>
<option value="CY">Cyprus</option>
<option value="CZ">Czech Republic</option>
<option value="DK">Denmark</option>
<option value="DJ">Djibouti</option>
<option value="DM">Dominica</option>
<option value="DO">Dominican Republic</option>
<option value="TP">East Timor</option>
<option value="EC">Ecuador</option>
<option value="EG">Egypt</option>
<option value="SV">El Salvador</option>
<option value="GQ">Equatorial Guinea</option>
<option value="ER">Eritrea</option>
<option value="EE">Estonia</option>
<option value="ET">Ethiopia</option>
<option value="FK">Falkland Islands (Malvinas)</option>
<option value="FO">Faroe Islands</option>
<option value="FJ">Fiji</option>
<option value="FI">Finland</option>
<option value="FR">France</option>
<option value="GF">French Guiana</option>
<option value="PF">French Polynesia</option>
<option value="TF">French Southern Territories</option>
<option value="GA">Gabon</option>
<option value="GM">Gambia</option>
<option value="GE">Georgia</option>
<option value="DE">Germany</option>
<option value="GH">Ghana</option>
<option value="GI">Gibraltar</option>
<option value="GR">Greece</option>
<option value="GL">Greenland</option>
<option value="GD">Grenada</option>
<option value="GP">Guadeloupe</option>
<option value="GU">Guam</option>
<option value="GT">Guatemala</option>
<option value="GN">Guinea</option>
<option value="GW">Guinea-Bissau</option>
<option value="GY">Guyana</option>
<option value="HT">Haiti</option>
<option value="HM">Heard Island and Mcdonald Islands</option>
<option value="VA">Holy See (Vatican City State)</option>
<option value="HN">Honduras</option>
<option value="HK">Hong Kong</option>
<option value="HU">Hungary</option>
<option value="IS">Iceland</option>
<option value="IN">India</option>
<option value="ID">Indonesia</option>
<option value="IR">Iran, Islamic Republic of</option>
<option value="IQ">Iraq</option>
<option value="IE">Ireland</option>
<option value="IL">Israel</option>
<option value="IT">Italy</option>
<option value="JM">Jamaica</option>
<option value="JP">Japan</option>
<option value="JO">Jordan</option>
<option value="KZ">Kazakstan</option>
<option value="KE">Kenya</option>
<option value="KI">Kiribati</option>
<option value="KP">Korea, Democratic People's Republic of</option>
<option value="KR">Korea, Republic of</option>
<option value="KW">Kuwait</option>
<option value="KG">Kyrgyzstan</option>
<option value="LA">Lao People's Democratic Republic</option>
<option value="LV">Latvia</option>
<option value="LB">Lebanon</option>
<option value="LS">Lesotho</option>
<option value="LR">Liberia</option>
<option value="LY">Libyan Arab Jamahiriya</option>
<option value="LI">Liechtenstein</option>
<option value="LT">Lithuania</option>
<option value="LU">Luxembourg</option>
<option value="MO">Macau</option>
<option value="MK">Macedonia, the Former Yugoslav Republic of</option>
<option value="MG">Madagascar</option>
<option value="MW">Malawi</option>
<option value="MY">Malaysia</option>
<option value="MV">Maldives</option>
<option value="ML">Mali</option>
<option value="MT">Malta</option>
<option value="MH">Marshall Islands</option>
<option value="MQ">Martinique</option>
<option value="MR">Mauritania</option>
<option value="MU">Mauritius</option>
<option value="YT">Mayotte</option>
<option value="MX">Mexico</option>
<option value="FM">Micronesia, Federated States of</option>
<option value="MD">Moldova, Republic of</option>
<option value="MC">Monaco</option>
<option value="MN">Mongolia</option>
<option value="MS">Montserrat</option>
<option value="MA">Morocco</option>
<option value="MZ">Mozambique</option>
<option value="MM">Myanmar</option>
<option value="NA">Namibia</option>
<option value="NR">Nauru</option>
<option value="NP">Nepal</option>
<option value="NL">Netherlands</option>
<option value="AN">Netherlands Antilles</option>
<option value="NC">New Caledonia</option>
<option value="NZ">New Zealand</option>
<option value="NI">Nicaragua</option>
<option value="NE">Niger</option>
<option value="NG">Nigeria</option>
<option value="NU">Niue</option>
<option value="NF">Norfolk Island</option>
<option value="MP">Northern Mariana Islands</option>
<option value="NO">Norway</option>
<option value="OM">Oman</option>
<option value="PK">Pakistan</option>
<option value="PW">Palau</option>
<option value="PS">Palestine</option>
<option value="PA">Panama</option>
<option value="PG">Papua New Guinea</option>
<option value="PY">Paraguay</option>
<option value="PE">Peru</option>
<option value="PH">Philippines</option>
<option value="PN">Pitcairn</option>
<option value="PL">Poland</option>
<option value="PT">Portugal</option>
<option value="PR">Puerto Rico</option>
<option value="QA">Qatar</option>
<option value="RE">Reunion</option>
<option value="RO">Romania</option>
<option value="RU">Russian Federation</option>
<option value="RW">Rwanda</option>
<option value="SH">Saint Helena</option>
<option value="KN">Saint Kitts and Nevis</option>
<option value="LC">Saint Lucia</option>
<option value="PM">Saint Pierre and Miquelon</option>
<option value="VC">Saint Vincent and the Grenadines</option>
<option value="WS">Samoa</option>
<option value="SM">San Marino</option>
<option value="ST">Sao Tome and Principe</option>
<option value="SA">Saudi Arabia</option>
<option value="SN">Senegal</option>
<option value="SC">Seychelles</option>
<option value="SL">Sierra Leone</option>
<option value="SG">Singapore</option>
<option value="SK">Slovakia</option>
<option value="SI">Slovenia</option>
<option value="SB">Solomon Islands</option>
<option value="SO">Somalia</option>
<option value="ZA">South Africa</option>
<option value="GS">South Georgia and the South Sandwich Islands</option>
<option value="ES">Spain</option>
<option value="LK">Sri Lanka</option>
<option value="SD">Sudan</option>
<option value="SR">Suriname</option>
<option value="SJ">Svalbard and Jan Mayen</option>
<option value="SZ">Swaziland</option>
<option value="SE">Sweden</option>
<option value="CH">Switzerland</option>
<option value="SY">Syrian Arab Republic</option>
<option value="TW">Taiwan</option>
<option value="TJ">Tajikistan</option>
<option value="TZ">Tanzania, United Republic of</option>
<option value="TH">Thailand</option>
<option value="TG">Togo</option>
<option value="TK">Tokelau</option>
<option value="TO">Tonga</option>
<option value="TT">Trinidad and Tobago</option>
<option value="TN">Tunisia</option>
<option value="TR">Turkey</option>
<option value="TM">Turkmenistan</option>
<option value="TC">Turks and Caicos Islands</option>
<option value="TV">Tuvalu</option>
<option value="UG">Uganda</option>
<option value="UA">Ukraine</option>
<option value="AE">United Arab Emirates</option>
<option value="GB">United Kingdom</option>
<option value="UM">United States Minor Outlying Islands</option>
<option value="UY">Uruguay</option>
<option value="UZ">Uzbekistan</option>
<option value="VU">Vanuatu</option>
<option value="VE">Venezuela</option>
<option value="VN">Vietnam</option>
<option value="VG">Virgin Islands, British</option>
<option value="VI">Virgin Islands, U.S.</option>
<option value="WF">Wallis and Futuna</option>
<option value="EH">Western Sahara</option>
<option value="YE">Yemen</option>
<option value="YU">Yugoslavia</option>
<option value="ZM">Zambia</option>
<option value="ZW">Zimbabwe</option>
</select>                                                    </div>
                    </div>
                    <div class="eachRow clearfix">
                        <div class="cell-1">Credit Card Number:</div>
                        <div class="cell-2">
                            <input type="text" id="cardNumber" name="cardNumber" value=""  />                                                    </div>
                    </div>
                    <div class="eachRow expDateRow clearfix">
                        <div class="cell-1">Expiration Date:</div>
                        <div class="cell-2">
                                                            <select id="expMon" name="expMon" class="expDate">
<option value="01">01</option>
<option value="02">02</option>
<option value="03">03</option>
<option value="04">04</option>
<option value="05">05</option>
<option value="06">06</option>
<option value="07">07</option>
<option value="08">08</option>
<option value="09">09</option>
<option value="10">10</option>
<option value="11">11</option>
<option value="12">12</option>
<option value="" selected="selected">(month)</option>
</select>                            
                                                            <select id="expYear" name="expYear" class="expYear">
<option value="2014">2014</option>
<option value="2015">2015</option>
<option value="2016">2016</option>
<option value="2017">2017</option>
<option value="2018">2018</option>
<option value="2019">2019</option>
<option value="2020">2020</option>
<option value="2021">2021</option>
<option value="2022">2022</option>
<option value="2023">2023</option>
<option value="2024">2024</option>
<option value="2025">2025</option>
<option value="2026">2026</option>
<option value="2027">2027</option>
<option value="2028">2028</option>
<option value="2029">2029</option>
<option value="" selected="selected">(year)</option>
</select>                                                    </div>
                    </div>
                    <div class="eachRow cvvRow clearfix">
                        <div class="cell-1">CVV2:</div>
                        <div class="cell-2">
                            <span class="cvvAlt">(3 or 4 digit code on back of card)</span>
                            <input type="text" id="cvc" name="cvc" value=""  />                                                    </div>
                    </div>
                    <div class="eachRow zipRow clearfix">
                        <div class="cell-1">Zip/Postal Code:</div>
                        <div class="cell-2">
                            <input type="text" id="zip" name="zip" value=""  />                                                    </div>
                    </div>
                    <div class="eachRow typeRow clearfix">
                        <div class="cell-1">Membership Type:</div>
                        <div class="cell-2">
                                                        <div class="ech-cell-2 clearfix">
                                <div class="ech-cell-2-1"><input value="trial" type="radio" name="product" id="product" ></div>
                                <label for="memberType1" class="ech-cell-2-2"><b>$1.00</b> one-day trial</label>
                            </div>
                                                                                    <div class="ech-cell-2 clearfix">
                                <div class="ech-cell-2-1"><input value="monthly" type="radio" name="product" id="product" checked='true'></div>
                                <label for="memberType2" class="ech-cell-2-2"><b>$29.95</b> - per month</label>
                            </div>
                                                                                    <div class="ech-cell-2 clearfix">
                                <div class="ech-cell-2-1"><input value="annually" type="radio" name="product" id="product" ></div>
                                <label for="memberType3" class="ech-cell-2-2"><b>$89.95</b> - 365 Days</label>
                            </div>
                                                    </div>
                    </div>
                                            <div class="usrConfirm clearfix">
                            <input type="checkbox" id="xsale" name="xsale" value="mygf1p3" checked="checked"  />                            <label for="renewplancnfrm" class="gray">
                                Sign me up for a 1 day Membership to MyGf.com for $1.95. Renews automatically at $29.97 every 1 month.                            </label>
                        </div>
                                        <div class="btmMain">
                        <input type="button" id="paybtn" name="paybtn" onclick="return checkForm(this.form)" value="Complete this Transaction"/>
                    </div>
                    <div class="btmTxt-1 gray">By completing this transaction you agree to the <a href="http://www.collegerules.com/terms" target="_new">Terms and Conditions</a> of this purchase, read the <a href="http://www.collegerules.com/privacypolicy" target="_new">Privacy Policy</a>, certify that you are 18 years of age or older and understand the terms of billing.</div>
                    <div class="btmTxt-2">
                        Annual memberships renew at 9.95 every year.<br>
                        Trial memberships renew at 39.95 every 30 days.<br>
                        Monthly membership renew at 29.95 every 30 days.
                    </div>
                    <div class="btmTxt-3 gray">Your IP Address : 174.97.51.36 (Logged for fraud prevention)</div>
                </div>
                <input type="hidden" name="site" value="collegerules">
                <input type="hidden" name="prodId" value="271">
                <input type="hidden" name="tourForm" value="">
                <input TYPE="hidden" NAME="ioBB" id="ioBB"  value="">
                <input type="hidden" name="specials" value="">
                <input type="hidden" name="price" value="">
                                                            </form>
                    </div>
    </div>

    <script type="text/javascript">

        function checkForm(form) {
            try{
                form.paybtn.disabled = true;
                form.paybtn.value = "Please wait...";
                setTimeout("resetForm(form)", 20000);
                form.submit();
                return true;
            }
            catch(err) {}
        }

        function resetForm(form) {
            try{
                form.paybtn.disabled = false;
                form.paybtn.value = "Complete this Transaction";
            }
            catch(err) {}
            }
    </script>
    <img src="https://ctrack.trafficjunky.net/ctrack?action=list&type=add&id=join&context=collegerules&cookiename=client_tracking"/>          
    
</div>

<script type="text/javascript">window.NREUM||(NREUM={});NREUM.info={"beacon":"beacon-3.newrelic.com","licenseKey":"7804033129","applicationID":"1639130","transactionName":"NFdSMEcEXEBUU0cIDQ0dcxFGEV1eGkBSGA8GXEQ7WApQWllVYC0=","queueTime":0,"applicationTime":9,"ttGuid":"","agentToken":"","userAttributes":"","errorBeacon":"bam.nr-data.net","agent":"js-agent.newrelic.com\/nr-476.min.js"}</script></body>
</html>