import pprint
import sys
import xml.etree.ElementTree as ET

tree = ET.parse(sys.argv[1])
root = tree.getroot()
clips = root.findall('.//audioClip')
things = ['sourceInPoint', 'sourceOutPoint', 'startPoint']
for c in clips:
    for t in things:
        newval = int(int(c.attrib[t]) * (48.0/44.1))
        print(t, c.attrib[t], newval)
        c.set(t, str(newval))

tree.write(sys.argv[1] + '- scaled.sesx')

# audioClip
# sourceInPoint
# sourceOutPoint
# startPoint
