
<?php
$source = "http://npl.streamguys1.com/status.xsl";

$dom = new DOMDocument();
$dom->loadHTMLFile($source);
$books = $dom->getElementsByTagName('tr');
foreach ($books as $book) {
    echo $book->nodeValue, PHP_EOL;
}

?>
