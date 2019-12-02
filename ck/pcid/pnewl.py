#!/usr/bin/python3

#PCID.PY
import urllib.request

pc = urllib.request.urlopen("https://docs.google.com/spreadsheets/d/e/2PACX-1vT2MHgVCJ15KfuNScE9L0sIVL37FNmSOGWPgVjGIVdt6Q7B9Ny9qHHpK9iY_kkcrOvwsPvHZAZuzmqZ/pub?gid=0&single=true&output=tsv").read().decode('utf8').split('\n')
#deletes row of column titles
del pc[0]

#creates tree (complex nested dict/index)
pcx = {}
for line in pc:
    plant = line.split('\t')
    x = plant[1]
    y = plant[2]
    if x not in pcx:
    	pcx[x]=['0', {}]
    if y not in pcx[x][1]:
    	pcx[x][1][y]=['0', []]
    pcx[x][1][y][1].append(line)

#enumerates genera, species and plants in nests
gi = 1
for g in pcx:
	pcx[g][0] = gi
	gi = gi + 1
	si = 1
	for s in pcx[g][1]:
		pcx[g][1][s][0] = si
		si = si + 1
#		print s
		for p in pcx[g][1][s][1]:
			i = pcx[g][1][s][1].index(p)
			pcx[g][1][s][1][i] = f'{pcx[g][0]:0{1}X}' + f'{pcx[g][1][s][0]:0{2}X}' + f'{(i + 1):0{2}X}' + '\t' + p


#populates tsv from tree
tsv = ''
for g in pcx:
	for s in pcx[g][1]:
		for p in pcx[g][1][s][1]:
			tsv = tsv + p + '\n'

tsv = tsv[:-2]

#saves tsv table
f = open('pcid.tsv', 'w+')
f.write(tsv)
f.close()

#PC2PNG.PY
import os
from os import path
from PIL import Image, ImageDraw, ImageFont
import qrcode


f = tsv.split('\n')


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
	filename = '/home/pi/git/ck/pcid/newl/' + cn + '.png'
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

#PNEWL.PY
dir = '/home/pi/git/ck/pcid/newl'
for filename in os.listdir(dir):
	if '.png' in filename:
		os.system(f'lp -d CITIZEN_CL-S621Z {dir}/{filename}')
		os.system(f'mv {dir}/{filename} /home/pi/git/ck/pcid/currentl/')
exit()
