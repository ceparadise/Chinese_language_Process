# -*- coding:utf-8 -*-
import os
import sys
import xml.etree.ElementTree as ET
'''
correct the pro's offset
'''

class Correctpro(object):
    def __init__(self):
        self.f_loc = "C:\\Users\\Liu\\Desktop\\Working\\"
        self.output = "C:\\Users\\Liu\\Desktop\\Working\\test_data\\"
        self.f = os.listdir(self.f_loc)

    def load_data(self):
        for fi in self.f:
            if fi.endswith('.xml'):
                fname = self.f_loc + fi
                outputname = self.output + fi
                self.tree = ET.parse(fname)
                self.root = self.tree.getroot()
                for tags in self.root[1]:
                    start = int(tags.attrib["start"])
                    end = int(tags.attrib["end"])
                    text = tags.attrib["text"]
                    if text == "*pro*":
                        print text
                        tags.attrib["text"]="pro"

                    if text == " *pro*":
                        print text
                        tags.attrib["text"]="pro"

                    if text == "*pro* ":
                        print text
                        tags.attrib["text"]="pro"

                    if text == " *pro* ":
                        print text
                        tags.attrib["text"]="pro"

                    if end-start == 5:
                        start = start+1
                        end = end-1
                        tags.attrib["start"]=str(start)
                        tags.attrib["end"]=str(end)
                    else:
                        pass

                self.tree.write(outputname, encoding="UTF-8", xml_declaration=True)


e = Correctpro()
e.load_data()
