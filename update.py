#! /usr/bin/env python 
# -*- coding: utf-8 -*-
import os
'''
asp = ['Aloe', 'Aloiampelos', 'Aloidendron', 'Aloinella', 'x Alworthia', 'Apicra', 'Aristaloe', 'Astroloba', 'x Astroworthia', 'Busipho', 'Catevala', 'x Gasteraloe', 'x Gasterhaworthia', 'Gasteria', 'x Gastrolea', 'Guillauminia', 'Haworthia', 'Haworthiopsis', 'Kumara', 'Kumaria', 'Lemeea', 'Leptaloe', 'Pachidendron', 'Poellnitzia', 'Ptyas', 'Rhipidodendrum', 'Tulista']
asc = ['Angolluma', 'Anomalluma', 'Apoxyanthera', 'Apteranthes', 'Asclepias', 'Australluma', 'Baynesia', 'Boucerosia', 'Brachystelma', 'Caralluma', 'Caruncularia', 'Caudanthera', 'Centrostemma', 'Ceramanthus', 'Ceropegia', 'Chymocormus', 'Cibirhiza', 'Collyris', 'Crenulluma', 'Cryptolluma', 'Cynanchum', 'Cynoctonum', 'Cyrtoceras', 'Decabelone', 'Decanemopsis', 'Desmidorchis', 'Dichaelia', 'Diplocyatha', 'Diplocyathus', 'Diplolepis', 'Dischidia', 'Drakebrockmania', 'Duvalia', 'Duvaliandra', 'Echidnopsis', 'Edithcolea', 'Fockea', 'Frerea', 'Funastrum', 'Gongronema', 'Gonolobus', 'Gonostemon', 'Gymnema', 'Hermanschwartzia', 'Hoodia', 'x Hoodiapelia', 'Hoya', 'Huernia', 'Huerniopsis', 'Hutchinia', 'Ischnolepis', 'Larryleachia', 'Lasiostelma', 'Lavrania', 'Leachia', 'Leachiella', 'Leptostemma', 'Lithocaulon', 'Luckhoffia', 'Macropetalum', 'Mafekingia', 'Matelea', 'Micraster', 'Monolluma', 'Monothylaceum', 'Neopectinaria', 'Notechidnopsis', 'Obesia', 'Ophionella', 'Orbea', 'Orbeanthus', 'Orbeopsis', 'Otostemma', 'Pachycymbium', 'Pectinaria', 'Pentagonanthus', 'Pentopetia', 'Pergularia', 'Petopentia', 'Philibertella', 'Philibertia', 'Physostelma', 'Piaranthus', 'Plocostemma', 'Podanthes', 'Pseudolithos', 'Pseudopectinaria', 'Quaqua', 'Raphiacme', 'Raphionacme', 'Rhytidocaulon', 'Richtersveldia', 'Sanguilluma', 'Sarcocodon', 'Sarcophagophilus', 'Sarcostemma', 'Schizoglossum', 'Schlechterella', 'Schollia', 'Scytanthus', 'Socotrella', 'Spathulopetalum', 'Spiralluma', 'x Staparesia', 'Stapelia', 'Stapelianthus', 'Stapeliopsis', 'Stathmostelma', 'Stissera', 'Stisseria', 'Stultitia', 'Sulcolluma', 'Tacazzea', 'Tapeinostelma', 'Tavaresia', 'x Tavarorbea', 'x Tavastemon', 'Trichocaulon', 'Tridentea', 'Triodoglossum', 'Tromotriche', 'Vincetoxicum', 'Whitesloanea', 'Zaczatea', 'Zucchellia']
aiz = ['Abryanthemum', 'Acaulon', 'Acrodon', 'Aistocaulon', 'Aizoon', 'Aloinopsis', 'Amphibolia', 'Anisocalyx', 'Antegibbaeum', 'Antimima', 'Aptenia', 'Argeta', 'Argyroderma', 'Aridaria', 'Astridia', 'Bergeranthus', 'Bijlia', 'Bolusanthemum', 'Braunsia', 'Carpobrotus', 'Carruanthus', 'Cephalophyllum', 'Cerochlamys', 'Chasmatophyllum', 'Cheiridopsis', 'Conophyllum', 'Conophytum', 'Corpuscularia', 'Crocanthus', 'Cryophytum', 'Cylindrophyllum', 'Dactylopsis', 'Deilanthe', 'Delosperma', 'Depacarpus', 'Derenbergia', 'Dicrocaulon', 'Dinteranthus', 'Diplosoma', 'Dracophilus', 'Drosanthemopsis', 'Drosanthemum', 'Ebracteola', 'Echinus', 'Erepsia', 'Faucaria', 'Fenestraria', 'Frithia', 'Gasoul', 'Gibbaeum', 'Glottiphyllum', 'Halenbergia', 'Halimus', 'Hammeria', 'Hartmanthus', 'Henricia', 'Hereroa', 'Hymenocyclus', 'Ihlenfeldtia', 'Imitaria', 'Jacobsenia', 'Jensenobotrya', 'Juttadinteria', 'Lampranthus', 'Lapidaria', 'Lithops', 'Litocarpus', 'Ludolfia', 'Machairophyllum', 'Malephora', 'Marlothistella', 'Maughaniella', 'Mentocalyx', 'Mesembryanthemum', 'Mestoklema', 'Meyerophytum', 'Mimetophytum', 'Mitrophyllum', 'Monilaria', 'Mossia', 'Namibia', 'Nananthus', 'Neohenricia', 'Neorhine', 'Nycteranthus', 'Odontophorus', 'Ophthalmophyllum', 'Opophytum', 'Orthopterum', 'Oscularia', 'Peersia', 'Pentacoilanthus', 'Perapentacoilanthus', 'Phyllobolus', 'Platythyra', 'Pleiospilos', 'Prenia', 'Prepodesma', 'Psammanthe', 'Psammophora', 'Psilocaulon', 'Pteropentacoilanthus', 'Punctillaria', 'Pyxipoma', 'Rabiea', 'Rhinephyllum', 'Rhombophyllum', 'Rimaria', 'Roodia', 'Ruschia', 'Ruschianthus', 'Sceletium', 'Schonlandia', 'Schwantesia', 'Sesuvium', 'Smicrostigma', 'Sphalmanthus', 'Stigmatocarpum', 'Stomatium', 'Synaptophyllum', 'Tanquana', 'Tetracoilanthus', 'Tetragonia', 'Titanopsis', 'Trianthema', 'Trichodiadema', 'Vanheerdea', 'Verrucifera', 'Veslingia']
eup = ['Euphorbia']
cra = ['Adromischus', 'Aeonium', 'Aichryson', 'Aithales', 'Aldasorea', 'Asterosedum', 'Bryophyllum', 'Bulliarda', 'Byrnesia', 'Combesia', 'Cotyledon', 'Cotyliphyllum', 'Crassula', 'Crassuvia', 'Creusa', 'Curtogyne', 'Danielia', 'Dietrichia', 'Diopogon', 'Diotostemon', 'Disporocarpa', 'Dudleya', 'Echeveria', 'Geaya', 'Globulea', 'Gomara', 'Gormania', 'Graptopetalum', 'x Graptosedum', 'x Graptoveria', 'Greenovia', 'Hydrophila', 'Hylotelephium', 'Jovibarba', 'Kalanchoe', 'Kitchingia', 'Larochea', 'Lenophyllum', 'Leucosedum', 'Macrobia', 'Meristostylus', 'Mesanchum', 'Monanthes', 'Oreosedum', 'Orostachys', 'Pachyphytum', 'x Pachyveria', 'Petrogeton', 'Petrophyes', 'Petrosedum', 'Phedimus', 'Procrassula', 'Purgosea', 'Rhodiola', 'Rochea', 'Rosularia', 'x Sedeveria', 'Sedum', 'Sempervivum', 'Septas', 'Septimia', 'Sinocrassula', 'Spathulata', 'Sphaeritis', 'Stylophyllum', 'Tacitus', 'Tetraphyle', 'Thisantha', 'Thysantha', 'Tillaea', 'Tillaeastrum', 'Toelkenia', 'Tolmachevia', 'Turgosea', 'Tylecodon', 'Umbilicus', 'Urbinia', 'Verea', 'Vereia', 'Villadia']
hya = ['Adenotheca', 'Albuca', 'Basaltogeton', 'Bowiea', 'Caloscilla', 'Charybdis', 'Coilonox', 'Daubenya', 'Dipcadi', 'Drimia', 'Drimiopsis', 'Eliokarmos', 'Falconera', 'Fenelonia', 'Hyacinthus', 'Ledebouria', 'Loncomelos', 'Massonia', 'Melomphis', 'Nicipe', 'Oncostema', 'Ornithogalum', 'Podocallis', 'Polyxena', 'Resnova', 'Schizobasis', 'Schizobasopsis', 'Scilla', 'Stellarioides', 'Urginavia', 'Urginea', 'Urophyllon', 'Veltheimia']
por = ['Anacampseros', 'Avonia', 'Calandrinia', 'Ceraria', 'Cistanthe', 'Claytonia', 'Grahamia', 'Helianthemoides', 'Lewisia', 'Oreobroma', 'Phemeranthus', 'Portulaca', 'Portulacaria', 'Ruelingia', 'Talinum']
cac = ['Acanthanthus', 'Acanthocalycium', 'Acanthocephala', 'Acanthocereus', 'Acantholobivia', 'Acanthopetalus', 'Acanthorhipsalis', 'Acharagma', 'Airampoa', 'Akersia', 'Ancistrocactus', 'Andenea', 'Andinopuntia', 'Anhalonium', 'Anisocereus', 'Aparadoa', 'Aporocactus', 'x Aporoheliocereus', 'Arequipa', 'Arequipiopsis', 'Ariocarpus', 'Armatocereus', 'Arrojadoa', 'Arrojadoopsis', 'Arthrocereus', 'Arthrophyllum', 'Astrobergia', 'Astrophytum', 'Aulacothele', 'Austrocactus', 'Austrocephalocereus', 'Austrocylindropuntia', 'Aylostera', 'Aztekium', 'Azureocereus', 'Backebergia', 'Banfiopuntia', 'Bartschella', 'Bergerocactus', 'Bergerocereus', 'Binghamia', 'Bisnaga', 'Blossfeldia', 'Bolivicactus', 'Bolivicereus', 'Bonifazia', 'Borzicactella', 'Borzicactus', 'x Borzipostoa', 'Brachycalycium', 'Brachycereus', 'Bragaia', 'Brasilicactus', 'Brasilicereus', 'Brasiliopuntia', 'Brasiliparodia', 'Brasilocactus', 'Bravocactus', 'Bridgesia', 'Brittonia', 'Brittonrosea', 'Browningia', 'Buiningia', 'Cactodendron', 'Cactus', 'Calymmanthium', 'Carnegiea', 'Carpophillus', 'Cassyta', 'Cassytha', 'Castellanosia', 'Cephalocereus', 'Cephalocleistocactus', 'Cephalomamillaria', 'Cephalophorus', 'Ceratistes', 'Cereus', 'Chaffeyopuntia', 'Chamaecereus', 'x Chamaelobivia', 'Chiapasia', 'Chichipia', 'Chilenia', 'Chileniopsis', 'Chileocactus', 'Chileorebutia', 'Chilita', 'Chrysocactus', 'Cinnabarinea', 'Cintia', 'Cipocereus', 'Cirinosum', 'Clavarioidia', 'Clavatopuntia', 'Cleistocactus', 'Cleistocereus', 'Clistanthocereus', 'Cochemiea', 'Cochiseia', 'Coleocephalocereus', 'Coloradoa', 'Consolea', 'Copiapoa', 'Corryocactus', 'Corryocereus', 'Corynopuntia', 'Coryphantha', 'Cryptocereus', 'Cullmannia', 'Cumarinia', 'Cumulopuntia', 'Cylindrolobivia', 'Cylindropuntia', 'Cylindrorebutia', 'Dactylanthocactus', 'Deamia', 'Delaetia', 'Dendrocereus', 'Denmoza', 'Digitorebutia', 'Digitostigma', 'Diploperianthium', 'Discocactus', 'Disisocactus', 'Disisorhipsalis', 'Disocactus', 'Disocereus', 'Dolichothele', 'Ebnerella', 'Eccremocactus', 'Echinocactus', 'Echinocereus', 'x Echinoferocactus', 'Echinofossulocactus', 'Echinolobivia', 'Echinomastus', 'Echinonyctanthus', 'Echinopsis', 'Echinorebutia', 'Efossus', 'Emorycactus', 'Encephalocarpus', 'Eomatucana', 'x Epinicereus', 'Epiphyllanthus', 'Epiphyllopsis', 'Epiphyllum', 'Epithelantha', 'Erdisia', 'Eriocactus', 'Eriocephala', 'x Eriocereopsis', 'Eriocereus', 'Eriosyce', 'Erythrocereus', 'Erythrorhipsalis', 'Escobaria', 'Escobariopsis', 'Escobesseya', 'Escobrittonia', 'Escocoryphantha', 'Escontria', 'Espostoa', 'x Espostocactus', 'Espostoopsis', 'Estevesia', 'Eulychnia', 'Euporteria', 'Eurebutia', 'Facheiroa', 'x Ferenocactus', 'x Ferobergia', 'Ferocactus', 'x Ferofossulocactus', 'Floribunda', 'Fobea', 'Frailea', 'Friesia', 'Furiolobivia', 'Geohintonia', 'Gerocephalus', 'Glandulicactus', 'Glandulifera', 'Grusonia', 'Gymnantha', 'Gymnanthocereus', 'Gymnocactus', 'Gymnocalycium', 'Gymnocereus', 'Gymnorebutia', 'Haagea', 'Haageocereus', 'x Haagespostoa', 'Hamatocactus', 'Hariota', 'Harrisia', 'x Harrisinopsis', 'Haseltonia', 'Hatiora', 'Heliabravoa', 'Helianthocereus', 'x Heliaporus', 'Heliocereus', 'Hertrichocereus', 'Hickenia', 'Hildewintera', 'Hildmannia', 'Homalocephala', 'Horridocactus', 'Hylocereus', 'Hylorhipsalis', 'Hymenolobivia', 'Hymenorebutia', 'Islaya', 'Isolatocereus', 'Jasminocereus', 'Kadenicarpus', 'Krainzia', 'Lactomamillaria', 'Lagenosocereus', 'Lasiocereus', 'Lemaireocereus', 'Leocereus', 'Lepidocoryphantha', 'Lepismium', 'Leptocereus', 'Leptocladia', 'Leptocladodia', 'Leuchtenbergia', 'Leucostele', 'Leuenbergeria', 'Lobeira', 'Lobivia', 'Lobiviopsis', 'Lodia', 'Lophocereus', 'Lophophora', 'Loxanthocereus', 'Lymanbensonia', 'Machaerocereus', 'Maierocactus', 'Maihuenia', 'Maihueniopsis', 'Malacocarpus', 'Mamillopsis', 'Mammillaria', 'Mammilloydia', 'Marenopuntia', 'Marginatocereus', 'Maritinocereus', 'Marniera', 'Marshallocereus', 'Masarykia', 'Matucana', 'Mediocactus', 'Mediolobivia', 'Mediorebutia', 'Melocactus', 'Mesechinopsis', 'Meyenia', 'Meyerocactus', 'Micranthocereus', 'Micropuntia', 'Microspermia', 'Mila', 'Miqueliopuntia', 'Mirabella', 'Mitrocereus', 'Monvillea', 'Morangaya', 'Morawetzia', 'x Myrtgerocactus', 'Myrtillocactus', 'x Myrtillocalycium', 'Myrtillocereus', 'Napina', 'Navajoa', 'Neoabbottia', 'Neobesseya', 'x Neobinghamia', 'Neobuxbaumia', 'Neocardenasia', 'Neochilenia', 'Neodawsonia', 'Neodiscocactus', 'Neoevansia', 'Neogomesia', 'Neohickenia', 'Neolemaireocereus', 'Neolloydia', 'Neolobivia', 'Neomammillaria', 'Neomatucana', 'Neonavajoa', 'Neoporteria', 'Neoraimondia', 'Neotanahashia', 'Neowerdermannia', 'Nichelia', 'Nopalea', 'Nopalxochia', 'Normanbokea', 'Nothorhipsalis', 'Notocactus', 'Nyctocereus', 'Obregonia', 'Oehmea', 'Ophiorhipsalis', 'Opuntia', 'Opuntiopsis', 'Oreocereus', 'Oroya', 'Ortegocactus', 'x Ortegopuntia', 'x Pacherocactus', 'x Pachgerocereus', 'Pachycereus', 'Parodia', 'Parrycactus', 'Parviopuntia', 'Pediocactus', 'Pelecyphora', 'Peniocereus', 'Pereskia', 'Pereskiopsis', 'Peronocactus', 'Peruvocereus', 'Peyotl', 'Pfeiffera', 'Phellosperma', 'Philippicereus', 'Phyllarthus', 'Phyllocactus', 'Pierrebraunia', 'Pilocanthus', 'Pilocereus', 'Pilocopiapoa', 'Pilosocereus', 'Piptanthocereus', 'Platyopuntia', 'Polaskia', 'Porfiria', 'Praecereus', 'Pseudoacanthocereus', 'Pseudoechinopsis', 'Pseudoespostoa', 'Pseudolobivia', 'Pseudomaihueniopsis', 'Pseudomammillaria', 'Pseudomitrocereus', 'Pseudonopalxochia', 'Pseudopilocereus', 'Pseudorhipsalis', 'Pseudoselenicereus', 'Pseudosolisia', 'Pseudotephrocactus', 'Pseudozygocactus', 'Pterocactus', 'Pterocereus', 'Puebloa', 'Puna', 'Punotia', 'Pygmaeocereus', 'Pyrrhocactus', 'Quiabentia', 'Rapicactus', 'Rathbunia', 'Rauhocereus', 'Rebulobivia', 'Rebutia', 'Reicheocactus', 'Rhipsalidopsis', 'Rhipsalis', 'Rhipsaphyllopsis', 'Rhodocactus', 'Rimacactus', 'Ritterocactus', 'Ritterocereus', 'Rodentiophila', 'Rooksbya', 'Roseocactus', 'Roseocereus', 'Rowleyara', 'Salmonopuntia', 'Salpingolobivia', 'Samaipaticereus', 'Schlumbergera', 'Sclerocactus', 'Scoparebutia', 'Selenicereus', 'x Seleniphyllum', 'Sericocactus', 'Seticereus', 'Seticleistocactus', 'Setiechinopsis', 'Setirebutia', 'Siccobaccatus', 'Soehrensia', 'Solisia', 'Spegazzinia', 'Sphaeropuntia', 'Spinicalycium', 'Stenocactus', 'Stenocereus', 'x Stenogonia', 'Stephanocereus', 'Stetsonia', 'Strombocactus', 'Strophocactus', 'Submatucana', 'Subpilocereus', 'Sulcorebutia', 'Tacinga', 'Tephrocactus', 'x Thelobergia', 'Thelocactus', 'Thelocephala', 'Thelomastus', 'Thrixanthocereus', 'Torreycactus', 'Toumeya', 'Trichocereus', 'x Trichopsis', 'Tunas', 'Tunilla', 'Turbinicarpus', 'Uebelmannia', 'Ursopuntia', 'Utahia', 'Vatricania', 'Weberbauerocereus', 'Weberiopuntia', 'Weberocereus', 'Weingartia', 'Werckleocereus', 'Wigginsia', 'Wilcoxia', 'Wilmattea', 'Winteria', 'Winterocereus', 'Wittia', 'Wittiocactus', 'Yavia', 'Yungasocereus', 'Zehntnerella', 'Zygocactus', 'Zygocereus']


all = asp + asc + aiz + eup + cra + hya + por + cac
'''

