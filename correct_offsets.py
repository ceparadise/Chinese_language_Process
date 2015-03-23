# -*- coding:utf-8 -*-


import os
import sys
import xml.etree.ElementTree as ET
'''
correct the pro's offset
'''

class Extract(object):
    def __init__(self):
        self.f_loc = "C:\\liuclp\\annotate_original_data\\"
        self.appenddir = "C:\\liuclp\\comparing\\output\\"
        self.output = "C:\\liuclp\\correct_offsets\\"
        self.f = os.listdir(self.f_loc)

    def load_data(self):
        for fi in self.f:
            if fi.endswith('.xml'):
                fname = self.f_loc + fi
                apname = self.appenddir + fi
                outputname = self.output + fi
                if os.path.exists(apname):
                    file_output = open(outputname, 'w')
                    infile = open(apname, 'r')
                else:
                    continue
                self.tree = ET.parse(fname)
                self.root = self.tree.getroot()

                standard_tree = ET.parse(apname)
                standard_root = standard_tree.getroot()[1]
                start = []
                end = []
                index = {}
                bug = []
                for child in standard_root:
                    # print child.attrib['id']
                    start.append(int(child.attrib['start']))
                    end.append(int(child.attrib['end']))
                start.sort()
                end.sort()

                for i in range(len(start)):
                    index[start[i]] = i

                new_start = []
                new_end = []
                x = standard_tree.getroot()[0]
                text = x.text
                count = 0
                # print len(text)
                for i in range(len(text)):
                    try:
                        if i + 5 >= len(text):
                            break
                        if text[i:i+5] == '*pro*':
                            # print text[i:i+5]
                            if end[count] - start[count] == 3:
                                new_start.append(i + 1)
                                new_end.append(i + 1 + end[count] - start[count])
                                count += 1
                            else:
                                new_start.append(i)
                                new_end.append(i + end[count] - start[count])

                    except Exception as e:
                        print fi
                        continue
                for child in standard_root:
                    try:
                        x = index[int(child.attrib['start'])]
                        child.attrib['start'] = str(new_start[x])
                        child.attrib['end'] = str(new_end[x])
                    except Exception as e:
                        print fi
                        continue

                standard_tree.write(outputname, encoding="UTF-8", xml_declaration=True)

                # for line in infile:
                #     if line.startswith('suid='):
                #         line = line.strip()
                #         line = line + " participant=" + dic[line[5:]] + "\n"
                #         participant_count = len(" participant=" + dic[line[5:]])
                #         file_output.write(line)
                #     elif line.count('*pro*') > 0 and line.count('text=') == 0:
                #         n = line.count('*pro')
                #         while n > 0:
                #             start[count] += participant_count
                #             end[count] += participant_count
                #             count += 1
                #             n -= 1
                #             index = line.index('*pro*')
                #             line = line[index + 5:]
                #     else:
                #         file_output.write(line)


e = Extract()
e.load_data()