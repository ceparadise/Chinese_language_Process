import os
import shutil

class Getfid(object):
    def __init__(self):
        self.fin_loc = "E:\\CLP\\comparing\\"
        self.fout_loc = "E:\\CLP\\output_fid\\"
        self.fin=os.listdir(self.fin_loc)

    def spearetefid(self):
        for file in self.fin:
            if file.endswith('.fid'):
				shutil.copy(self.fin_loc+file, self.fout_loc+file)

if __name__=="__main__":
    e = Getfid()
    e.spearetefid()

