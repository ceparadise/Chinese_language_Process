#-*- coding: utf-8 -*-
import os
import xml.etree.ElementTree as ET
import codecs


class Comparexml(object):
    def __init__(self):
        self.xmlfile = []
        self.comparef_loc = "C:\\Users\\Liu\\Desktop\\Liu_Final\\"
        self.standf_loc = "C:\\Users\\Liu\\Desktop\\Wang_Final\\"
        
        self.standf = os.listdir(self.standf_loc)
        self.comparef=os.listdir(self.comparef_loc)


    def load_data(self):
        for x in self.standf:
            if x.endswith('.xml'):
                standf_name = self.standf_loc + x
                '''
                standard tree 
                '''
                if x not in self.comparef:
                    print x
                    continue
if __name__ =="__main__":
    e = Comparexml()
    e.load_data()
    print 'finish'
                    