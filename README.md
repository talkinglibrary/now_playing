# nowplaying
print "Now Playing" metadata from TL Icecast server

Several different methods to parse the public-facing part of the TL Icecast server and return the "Now Playing" info (Icecast calls this "Current Song"). Javascript, Python, and PHP.

**JS/HTML**

The JS file outputs the text to the browser console. JS in included in the console_log.HTML file.

The TLNowPlaying.HTML file is an example of including the script directly on a page.

**PHP**

There are two PHP files. ReturnAll.php returns all info from Icecast, which is useful for testing.

ReturnOne.php returns only "Now Playing".

**Python**

There are two Python files.

NowPlaying-ET.py uses ElementTree, but credentials are required to access the raw xml.

NowPlaying-LXML.py uses lxml (and xpath). No credentials are needed.
