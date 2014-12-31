<?PHP

include("connect.php");

$result = mysql_query("SELECT * FROM download ORDER BY stats DESC");

echo "<table border='1' align='center'>";
echo "<tr> <th> Deb </th> <th> Downloads </th> <th> Last downloaded </th> </tr>";

while($row = mysql_fetch_array($result)) {

$trimed1 = str_replace("files/", "", $row[filename]);
$trimed2 = str_replace(".deb", "", $trimed1);

echo "<tr> <td> $trimed2 </td> <td> $row[stats] </td> <td> $row[dldate] </td> </tr>";

}

echo "</table>"

?>