<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
<meta content="yes" name="apple-mobile-web-app-capable" />
<meta content="text/html; charset=UTF-8" http-equiv="Content-Type" />
<link href="images/apple-touch-icon.png" rel="apple-touch-icon" />
<meta content="minimum-scale=1.0, width=device-width, maximum-scale=0.6667, user-scalable=no" name="viewport" />
<link href="css/depiction.css" rel="stylesheet" type="text/css" />
<meta content="iPod,iPhone,theme,apps,cydia,apple" name="Keywords" />
</head>

<body>

<div align="center">
  <a href="http://[linkfromlogo]" target="_blank"><img src="images/banner.png" alt="alt tag here" width="300" /></a>
</div>

<div id="content">

  <ul class="pageitem">
    <li class="textbox">
	    <div align="center">Description of your App here</div>
    </li>
    <li class="textbox">
    	<div align="center">
        Downloads: <?PHP

include("../connect.php");

$query = "SELECT stats FROM download WHERE filename = 'files/[NameOfPackage].deb'";

$result = mysql_query($query);

while ($row = mysql_fetch_array($result)) {

echo $row[0];
}

?>
		</div>
	</li>
  </ul>

	<ul class="pageitem">
		<li class="menu">
		  <a href="screenshots/[NameOfPackage].htm" target="_blank"><span class="name">Screenshots</span><span class="arrow"></span></a>
		</li>
		<li class="menu">
		  <a href="http://[yourwebsiteURL]" target="_blank"><span class="name">Website</span><span class="arrow"></span></a>
		</li>
	</ul>
<br />

</div>
</body>
</html>