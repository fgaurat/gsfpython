import xml.etree.ElementTree as ET

tree = ET.parse('samples.xml')
root = tree.getroot()
print(root)
for child in root:
    print(child.tag, child.attrib)

# Top-level elements
all = root.findall(".")
for tag in all:
    print(tag.tag)

authors = root.findall(".//author")
for author in authors:
    print(author.text)
//*[@id="collapsible4"]/div[1]/div[1]/span[2]