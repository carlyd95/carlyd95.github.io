#!/usr/bin/python3
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

#saves tsv table
f = open('pcid.tsv', 'w+')
f.write(tsv[:-2])
f.close()
exit()

