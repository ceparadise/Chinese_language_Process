import os
import sys
import xml.etree.ElementTree as ET


class Extract(object):
    def __init__(self):
        self.f_loc = "/Users/zhengxx/PycharmProjects/annotate_original_data/"
        self.appenddir = "/Users/zhengxx/PycharmProjects/xml/"
        self.output = "/Users/zhengxx/PycharmProjects/output/"
        self.f = os.listdir(self.f_loc)

    def load_data(self):
        for x in self.f:
            if x.endswith('.xml'):
                fname = self.f_loc + x
                apname = self.appenddir + x
                outputname = self.output + x
                if os.path.exists(apname):
                    file_output = open(outputname, 'w')
                    infile = open(apname, 'r')
                else:
                    continue
                self.tree = ET.parse(fname)
                self.root = self.tree.getroot()
                dic = {}
                for child in self.root:
                    t = child[0][0].attrib['participant']
                    dic[child.attrib["id"]] = t

                for line in infile:
                    if line.startswith('suid='):
                        line = line.strip()
                        line = line + " participant=" + dic[line[5:]] + "\n"
                        file_output.write(line)
                    else:
                        file_output.write(line)


e = Extract()
e.load_data()