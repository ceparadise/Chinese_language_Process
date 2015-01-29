# -*- coding: utf-8 -*-
import os
import sys
import xml.etree.ElementTree as ET

class Generate(object):
    def __init__(self):
        self.f_loc = "C:\\liuclp\\June2014sms-with-pro\\"
        self.f = os.listdir(self.f_loc)
        
    def load_data(self):
        self.xmlfile = []
        for x in self.f:
            if x.endswith('.xml'):
                fname = self.f_loc+x
                self.xmlfile.append(fname)
        
    def extr_data(self):
        for x in self.xmlfile:
            self.tree = ET.parse(x)
            self.root = self.tree.getroot()
            #print root[1]
            #root[1] is all the tags
            for tags in self.root[1]:
                #print tags.tag, tags.attrib["type"], tags.attrib["start"], tags.attrib["end"]
                if tags.attrib["type"] == "unsure":
                    print tags.tag,tags.attrib["type"],tags.attrib["start"],tags.attrib["end"],
                    print self.locate(int(tags.attrib["start"]))
                    print

    
    def locate(self, start):
        self.text = self.root[0].text
        offsetid = []
        for i in range(len(self.text)):
            x = self.text[i]
            if x == "\n":
                offsetid.append(i)
        
        sentid = 0
        for i in range(len(offsetid)):
            off = offsetid[i]
            if start < off:
                print self.text[offsetid[i-1]+1:offsetid[i]],
                return sentid
            else:
                sentid += 1
        
                
e = Generate()
e.load_data()
e.extr_data()