begin="""<!DOCTYPE html>
<html>
	<head>
		<meta http-equiv="content-type"
content="text/html;charset=utf-8" />
		<title>
		CK: ZOIKS
		</title>
		<meta name="viewport" content="initial-scale=1, maximum-scale=1, user-scalable=0">
		
		<link rel="stylesheet" type="text/css" href="../depics/css/layoutNew.css">

		<link rel="stylesheet" type="text/css" href="depics/css/layoutNew.css">
		<link rel="icon" href='/favicon.png' type='image/png' />
	</head>

	<body>
		<div class="outer">
		<div class="middle">
		<div id="container">

			<div id="contentSingleTop">
				<img src="../depics/images/FINDMEHAHA.jpg" 
				class="croppedImage">
				<h2 class="repoDescriptionHeader">ZOIKS<br>For Sale</h2>
			
			</div><!--Close Package Header Div-->
			<div id="contentSingle">
				<h3 class="textHeaderLabel">Order Information</h3>
			</div>
			<div id="contentBottom">
				<ul>
					<li>
						<p>For the time being U.S. orders only...
								<br>
								<br>
							BISNITCH 
						</p>
					</li> 
				</ul> 
			</div>
"""

fambegin='''<div id="contentSingle">
						     <h3 class="textHeaderLabel">'''
