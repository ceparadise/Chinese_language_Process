#-*- coding: utf-8 -*-
import os
import xml.etree.ElementTree as ET
import codecs


class CompareXml(object):
    def __init__(self):
        self.xmlfile = []
        self.comparef_loc = "E:\\CLP\\liu_new\\"
        self.standf_loc = "E:\\CLP\\wang_new\\"
        self.output = "E:\\CLP\\result.txt"
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
                dic_pron_tag = {}
                dic_generic_tag = {}
                dic_refer_tag = {}
                dic_event_tag = {}
                dic_pre_tag = {}
                dic_ple_tag = {}
                dic_exi_tag = {}
                for tags in self.root[1]:
                    start = int(tags.attrib["start"])
                    pron = tags.tag
                    if pron=='other':
                        continue
                    generic = str(tags.attrib["generic"])
                    refer = str(tags.attrib["referential"])
                    event = str(tags.attrib["event"])
                    pre = str(tags.attrib["pre_utter"])
                    ple = str(tags.attrib["pleonastic"])
                    exi = str(tags.attrib["existential"])
                    dic_pron_tag[start] = pron
                    dic_generic_tag[start] = generic
                    dic_refer_tag[start] = refer
                    dic_event_tag[start] = event
                    dic_pre_tag[start] = pre
                    dic_ple_tag[start] = ple
                    dic_exi_tag[start] = exi
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
                    cpron = tags.tag
                    cstart = int(tags.attrib["start"])
                    if cpron!='other':
                        cgeneric = str(tags.attrib["generic"])
                        crefer = str(tags.attrib["referential"])
                        cevent = str(tags.attrib["event"])
                        cpre = str(tags.attrib["pre_utter"])
                        cple = str(tags.attrib["pleonastic"])
                        cexi = str(tags.attrib["existential"])

                    if dic_pron_tag.has_key(cstart):
                        if cpron != dic_pron_tag[cstart]:
                            right_pro=dic_pron_tag[cstart]
                            self.error_count[right_pro]=self.error_count.get(right_pro,0)+1
                            #print self.locate(cstart),'compare: ',cpron, 'standard: ',dic_pron_tag[cstart]
                            self.result.write(x+'\n'+self.locate(cstart)+'\t Liu: '+cpron+'\t Wang: '+dic_pron_tag[cstart]+'\n\n')
                        if cpron == dic_pron_tag[cstart]:
                            if cgeneric != dic_generic_tag[cstart]:
                                self.result.write(x+'\n'+self.locate(cstart)+'\t\t'+cpron+'\t generic Liu:'+'\t'+cgeneric+'\t Wang: '+dic_generic_tag[cstart]+'\n\n')
                            if crefer != dic_refer_tag[cstart]:
                                self.result.write(x+'\n'+self.locate(cstart)+'\t\t'+cpron+'\t refer Liu:'+'\t'+crefer+'\t Wang: '+dic_refer_tag[cstart]+'\n\n')
                            if cevent != dic_event_tag[cstart]:
                                self.result.write(x+'\n'+self.locate(cstart)+'\t\t'+cpron+'\t event Liu:'+'\t'+cevent+'\t Wang: '+dic_event_tag[cstart]+'\n\n')
                            if cpre != dic_pre_tag[cstart]:
                                self.result.write(x+'\n'+self.locate(cstart)+'\t\t'+cpron+'\t pre_utterance Liu:'+'\t'+cpre+'\t Wang: '+dic_pre_tag[cstart]+'\n\n')
                            if cple != dic_ple_tag[cstart]:
                                self.result.write(x+'\n'+self.locate(cstart)+'\t\t'+cpron+'\t pleonastic Liu:'+'\t'+cple+'\t Wang: '+dic_ple_tag[cstart]+'\n\n')
                            if cexi != dic_exi_tag[cstart]:
                                self.result.write(x+'\n'+self.locate(cstart)+'\t\t'+cpron+'\t existential Liu:'+'\t'+cexi+'\t Wang: '+dic_exi_tag[cstart]+'\n\n')
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
                return self.text[offsetid[i-4]+1:offsetid[i]]
                #print self.text[offsetid[i-1]+1:offsetid[i]],
                #return sentid
            else:
                sentid += 1



if __name__ =="__main__":
    e = CompareXml()
    e.load_data()
    e.calculation()
    print 'finish'
