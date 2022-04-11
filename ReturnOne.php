<?php

// fetch "Now Playing" metadata from TL Icecast server

$source = "http://npl.streamguys1.com/status.xsl";
$index = 21;

$dom = new DOMDocument();
$dom->loadHTMLFile($source);
$tag = $dom->getElementsByTagName('td');
$result = $tag->item($index)->nodeValue;

echo $result;

?>