titleend='''</h3>
					 </div>
					 <div id="contentBottom">
					 	<ul>'''
famend='''</ul>
					</div>'''
end='''</ul>
					</div>
					</li>
				</ul>			
			</div><!--Close Package Header Div-->

		</div><!--Close Container Div-->
		</div>
		</div>
	</body>
	
</html>'''

info={'seeds':'The shipping is $2 for up to 6 packs of seeds. $0.50 for each additional 4 packs. Seed amount per pack differs according to familial rank and is displayed to the right of each botanical family. If seeds are the product of unknown hybridization the mother plant will be displayed.','plants':'The minimum shipping costs for any plant ordrs is $8. The plant for sale is in the picture displayed'}

def addtosite(dicform):
	formy=dicform['form']
	for line in (os.listdir(dirx + 'pics/' + formy)):
		if line != '.DS_Store':
			dicform[line[:3]].append(line)
	occup=[]
	for key in dicform:
		if key != 'form':
			if len(dicform[key]) > 1:
				occup.append(key)
				occup.sort()
	html=open((dirx + formy + '.html'), 'w+')
	linkfix='pics/' + formy + '/'
	html.write(begin.replace('ZOIKS', formy.capitalize()).replace('FINDMEHAHA', formy).replace('BISNITCH',info[formy]))
	for key in occup:
		html.write( fambegin + dicform[key][0] + titleend)
		x = decy(dicform[key][1])
		html.write('<a href="' + (linkfix + x[4].replace('"', '&#34;')) + '">' + (x[1] + ' ' + x[2]) + '</a> ' + x[3])
		for index in dicform[key]:
			if dicform[key].index(index) > 1:
				x = decy(index)
				html.write('<hr>\n<a href="' + (linkfix + x[4].replace('"', '&#34;')) + '">' + (x[1] + ' ' + x[2]) + '</a> ' + x[3])
		html.write(famend)
	html.write(end)
	html.close()



