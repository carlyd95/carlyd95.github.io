#!/bin/python2.7

import os

Aizocaceae = ['lithops']
Asphodelaceae = ['Aloe', 'Astroloba', 'Gasteria', 'Haworthia', 'Haworthiopsia', 'Tulista']
Cactaceae = ['Ariocarpus', 'Astrophytum', 'Frailea', 'Gymnocalycium', 'Lophophora', 'Melocactus']
Euphorbiaceae = ['Euphorbia']
Hyacinthaceae = ['Schizobasis', 'Boweia']
Asclepiadaceae = ['Huernia', 'Stapelia', 'Orbea', 'Duvalia', 'Rhytidocaulon', 'Trichocaulon']
Portulacaceae = ['Avonia', 'Crassula']

family = {'a':Aizocaceae, 'b':Asphodelaceae, 'c':Cactaceae, 'd':Euphorbiaceae, 'e':Hyacinthaceae, 'f':Asclepiadaceae, 'g':Portulacaceae}



for line in (os.listdir("/Users/carlyd95/git/carltons-karoo/pics")):
		if line.endswith(('.jpg')):
			list line.replace('.', '')