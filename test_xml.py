# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET

if __name__ == "__main__":
    tree = ET.parse('samples.xml')
    root = tree.getroot()
    authors = root.findall('.//author')
    for author in authors:
        print (author.text)
    print(50*'-')
    book_bk108 = root.find('./book[@id="bk108"]')
    print(book_bk108.attrib)

    for c in book_bk108.findall('./'):
        print(c.tag,repr(c.text))

    
    
    # for child in root:
    #     attrs = child.attrib.keys()
        

        # print(child.tag,child.attrib['id'])