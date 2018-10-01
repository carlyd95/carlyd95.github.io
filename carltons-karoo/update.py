#! /usr/bin/env python 

import os

Aizocaceae = ['lithops']
Asphodelaceae = ['Aloe', 'Astroloba', 'Gasteria', 'Haworthia', 'Haworthiopsia', 'Tulista']
Cactaceae = ['Ariocarpus', 'Astrophytum', 'Frailea', 'Gymnocalycium', 'Lophophora', 'Melocactus']
Euphorbiaceae = ['Euphorbia']
Hyacinthaceae = ['Schizobasis', 'Boweia']
Asclepiadaceae = ['Huernia', 'Stapelia', 'Orbea', 'Duvalia', 'Rhytidocaulon', 'Trichocaulon']
Portulacaceae = ['Avonia', 'Crassula']

family = {'a':Aizocaceae, 'b':Asphodelaceae, 'c':Cactaceae, 'd':Euphorbiaceae, 'e':Hyacinthaceae, 'f':Asclepiadaceae, 'g':Portulacaceae}



for line in (os.listdir( os.environ['HOME'] + "/git/carltons-karoo/pics/seeds")):
	if line.endswith(('.jpg')):
		print line.replace('.', '	').replace('jpg', 'jpg')
