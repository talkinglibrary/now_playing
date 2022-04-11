import xml.etree.ElementTree as ET
import requests

tree = ET.fromstring(requests.get('https://npl.streamguys1.com/admin/stats.xml', auth=('username', 'password')).text)
nowplaying = tree[23][30].text
print (nowplaying)

