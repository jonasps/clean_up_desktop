
#!/usr/bin/env python

import os
import glob
import time
import shutil

class Desktop_organizer:
	"""This class moves files and folders into a directory called old_folders"""
	def __init__(self, *args):
		self.place = "Desktop"
		self.username = "jonassandstrom"
		self.do_not_move = ["Download", "webDownload", "customer","old_folders"]
		for arg in args:
			# add file or foldernames that you don't font to move
			self.do_not_move.append(arg)
		print("Not moving:")
		print(self.do_not_move)
		self.desktop_path ="/Users/"+self.username+"/"+self.place+"/"
		

	def create_folders(self):
		foldername = time.strftime("%m-%d-%Y-%s") 
		if not os.path.exists(self.desktop_path+"old_folders"):
			os.makedirs(self.desktop_path+"old_folders")
		if not os.path.exists(self.desktop_path+foldername):
			os.makedirs(self.desktop_path+"old_folders/"+foldername)
		return self.desktop_path+"old_folders/"+foldername

	def move_stuff_from_desktop(self):
		files = glob.glob(self.desktop_path+"*")
		if (len(files) - len(self.do_not_move)) > 0:
			print('Moving:')
			folder = self.create_folders()
			for f in files:
				filename = f.rsplit('/', 1)[-1]
				if filename not in self.do_not_move:
					shutil.move(f, folder)
					print(filename)

	def start_organize(self):
			self.move_stuff_from_desktop()


if __name__ == '__main__':
			my_desktop = Desktop_organizer()
			my_desktop.start_organize()