def decy(filename):
	splitname=filename.replace('.JPG', '').split('!')
	splitname[1] = splitname[1][:1].upper() + splitname[1][1:]
	splitname[3] = '$' + splitname[3]
	splitname.append(filename)
	return splitname

def orgpics(form):
	for line in (os.listdir(dirx + 'pics/' + form['form'])):
		if line != '.DS_Store':
			form[line[:3]].append(line)

dirx=os.environ['HOME'] +'/git/carltons-karoo/'
seeds={'form':'seeds','asp':['Asphodelaceae | 10 seeds'],'asc':['Asclepiadaceae | 10 seeds'],'aiz':['Aizoaceae | 25 seeds'],'eup':['Euphorbiaceae | 5 seeds'],'cra':['Crassulaceae | 10 seeds'],'hya':['Hyacinthaceae 10 seeds'],'por':['Portulacaceae | 10 seeds'],'cac':['Cactaceae | 10 seeds']}
plants={'form':'plants','asp':['Asphodelaceae'],'asc':['Asclepiadaceae'],'aiz':['Aizoaceae'],'eup':['Euphorbiaceae'],'cra':['Crassulaceae'],'hya':['Hyacinthaceae'],'por':['Portulacaceae'],'cac':['Cactaceae']}
orgpics(seeds)
orgpics(plants)
addtosite(seeds)
addtosite(plants)
os.system('cd ' + os.environ['HOME'] + '/git && ./updategit.sh')













#	naming format = gen [species] price .JPG

#		eua!baioensis!12.JPG
#		decy(

'''

def decy(filename):
	splitname=filename.replace('.JPG', '').split('!')
	for key in plantindex[splitname[0]]:
			if splitname[1] in key:
				splitname[0] = plantindex[splitname[0]].get(splitname[1])
	return splitname

def devowel(word):
	x = word.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '')
	return x





def abrgen(fam):
	new = {}
	for line in fam:
		x = devowel(line.lower().replace(' ', ''))
		x = x[:2] + x[-1:]
		if x not in new:
			new[x]=line
		else:
			print(line)

'''
