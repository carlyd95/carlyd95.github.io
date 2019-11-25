#!/usr/bin/python3
import os
from os import path
from PIL import Image, ImageDraw, ImageFont
import urllib.request
import qrcode


f = open('pcid.tsv', 'r').read().split('\n')


for plant in f:
	p = plant.split('\t')
	cn = p[0]
	cv = p[1]
	gn = p[2]
	sp = p[3]
	ex = p[4]
	pa = p[5]
	lo = p[6]
	no = p[7]
	filename = '/home/pi/git/ck/pcid/labels/' + cn + '.png'
	if path.exists(filename) is False:
		if ' aff.' in sp:
			sp = sp.replace(' aff.', '-aff.')
		if ' hyb.' in sp:
                        sp = sp.replace(' hyb.', '-hyb.')
		if ' ' in sp:
			sp = sp.split()[-1]
		if '-aff.' in sp:
			sp = sp.replace('-aff.', ' aff.')
		if '-hyb.' in sp:
                        sp = sp.replace('-hyb.', ' hyb.')
		qr = qrcode.QRCode(version=2,error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=8, border=0)
		qr.add_data('carltons-karoo.com/pc/' + cn)
		qrc = qr.make_image()
		qrc = qrc.resize([109,109], Image.ANTIALIAS)
		img = Image.new('RGB', (900, 150), color = 'white')
		d = ImageDraw.Draw(img)
		font = ImageFont.truetype('VeraMoBd.ttf', 38)
		d.text((140, 13), sp.upper() + '\n' + cv.upper() + '\nCK ' + cn, fill=(0,0,0), font=font)
		img.paste(qrc, (20, 20))
		img.save(filename.replace(' ', ''), 'PNG')
	cndir = '/home/pi/git/ck/pc/' + cn
	if path.exists(cndir) is False:
		os.mkdir(cndir)
	temp = open('/home/pi/git/ck/pcid/pc.html', 'r').read()
	cnhtml = open(cndir + '/index.html', 'w+')
	cnhtml.write(temp.replace('$cn', 'CK ' + cn).replace('$cv', cv).replace('$gn', gn).replace('$sp', p[3]).replace('$ex', ex).replace('$pa', pa).replace('$lo', lo).replace('$no', no))
exit()

