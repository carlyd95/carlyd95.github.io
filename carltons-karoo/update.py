#! /usr/bin/env python 

import os

Aizocaceae = {'lit':'lithops'}
Asphodelaceae = ['aloe', 'astroloba', 'gasteria', 'haworthia', 'haworthiopsia', 'tulista']
Cactaceae = ['ariocarpus', 'astrophytum', 'frailea', 'gymnocalycium', 'lophophora', 'melocactus']
Euphorbiaceae = ['euphorbia']
Hyacinthaceae = ['schizobasis', 'boweia']
Asclepiadaceae = ['huernia', 'stapelia', 'orbea', 'duvalia', 'rhytidocaulon', 'trichocaulon']
Portulacaceae = ['Avonia', 'Crassula']

family = {'a':Aizocaceae, 'b':Asphodelaceae, 'c':Cactaceae, 'd':Euphorbiaceae, 'e':Hyacinthaceae, 'f':Asclepiadaceae, 'g':Portulacaceae}


for line in (os.listdir( os.environ['HOME'] + "/git/carltons-karoo/pics/seeds")):
	if line.endswith(('.jpg')):
		print line.replace('.', '	').replace('jpg', 'jpg')


Aizocaceae = {'Cha': 'Chasmatophyllum', 'Hal': 'Halimus', 'Che': 'Cheiridopsis', 'Gib': 'Gibbaeum', 'Van': 'Vanheerdea', 'Har': 'Hartmanthus', 'Jac': 'Jacobsenia', 'Ham': 'Hammeria', 'Psi': 'Psilocaulon', 'Bij': 'Bijlia', 'Dac': 'Dactylopsis', 'Mos': 'Mossia', 'Psa': 'Psammophora', 'Gas': 'Gasoul', 'Phy': 'Phyllobolus', 'Fau': 'Faucaria', 'Imi': 'Imitaria', 'Mon': 'Monilaria', 'Opo': 'Opophytum', 'Oph': 'Ophthalmophyllum', 'Cyl': 'Cylindrophyllum', 'Tri': 'Trichodiadema', 'Din': 'Dinteranthus', 'Pla': 'Platythyra', 'Aiz': 'Aizoon', 'Car': 'Carruanthus', 'Hym': 'Hymenocyclus', 'Ais': 'Aistocaulon', 'Dic': 'Dicrocaulon', 'Ere': 'Erepsia', 'Dip': 'Diplosoma', 'Pre': 'Prepodesma', 'Rab': 'Rabiea', 'Sph': 'Sphalmanthus', 'Rim': 'Rimaria', 'Ebr': 'Ebracteola', 'Arg': 'Argyroderma', 'Ari': 'Aridaria', 'Tan': 'Tanquana', 'Neo': 'Neohenricia', 'Per': 'Perapentacoilanthus', 'Pen': 'Pentacoilanthus', 'Lud': 'Ludolfia', 'Smi': 'Smicrostigma', 'Pee': 'Peersia', 'Pun': 'Punctillaria', 'Ort': 'Orthopterum', 'Men': 'Mentocalyx', 'Ple': 'Pleiospilos', 'Mes': 'Mestoklema', 'Rus': 'Ruschianthus', 'Mey': 'Meyerophytum', 'Bol': 'Bolusanthemum', 'Dro': 'Drosanthemum', 'Dra': 'Dracophilus', 'Sto': 'Stomatium', 'Sch': 'Schwantesia', 'Roo': 'Roodia', 'Sce': 'Sceletium', 'Pte': 'Pteropentacoilanthus', 'Apt': 'Aptenia', 'Ihl': 'Ihlenfeldtia', 'Osc': 'Oscularia', 'Ver': 'Verrucifera', 'Ves': 'Veslingia', 'Her': 'Hereroa', 'Fen': 'Fenestraria', 'Fri': 'Frithia', 'Hen': 'Henricia', 'Jen': 'Jensenobotrya', 'Cer': 'Cerochlamys', 'Jut': 'Juttadinteria', 'Cep': 'Cephalophyllum', 'Amp': 'Amphibolia', 'Dep': 'Depacarpus', 'Der': 'Derenbergia', 'Cry': 'Cryophytum', 'Sti': 'Stigmatocarpum', 'Dei': 'Deilanthe', 'Del': 'Delosperma', 'Ber': 'Bergeranthus', 'Cro': 'Crocanthus', 'Ses': 'Sesuvium', 'Ani': 'Anisocalyx', 'Ant': 'Antimima', 'Odo': 'Odontophorus', 'Tet': 'Tetragonia', 'Mim': 'Mimetophytum', 'Tit': 'Titanopsis', 'Nan': 'Nananthus', 'Nam': 'Namibia', 'Lit': 'Litocarpus', 'Abr': 'Abryanthemum', 'Nyc': 'Nycteranthus', 'Mit': 'Mitrophyllum', 'Pyx': 'Pyxipoma', 'Lam': 'Lampranthus', 'Mar': 'Marlothistella', 'Mau': 'Maughaniella', 'Ast': 'Astridia', 'Syn': 'Synaptophyllum', 'Ech': 'Echinus', 'Rhi': 'Rhinephyllum', 'Mac': 'Machairophyllum', 'Rho': 'Rhombophyllum', 'Lap': 'Lapidaria', 'Mal': 'Malephora', 'Aca': 'Acaulon', 'Cor': 'Corpuscularia', 'Glo': 'Glottiphyllum', 'Acr': 'Acrodon', 'Con': 'Conophytum', 'Alo': 'Aloinopsis', 'Bra': 'Braunsia'}


