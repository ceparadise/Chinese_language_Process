#-*- coding: utf-8 -*-
import os
import xml.etree.ElementTree as ET
import codecs


class CompareXml(object):
    def __init__(self):
        self.xmlfile = []
        self.comparef_loc = "C:\\Users\\Liu\\Desktop\\comparing\\"
        self.standf_loc = "C:\\Users\\Liu\\Desktop\\standard\\"
        self.output = "C:\\Users\\Liu\\Desktop\\comparing\\result.txt"
        self.standf = os.listdir(self.standf_loc)
        self.comparef=os.listdir(self.comparef_loc)
        self.error_count = {}
        '''count the comparing file error in different types'''
        self.total_count = {}
        '''count the total in different types'''
        self.result = codecs.open(self.output,'w',encoding='utf8')


    def load_data(self):
        for x in self.standf:
            if x.endswith('.xml'):
                standf_name = self.standf_loc + x
                '''
                standard tree 
                '''
                if x not in self.comparef:
                    continue
                self.tree = ET.parse(standf_name)
                self.root = self.tree.getroot()
                #text = self.root[0].text
                dic_start_tag = {}
                for tags in self.root[1]:
                    start = int(tags.attrib["start"])
                    pron = tags.tag
                    dic_start_tag[start] = pron
                    self.total_count[pron] = self.total_count.get(pron,0)+1
                '''
                ctree is the compare tree and text 
                '''
                comparef_name = self.comparef_loc + x
                self.ctree = ET.parse(comparef_name)
                self.croot = self.ctree.getroot()
                #ctext = self.croot[0].text
                for tags in self.croot[1]:
                    '''all the tags in compare tree'''
                    cstart = int(tags.attrib["start"])
                    cpron = tags.tag
                    if dic_start_tag.has_key(cstart):
                        if cpron != dic_start_tag[cstart]: 
                            right_pro=dic_start_tag[cstart]
                            self.error_count[right_pro]=self.error_count.get(right_pro,0)+1
                            #print self.locate(cstart),'compare: ',cpron, 'standard: ',dic_start_tag[cstart]
                            self.result.write(self.locate(cstart)+'\t compare: '+cpron+'\t standard: '+dic_start_tag[cstart]+'\n')
                    
                    elif dic_start_tag.has_key(cstart-1):
                        if cpron != dic_start_tag[cstart-1]:
                            right_pro=dic_start_tag[cstart-1]
                            self.error_count[right_pro]=self.error_count.get(right_pro,0)+1
                            self.result.write(self.locate(cstart-1)+'\t compare: '+cpron+'\t standard: '+dic_start_tag[cstart-1]+'\n')
                    
                    elif dic_start_tag.has_key(cstart-2):
                        if cpron != dic_start_tag[cstart-2]:
                            right_pro=dic_start_tag[cstart-2]
                            self.error_count[right_pro]=self.error_count.get(right_pro,0)+1
                            self.result.write(self.locate(cstart-2)+'\t compare: '+cpron+'\t standard: '+dic_start_tag[cstart-2]+'\n')
                        
                    elif dic_start_tag.has_key(cstart+1):
                        if cpron != dic_start_tag[cstart+1]:
                            right_pro=dic_start_tag[cstart+1]
                            self.error_count[right_pro]=self.error_count.get(right_pro,0)+1
                            self.result.write(self.locate(cstart+1)+'\t compare: '+cpron+'\t standard: '+dic_start_tag[cstart+1]+'\n')
                    
                    elif dic_start_tag.has_key(cstart+2):
                        if cpron != dic_start_tag[cstart+2]:
                            right_pro=dic_start_tag[cstart+2]
                            self.error_count[right_pro]=self.error_count.get(right_pro,0)+1
                            self.result.write(self.locate(cstart+2)+'\t compare: '+cpron+'\t standard: '+dic_start_tag[cstart+2]+'\n')
                        
                    else:
                        print "mismatch"
                        print 'compare:',cpron,cstart,'filename=',x
                        print self.locate(cstart)
                        #self.result.write(cpron + ' '+ cstart)
                        #raise Exception("start match not found ")

    def calculation(self):
        for pron in self.total_count.keys():
            self.result.write(pron + ' '+ str(self.error_count.get(pron,0)/float(self.total_count[pron]))+'\n')
            
        
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

                #self.result.write( self.text[offsetid[i-1]+1:offsetid[i]])
                return self.text[offsetid[i-1]+1:offsetid[i]]
                #print self.text[offsetid[i-1]+1:offsetid[i]],
                #return sentid
            else:
                sentid += 1

                       
                    
if __name__ =="__main__":
    e = CompareXml()
    e.load_data()
    e.calculation()
    print 'finish'
                    
                    
                    
                    
                    
                    
                    
                    
                    
                
                