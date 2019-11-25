#!/usr/bin/python3
import zbar
from PIL import Image
import os
import shutil

dir = '/home/pi/git/ck/pcid/plants'
for pic in os.listdir(dir):
	pic = dir + '/' + pic
	if '.py' in pic:
		pass
	else:
		for result in zbar.Scanner().scan(Image.open(pic).convert('L')):
			print(result.data)
			shutil.copy(pic, '/home/pi/git/ck/pc/' + str(result.data).split('/pc/')[1].replace("'", '') + '/plant.png')
