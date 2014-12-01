<a href="<?php
$useragent = $_SERVER['HTTP_USER_AGENT'];
if(preg_match('/Macintosh/',$useragent)) $os = 'imessage';
elseif(preg_match('/iPhone/',$useragent)) $os = 'sms';
else $os = 'sms';
echo $os;
?>:dcarltondunlap@me.com">iMessage</a>