import shutil
import os
import math
#the folder to split
source = "/home/sajid/Desktop/zeus/"
#Chunk reflects how many files for each sub-directory
chunk=150
files = os.listdir(source)
total = len(files)
part = math.ceil((total/chunk))
for subdir in range(0, part):
	moved = 0
	command = 'mkdir '+source+"part"+str(subdir)
	os.system(command)
	#update the file list
	files = [x for x in os.listdir(source) if os.path.isfile(source+x)]
	for f in files:
		if moved < chunk:
			dest = source+"part"+str(subdir)
			command = 'mv '+source+f+ ' '+dest
			os.system(command)
			moved = moved + 1
		else:
			continue


