<?php

$server = "localhost"; 
$user = "yourusername"; 
$password = "yourpassword"; 
$database = mysql_connect ($server, $user, $password); 
mysql_select_db("yourdatabase", $database); 

?>