<?php
$databaseHost = 'db';
$databaseName = 'test';
$databaseUsername = 'root';
$databasePassword = 'root';

$mysqli = mysqli_connect($databaseHost, $databaseUsername, $databasePassword, $databaseName); 

if (!$mysqli) {
    die("Ошибка подключения: " . mysqli_connect_error());
}
?>
