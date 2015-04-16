import  os

class Separetefiles(object):
    def __init__(self):
        self.inputf_loc="C:\\Users\\Liu\\Desktop\\pro\\bolt\\"
        #self.out_test_loc=""
        #self.out_train_loc=""
        self.test_list=[]
        self.train_list=[]

        self.inputf=os.listdir(self.inputf_loc)

    def load_data(self):

        step=len(self.inputf)/10

        for i in xrange(9):
            start = i*step
            end=(i+1)*step

            if end < len(self.inputf):
                self.test_list=self.inputf[start :end]
            else:
                self.test_list=self.inputf[start:]
            self.train_list=self.inputf[:start]
            self.train_list.extend(self.inputf[end:])
            print len(self.test_list)
            print len(self.train_list)

if __name__=="__main__":
    inst=Separetefiles()
    inst.load_data()
