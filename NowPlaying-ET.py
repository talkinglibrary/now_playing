'''
Print Now Playing metadata from TL Icecast server.

© Nashville Public Library
© Ben Weddle is to blame for this code. Anyone is free to use it.
'''

import xml.etree.ElementTree as ET
import requests

tree = ET.fromstring(requests.get('https://npl.streamguys1.com/admin/stats.xml', auth=('username', 'password')).text)
nowplaying = tree[23][30].text
print (nowplaying)


