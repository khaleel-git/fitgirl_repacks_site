<?php

define( 'WP_USE_THEMES', true );
require( $_SERVER['DOCUMENT_ROOT'] . '/journal/wp-load.php' );		
require_once($_SERVER['DOCUMENT_ROOT'] . '/journal/wp-admin/includes/image.php'); 

$path    = '/home/apkfuel/public_html/journal/bulk_publish_posts/content/';
$files = scandir($path);

	// for ($i = 2; $i < count($files); $i++) # first two entries of array are single dot(.) and double dot(..)
    for ($i = 2; $i < 10; $i++) # first two entries of array are single dot(.) and double dot(..)
	{
	$appId = substr($files[$i]	, 0, -5);
    echo "$appId <br>";
	$get_json = file_get_contents("content/$files[$i]");
	$json_obj = json_decode($get_json, true);    	
    // echo $json_obj['body'];
    file_put_contents('test.txt', $json_obj['body']);
	include 'publish.php';
	}
?>
   