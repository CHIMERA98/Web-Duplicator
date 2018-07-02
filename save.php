<?php
$f = fopen("data.txt", "a");
$newline = readfile($f)."\n".$_GET["tosave"];
fwrite($f,$newline);
fclose($f);
?>
