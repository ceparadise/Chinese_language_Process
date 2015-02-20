import os
import shutil
class deletefid():
	def __init__(self):
		self.xmlfile = []
		self.ori_loc = "C:\\Users\\Liu\\Desktop\\comparing\\"
		self.output_loc = "C:\\Users\\Liu\\Desktop\\xml\\"
		self.f = os.listdir(self.ori_loc)

	def load_data(self):
		for x in self.f:
			if x.endswith('.xml'):
				shutil.copy(self.ori_loc+x, self.output_loc+x)
	def find_unanotate(self):
		for x in self.f:
			if x.endswith('.fid'):
				x = x[:-3]+'xml'
				if x not in self.f:
					print x

if __name__ == "__main__":
	e = deletefid()
	e.find_unanotate()