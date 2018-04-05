# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET


if __name__ == "__main__":
    tree = ET.parse('samples.xml')
    root = tree.getroot()
    print(root)