cactaceae = ['Echinopsis', 'Acanthocalycium', 'Parodia', 'Acanthocereus', 'Lepismium', 'Acharagma', 'Tunilla', 'Cleistocactus', 'Sclerocactus', 'Andinopuntia', 'Ariocarpus', 'Pachycereus', 'Disocactus', 'x Aporoheliocereus', 'Oreocereus', 'Armatocereus', 'Arrojadoa', 'Arrojadoopsis', 'Arthrocereus', 'Epiphyllum', 'Astrobergia', 'Astrophytum', 'Coryphantha', 'Austrocactus', 'Micranthocereus', 'Austrocylindropuntia', 'Rebutia', 'Aztekium', 'Browningia', 'Banfiopuntia', 'Mammillaria', 'Bergerocactus', 'Espostoa', 'Ferocactus', 'Blossfeldia', 'x Borzipostoa', 'Gymnocalycium', 'Brachycereus', 'Bragaia', 'Brasilicereus', 'Brasiliopuntia', 'Turbinicarpus', 'Bridgesia', 'Brittonia', 'Stenocactus', 'Coleocephalocereus', 'Opuntia', 'Cactus', 'Calymmanthium', 'Carnegiea', 'Pereskia', 'Cassyta', 'Cassytha', 'Cephalocereus', 'Cephalocleistocactus', 'Epithelantha', 'Eriosyce', 'Cereus', 'Polaskia', 'Cintia', 'Cipocereus', 'Maihueniopsis', 'Escobaria', 'Consolea', 'Copiapoa', 'Corryocactus', 'Grusonia', 'Selenicereus', 'Peniocereus', 'Cumulopuntia', 'Cylindropuntia', 'Dendrocereus', 'Denmoza', 'Discocactus', 'Weberocereus', 'Echinocactus', 'Echinocereus', 'x Echinoferocactus', 'Echinomastus', 'Echinonyctanthus', 'Encephalocarpus', 'Matucana', 'x Epinicereus', 'Schlumbergera', 'Hatiora', 'x Eriocereopsis', 'Harrisia', 'Rhipsalis', 'Escontria', 'x Espostocactus', 'Espostoopsis', 'Estevesia', 'Eulychnia', 'Euporteria', 'Facheiroa', 'x Ferenocactus', 'x Ferobergia', 'x Doweld', 'Frailea', 'Geohintonia', 'Gymnantha', 'Haageocereus', 'x Haagespostoa', 'Thelocactus', 'x Harrisinopsis', 'x Heliaporus', 'Stenocereus', 'Hylocereus', 'Hymenolobivia', 'Isolatocereus', 'Jasminocereus', 'Stephanocereus', 'Lasiocereus', 'Leocereus', 'Leptocereus', 'Leuchtenbergia', 'Leuenbergeria', 'Lophophora', 'Loxanthocereus', 'Maihuenia', 'Mammilloydia', 'Melocactus', 'Mila', 'Miqueliopuntia', 'Monvillea', 'Morangaya', 'x Myrtgerocactus', 'Myrtillocactus', 'x Myrtillocalycium', 'Neolloydia', 'Pediocactus', 'x G.D.Rowley', 'Neobuxbaumia', 'Neoraimondia', 'Neolemaireocereus', 'Echidnopsis', 'Neomatucana', 'Neotanahashia', 'Neowerdermannia', 'Nichelia', 'Nyctocereus', 'Obregonia', 'Oroya', 'Ortegocactus', 'x Ortegopuntia', 'x Pacherocactus', 'x Pachgerocereus', 'Pelecyphora', 'Pereskiopsis', 'Pfeiffera', 'Pierrebraunia', 'Pilosocereus', 'Praecereus', 'Pseudoacanthocereus', 'Pseudoechinopsis', 'Pseudomaihueniopsis', 'Pseudorhipsalis', 'Pterocactus', 'Punotia', 'Pygmaeocereus', 'Quiabentia', 'Rauhocereus', 'Rhipsaphyllopsis', 'Rowleyara', 'Obesia', 'Samaipaticereus', 'x Seleniphyllum', 'Sphaeropuntia', 'x Stenogonia', 'Stetsonia', 'Strombocactus', 'Tacinga', 'Tephrocactus', 'x Thelobergia', 'Toumeya', 'x Trichopsis', 'Tunas', 'Uebelmannia', 'Weberbauerocereus', 'Yavia', 'Yungasocereus']


fam=[]

for line in (os.listdir("/Usercactus.txts/carlyd95/git/carltons-karoo/pics/plants")):i
	if line.startswith("."):
		exit
	else:


f = open("file.txt", "a")
dic={}

def imageLinker(family):
	for line in (os.listdir(os.environ['HOME'] + "git/carltons-karoo/pics/plants/" + family))
		f.write()
fam={"e":"Euphorbiaceae"}
def decy(filename):
	list=filename.replace("-", "\n").split()
	dic[filename]=filename.replace(".JPG", "").replace("$", "\n").replace(list[0] + "-", fam.get(list[0])).replace("-", "\n")


naming format = fam + gen + (species + X) + price + .ext 

 eup~eup~baioensis~12.JPG
cac~cop~cinerea~45.JPG

def decy(filename):
	namelist=filename.replace('&', '\n').replace('.JPG', '').split()
	namelist[0]=plantlist.get(namelist[0])[0]
	namelist[1]=plantlist.get(namelist[0])[1].get(namelist[1])
	namelist[3]='$' + namelist[3]





for entry in fam:
...     for entry2 in fam.get(entry)[1]:
...             if entry2 == 'Lit':
...                      print(fam.get(entry)[1].get(entry2))


for line in cactus:
	if '=' in line:
		list.append(line.split('=')[1])
	else:
		list.append(line)
... 
>>> list

