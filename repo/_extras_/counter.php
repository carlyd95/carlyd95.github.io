<?php

include("connect.php");

$filename = mysql_real_escape_string($_GET['file']);
$path = $_SERVER['DOCUMENT_ROOT']."/"; 
$fullPath = $path.$filename; 

$filetypes = array("deb", "zip");

if (!in_array(substr($filename, -3), $filetypes)) {
	echo "Invalid download type.";
	exit;
}

if ($fd = fopen ($fullPath, "r")) {
	$result = mysql_query("SELECT COUNT(*) AS countfile FROM download
	WHERE filename='" . $filename . "'");
	$data = mysql_fetch_array($result);
	$q = "";
	
	if ($data['countfile'] > 0) {
		$q = "UPDATE download SET dldate = NOW()+INTERVAL x HOUR, stats = stats + 1 WHERE
		filename = '" . $filename . "'";
	} else {
		$q = "INSERT INTO download (filename, dldate, stats) VALUES
		('" . $filename . "',NOW()+INTERVAL x HOUR, 1)";
	}
	$statresult = mysql_query($q);
	
	$fsize = filesize($fullPath);
	$path_parts = pathinfo($fullPath);

	header("Content-type: application/octet-stream");
	header("Content-Disposition: filename=\"".$path_parts["basename"]."\"");
	header("Content-length: $fsize");
	header("Cache-control: private"); 
	while(!feof($fd)) {
		$buffer = fread($fd, 2048);
		echo $buffer;
	}
}
fclose ($fd);
exit;

?>