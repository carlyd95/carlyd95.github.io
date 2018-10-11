#! /usr/bin/env python 

import os

'''
Aizocaceae = {'lit':'lithops'}
Asphodelaceae = ['aloe', 'astroloba', 'gasteria', 'haworthia', 'haworthiopsia', 'tulista']
Cactaceae = ['ariocarpus', 'astrophytum', 'frailea', 'gymnocalycium', 'lophophora', 'melocactus']
Euphorbiaceae = ['euphorbia']
Hyacinthaceae = ['schizobasis', 'boweia']
Asclepiadaceae = ['huernia', 'stapelia', 'orbea', 'duvalia', 'rhytidocaulon', 'trichocaulon']
Portulacaceae = ['Avonia', 'Crassula']

family = {'a':Aizocaceae, 'b':Asphodelaceae, 'c':Cactaceae, 'd':Euphorbiaceae, 'e':Hyacinthaceae, 'f':Asclepiadaceae, 'g':Portulacaceae}
'''

def famgen(family):
	f = open('/Users/carlyd95/Downloads/cactus.txt')
	longlist = []
	shortlist = []
	for line in f:
		longlist.append(line.replace('+', 'x').replace('\tx ', '\tx%').replace('undefined\t', '').split(' ')[0].replace('%',' '))
	for line in longlist:
		shortlist.append(line.replace(' ','').lower()[:5])
	if len(longlist) != len(shortlist):
		print "!! ERROR SHORT LIST AND LONG LIST DO NOT HAVE EQUAL ENTRIES !!"
	else:
		print family + ' = '
		print longlist
		print family.lower()[:5] + ' = '
		print shortlist


cactaceae = ['Echinopsis', 'Acanthocalycium', 'Parodia', 'Acanthocereus', 'Lepismium', 'Acharagma', 'Tunilla', 'Cleistocactus', 'Sclerocactus', 'Andinopuntia', 'Ariocarpus', 'Pachycereus', 'Disocactus', 'x Aporoheliocereus', 'Oreocereus', 'Armatocereus', 'Arrojadoa', 'Arrojadoopsis', 'Arthrocereus', 'Epiphyllum', 'Astrobergia', 'Astrophytum', 'Coryphantha', 'Austrocactus', 'Micranthocereus', 'Austrocylindropuntia', 'Rebutia', 'Aztekium', 'Browningia', 'Banfiopuntia', 'Mammillaria', 'Bergerocactus', 'Espostoa', 'Ferocactus', 'Blossfeldia', 'x Borzipostoa', 'Gymnocalycium', 'Brachycereus', 'Bragaia', 'Brasilicereus', 'Brasiliopuntia', 'Turbinicarpus', 'Bridgesia', 'Brittonia', 'Stenocactus', 'Coleocephalocereus', 'Opuntia', 'Cactus', 'Calymmanthium', 'Carnegiea', 'Pereskia', 'Cassyta', 'Cassytha', 'Cephalocereus', 'Cephalocleistocactus', 'Epithelantha', 'Eriosyce', 'Cereus', 'Polaskia', 'Cintia', 'Cipocereus', 'Maihueniopsis', 'Escobaria', 'Consolea', 'Copiapoa', 'Corryocactus', 'Grusonia', 'Selenicereus', 'Peniocereus', 'Cumulopuntia', 'Cylindropuntia', 'Dendrocereus', 'Denmoza', 'Discocactus', 'Weberocereus', 'Echinocactus', 'Echinocereus', 'x Echinoferocactus', 'Echinomastus', 'Echinonyctanthus', 'Encephalocarpus', 'Matucana', 'x Epinicereus', 'Schlumbergera', 'Hatiora', 'x Eriocereopsis', 'Harrisia', 'Rhipsalis', 'Escontria', 'x Espostocactus', 'Espostoopsis', 'Estevesia', 'Eulychnia', 'Euporteria', 'Facheiroa', 'x Ferenocactus', 'x Ferobergia', 'x Doweld', 'Frailea', 'Geohintonia', 'Gymnantha', 'Haageocereus', 'x Haagespostoa', 'Thelocactus', 'x Harrisinopsis', 'x Heliaporus', 'Stenocereus', 'Hylocereus', 'Hymenolobivia', 'Isolatocereus', 'Jasminocereus', 'Stephanocereus', 'Lasiocereus', 'Leocereus', 'Leptocereus', 'Leuchtenbergia', 'Leuenbergeria', 'Lophophora', 'Loxanthocereus', 'Maihuenia', 'Mammilloydia', 'Melocactus', 'Mila', 'Miqueliopuntia', 'Monvillea', 'Morangaya', 'x Myrtgerocactus', 'Myrtillocactus', 'x Myrtillocalycium', 'Neolloydia', 'Pediocactus', 'Neobuxbaumia', 'Neoraimondia', 'Neolemaireocereus', 'Echidnopsis', 'Neomatucana', 'Neotanahashia', 'Neowerdermannia', 'Nichelia', 'Nyctocereus', 'Obregonia', 'Oroya', 'Ortegocactus', 'x Ortegopuntia', 'x Pacherocactus', 'x Pachgerocereus', 'Pelecyphora', 'Pereskiopsis', 'Pfeiffera', 'Pierrebraunia', 'Pilosocereus', 'Praecereus', 'Pseudoacanthocereus', 'Pseudoechinopsis', 'Pseudomaihueniopsis', 'Pseudorhipsalis', 'Pterocactus', 'Punotia', 'Pygmaeocereus', 'Quiabentia', 'Rauhocereus', 'Rhipsaphyllopsis', 'Rowleyara', 'Obesia', 'Samaipaticereus', 'x Seleniphyllum', 'Sphaeropuntia', 'x Stenogonia', 'Stetsonia', 'Strombocactus', 'Tacinga', 'Tephrocactus', 'x Thelobergia', 'Toumeya', 'x Trichopsis', 'Tunas', 'Uebelmannia', 'Weberbauerocereus', 'Yavia', 'Yungasocereus']
cacta = ['echin', 'acant', 'parod', 'acant', 'lepis', 'achar', 'tunil', 'cleis', 'scler', 'andin', 'arioc', 'pachy', 'disoc', 'xapor', 'oreoc', 'armat', 'arroj', 'arroj', 'arthr', 'epiph', 'astro', 'astro', 'coryp', 'austr', 'micra', 'austr', 'rebut', 'aztek', 'brown', 'banfi', 'mammi', 'berge', 'espos', 'feroc', 'bloss', 'xborz', 'gymno', 'brach', 'braga', 'brasi', 'brasi', 'turbi', 'bridg', 'britt', 'steno', 'coleo', 'opunt', 'cactu', 'calym', 'carne', 'peres', 'cassy', 'cassy', 'cepha', 'cepha', 'epith', 'erios', 'cereu', 'polas', 'cinti', 'cipoc', 'maihu', 'escob', 'conso', 'copia', 'corry', 'gruso', 'selen', 'penio', 'cumul', 'cylin', 'dendr', 'denmo', 'disco', 'weber', 'echin', 'echin', 'xechi', 'echin', 'echin', 'encep', 'matuc', 'xepin', 'schlu', 'hatio', 'xerio', 'harri', 'rhips', 'escon', 'xespo', 'espos', 'estev', 'eulyc', 'eupor', 'fache', 'xfere', 'xfero', 'xdowe', 'frail', 'geohi', 'gymna', 'haage', 'xhaag', 'thelo', 'xharr', 'xheli', 'steno', 'hyloc', 'hymen', 'isola', 'jasmi', 'steph', 'lasio', 'leoce', 'lepto', 'leuch', 'leuen', 'lopho', 'loxan', 'maihu', 'mammi', 'meloc', 'mila', 'mique', 'monvi', 'moran', 'xmyrt', 'myrti', 'xmyrt', 'neoll', 'pedio', 'neobu', 'neora', 'neole', 'echid', 'neoma', 'neota', 'neowe', 'niche', 'nycto', 'obreg', 'oroya', 'orteg', 'xorte', 'xpach', 'xpach', 'pelec', 'peres', 'pfeif', 'pierr', 'pilos', 'praec', 'pseud', 'pseud', 'pseud', 'pseud', 'ptero', 'punot', 'pygma', 'quiab', 'rauho', 'rhips', 'rowle', 'obesi', 'samai', 'xsele', 'sphae', 'xsten', 'stets', 'strom', 'tacin', 'tephr', 'xthel', 'toume', 'xtric', 'tunas', 'uebel', 'weber', 'yavia', 'yunga']

asphodelaceae = ['Aloe', 'Aloiampelos', 'Aloidendron', 'Aloinella', 'x Alworthia', 'Apicra', 'Aristaloe', 'Astroloba', 'x Astroworthia', 'Busipho', 'Catevala', 'x Gasteraloe', 'x Gasterhaworthia', 'Gasteria', 'x Gastrolea', 'Guillauminia', 'Haworthia', 'Haworthiopsis', 'Kumara', 'Kumaria', 'Lemeea', 'Leptaloe', 'Pachidendron', 'Poellnitzia', 'Ptyas', 'Rhipidodendrum', 'Tulista']
aspho = ['aloe', 'aloia', 'aloid', 'aloin', 'xalwo', 'apicr', 'arist', 'astro', 'xastr', 'busip', 'catev', 'xgast', 'xgast', 'gaste', 'xgast', 'guill', 'hawor', 'hawor', 'kumar', 'kumar', 'lemee', 'lepta', 'pachi', 'poell', 'ptyas', 'rhipi', 'tulis']

asclepiadaceae = ['Angolluma', 'Anomalluma', 'Apoxyanthera', 'Apteranthes', 'Asclepias', 'Australluma', 'Baynesia', 'Boucerosia', 'Brachystelma', 'Caralluma', 'Caruncularia', 'Caudanthera', 'Centrostemma', 'Ceramanthus', 'Ceropegia', 'Chymocormus', 'Cibirhiza', 'Collyris', 'Crenulluma', 'Cryptolluma', 'Cynanchum', 'Cynoctonum', 'Cyrtoceras', 'Decabelone', 'Decanemopsis', 'Desmidorchis', 'Dichaelia', 'Diplocyatha', 'Diplocyathus', 'Diplolepis', 'Dischidia', 'Drakebrockmania', 'Duvalia', 'Duvaliandra', 'Echidnopsis', 'Edithcolea', 'Fockea', 'Frerea', 'Funastrum', 'Gongronema', 'Gonolobus', 'Gonostemon', 'Gymnema', 'Hermanschwartzia', 'Hoodia', 'x Hoodiapelia', 'Hoya', 'Huernia', 'Huerniopsis', 'Hutchinia', 'Ischnolepis', 'Larryleachia', 'Lasiostelma', 'Lavrania', 'Leachia', 'Leachiella', 'Leptostemma', 'Lithocaulon', 'Luckhoffia', 'Macropetalum', 'Mafekingia', 'Matelea', 'Micraster', 'Monolluma', 'Monothylaceum', 'Neopectinaria', 'Notechidnopsis', 'Obesia', 'Ophionella', 'Orbea', 'Orbeanthus', 'Orbeopsis', 'Otostemma', 'Pachycymbium', 'Pectinaria', 'Pentagonanthus', 'Pentopetia', 'Pergularia', 'Petopentia', 'Philibertella', 'Philibertia', 'Physostelma', 'Piaranthus', 'Plocostemma', 'Podanthes', 'Pseudolithos', 'Pseudopectinaria', 'Quaqua', 'Raphiacme', 'Raphionacme', 'Rhytidocaulon', 'Richtersveldia', 'Sanguilluma', 'Sarcocodon', 'Sarcophagophilus', 'Sarcostemma', 'Schizoglossum', 'Schlechterella', 'Schollia', 'Scytanthus', 'Socotrella', 'Spathulopetalum', 'Spiralluma', 'x Staparesia', 'Stapelia', 'Stapelianthus', 'Stapeliopsis', 'Stathmostelma', 'Stissera', 'Stisseria', 'Stultitia', 'Sulcolluma', 'Tacazzea', 'Tapeinostelma', 'Tavaresia', 'x Tavarorbea', 'x Tavastemon', 'Trichocaulon', 'Tridentea', 'Triodoglossum', 'Tromotriche', 'Vincetoxicum', 'Whitesloanea', 'Zaczatea', 'Zucchellia']
ascle = ['angol', 'anoma', 'apoxy', 'apter', 'ascle', 'austr', 'bayne', 'bouce', 'brach', 'caral', 'carun', 'cauda', 'centr', 'ceram', 'cerop', 'chymo', 'cibir', 'colly', 'crenu', 'crypt', 'cynan', 'cynoc', 'cyrto', 'decab', 'decan', 'desmi', 'dicha', 'diplo', 'diplo', 'diplo', 'disch', 'drake', 'duval', 'duval', 'echid', 'edith', 'focke', 'frere', 'funas', 'gongr', 'gonol', 'gonos', 'gymne', 'herma', 'hoodi', 'xhood', 'hoya', 'huern', 'huern', 'hutch', 'ischn', 'larry', 'lasio', 'lavra', 'leach', 'leach', 'lepto', 'litho', 'luckh', 'macro', 'mafek', 'matel', 'micra', 'monol', 'monot', 'neope', 'notec', 'obesi', 'ophio', 'orbea', 'orbea', 'orbeo', 'otost', 'pachy', 'pecti', 'penta', 'pento', 'pergu', 'petop', 'phili', 'phili', 'physo', 'piara', 'ploco', 'podan', 'pseud', 'pseud', 'quaqu', 'raphi', 'raphi', 'rhyti', 'richt', 'sangu', 'sarco', 'sarco', 'sarco', 'schiz', 'schle', 'schol', 'scyta', 'socot', 'spath', 'spira', 'xstap', 'stape', 'stape', 'stape', 'stath', 'stiss', 'stiss', 'stult', 'sulco', 'tacaz', 'tapei', 'tavar', 'xtava', 'xtava', 'trich', 'tride', 'triod', 'tromo', 'vince', 'white', 'zacza', 'zucch']

euphorbiaceae = ['Euphorbia']
eupho = ['eupho']

aizoaceae = ['Abryanthemum', 'Acaulon', 'Acrodon', 'Aistocaulon', 'Aizoon', 'Aloinopsis', 'Amphibolia', 'Anisocalyx', 'Antegibbaeum', 'Antimima', 'Aptenia', 'Argeta', 'Argyroderma', 'Aridaria', 'Astridia', 'Bergeranthus', 'Bijlia', 'Bolusanthemum', 'Braunsia', 'Carpobrotus', 'Carruanthus', 'Cephalophyllum', 'Cerochlamys', 'Chasmatophyllum', 'Cheiridopsis', 'Conophyllum', 'Conophytum', 'Corpuscularia', 'Crocanthus', 'Cryophytum', 'Cylindrophyllum', 'Dactylopsis', 'Deilanthe', 'Delosperma', 'Depacarpus', 'Derenbergia', 'Dicrocaulon', 'Dinteranthus', 'Diplosoma', 'Dracophilus', 'Drosanthemopsis', 'Drosanthemum', 'Ebracteola', 'Echinus', 'Erepsia', 'Faucaria', 'Fenestraria', 'Frithia', 'Gasoul', 'Gibbaeum', 'Glottiphyllum', 'Halenbergia', 'Halimus', 'Hammeria', 'Hartmanthus', 'Henricia', 'Hereroa', 'Hymenocyclus', 'Ihlenfeldtia', 'Imitaria', 'Jacobsenia', 'Jensenobotrya', 'Juttadinteria', 'Lampranthus', 'Lapidaria', 'Lithops', 'Litocarpus', 'Ludolfia', 'Machairophyllum', 'Malephora', 'Marlothistella', 'Maughaniella', 'Mentocalyx', 'Mesembryanthemum', 'Mestoklema', 'Meyerophytum', 'Mimetophytum', 'Mitrophyllum', 'Monilaria', 'Mossia', 'Namibia', 'Nananthus', 'Neohenricia', 'Neorhine', 'Nycteranthus', 'Odontophorus', 'Ophthalmophyllum', 'Opophytum', 'Orthopterum', 'Oscularia', 'Peersia', 'Pentacoilanthus', 'Perapentacoilanthus', 'Phyllobolus', 'Platythyra', 'Pleiospilos', 'Prenia', 'Prepodesma', 'Psammanthe', 'Psammophora', 'Psilocaulon', 'Pteropentacoilanthus', 'Punctillaria', 'Pyxipoma', 'Rabiea', 'Rhinephyllum', 'Rhombophyllum', 'Rimaria', 'Roodia', 'Ruschia', 'Ruschianthus', 'Sceletium', 'Schonlandia', 'Schwantesia', 'Sesuvium', 'Smicrostigma', 'Sphalmanthus', 'Stigmatocarpum', 'Stomatium', 'Synaptophyllum', 'Tanquana', 'Tetracoilanthus', 'Tetragonia', 'Titanopsis', 'Trianthema', 'Trichodiadema', 'Vanheerdea', 'Verrucifera', 'Veslingia']
aizoa = ['abrya', 'acaul', 'acrod', 'aisto', 'aizoo', 'aloin', 'amphi', 'aniso', 'anteg', 'antim', 'apten', 'arget', 'argyr', 'arida', 'astri', 'berge', 'bijli', 'bolus', 'braun', 'carpo', 'carru', 'cepha', 'ceroc', 'chasm', 'cheir', 'conop', 'conop', 'corpu', 'croca', 'cryop', 'cylin', 'dacty', 'deila', 'delos', 'depac', 'deren', 'dicro', 'dinte', 'diplo', 'draco', 'drosa', 'drosa', 'ebrac', 'echin', 'ereps', 'fauca', 'fenes', 'frith', 'gasou', 'gibba', 'glott', 'halen', 'halim', 'hamme', 'hartm', 'henri', 'herer', 'hymen', 'ihlen', 'imita', 'jacob', 'jense', 'jutta', 'lampr', 'lapid', 'litho', 'litoc', 'ludol', 'macha', 'malep', 'marlo', 'maugh', 'mento', 'mesem', 'mesto', 'meyer', 'mimet', 'mitro', 'monil', 'mossi', 'namib', 'nanan', 'neohe', 'neorh', 'nycte', 'odont', 'ophth', 'opoph', 'ortho', 'oscul', 'peers', 'penta', 'perap', 'phyll', 'platy', 'pleio', 'preni', 'prepo', 'psamm', 'psamm', 'psilo', 'ptero', 'punct', 'pyxip', 'rabie', 'rhine', 'rhomb', 'rimar', 'roodi', 'rusch', 'rusch', 'scele', 'schon', 'schwa', 'sesuv', 'smicr', 'sphal', 'stigm', 'stoma', 'synap', 'tanqu', 'tetra', 'tetra', 'titan', 'trian', 'trich', 'vanhe', 'verru', 'vesli']

crassulaceae = ['Adromischus', 'Aeonium', 'Aichryson', 'Aithales', 'Aldasorea', 'Asterosedum', 'Bryophyllum', 'Bulliarda', 'Byrnesia', 'Combesia', 'Cotyledon', 'Cotyliphyllum', 'Crassula', 'Crassuvia', 'Creusa', 'Curtogyne', 'Danielia', 'Dietrichia', 'Diopogon', 'Diotostemon', 'Disporocarpa', 'Dudleya', 'Echeveria', 'Geaya', 'Globulea', 'Gomara', 'Gormania', 'Graptopetalum', 'x Graptosedum', 'x Graptoveria', 'Greenovia', 'Hydrophila', 'Hylotelephium', 'Jovibarba', 'Kalanchoe', 'Kitchingia', 'Larochea', 'Lenophyllum', 'Leucosedum', 'Macrobia', 'Meristostylus', 'Mesanchum', 'Monanthes', 'Oreosedum', 'Orostachys', 'Pachyphytum', 'x Pachyveria', 'Petrogeton', 'Petrophyes', 'Petrosedum', 'Phedimus', 'Procrassula', 'Purgosea', 'Rhodiola', 'Rochea', 'Rosularia', 'x Sedeveria', 'Sedum', 'Sempervivum', 'Septas', 'Septimia', 'Sinocrassula', 'Spathulata', 'Sphaeritis', 'Stylophyllum', 'Tacitus', 'Tetraphyle', 'Thisantha', 'Thysantha', 'Tillaea', 'Tillaeastrum', 'Toelkenia', 'Tolmachevia', 'Turgosea', 'Tylecodon', 'Umbilicus', 'Urbinia', 'Verea', 'Vereia', 'Villadia']
crass = ['adrom', 'aeoni', 'aichr', 'aitha', 'aldas', 'aster', 'bryop', 'bulli', 'byrne', 'combe', 'cotyl', 'cotyl', 'crass', 'crass', 'creus', 'curto', 'danie', 'dietr', 'diopo', 'dioto', 'dispo', 'dudle', 'echev', 'geaya', 'globu', 'gomar', 'gorma', 'grapt', 'xgrap', 'xgrap', 'green', 'hydro', 'hylot', 'jovib', 'kalan', 'kitch', 'laroc', 'lenop', 'leuco', 'macro', 'meris', 'mesan', 'monan', 'oreos', 'orost', 'pachy', 'xpach', 'petro', 'petro', 'petro', 'phedi', 'procr', 'purgo', 'rhodi', 'roche', 'rosul', 'xsede', 'sedum', 'sempe', 'septa', 'septi', 'sinoc', 'spath', 'sphae', 'stylo', 'tacit', 'tetra', 'thisa', 'thysa', 'tilla', 'tilla', 'toelk', 'tolma', 'turgo', 'tylec', 'umbil', 'urbin', 'verea', 'verei', 'villa']

hyacinthaceae = ['Adenotheca', 'Albuca', 'Basaltogeton', 'Bowiea', 'Caloscilla', 'Charybdis', 'Coilonox', 'Daubenya', 'Dipcadi', 'Drimia', 'Drimiopsis', 'Eliokarmos', 'Falconera', 'Fenelonia', 'Hyacinthus', 'Ledebouria', 'Loncomelos', 'Massonia', 'Melomphis', 'Nicipe', 'Oncostema', 'Ornithogalum', 'Podocallis', 'Polyxena', 'Resnova', 'Schizobasis', 'Schizobasopsis', 'Scilla', 'Stellarioides', 'Urginavia', 'Urginea', 'Urophyllon', 'Veltheimia']
hyaci = ['adeno', 'albuc', 'basal', 'bowie', 'calos', 'chary', 'coilo', 'daube', 'dipca', 'drimi', 'drimi', 'eliok', 'falco', 'fenel', 'hyaci', 'ledeb', 'lonco', 'masso', 'melom', 'nicip', 'oncos', 'ornit', 'podoc', 'polyx', 'resno', 'schiz', 'schiz', 'scill', 'stell', 'urgin', 'urgin', 'uroph', 'velth']

portulacaceae = ['Anacampseros', 'Avonia', 'Calandrinia', 'Ceraria', 'Cistanthe', 'Claytonia', 'Grahamia', 'Helianthemoides', 'Lewisia', 'Oreobroma', 'Phemeranthus', 'Portulaca', 'Portulacaria', 'Ruelingia', 'Talinum']
portu = ['anaca', 'avoni', 'calan', 'cerar', 'cista', 'clayt', 'graha', 'helia', 'lewis', 'oreob', 'pheme', 'portu', 'portu', 'rueli', 'talin']


'''
'''


for line in (os.listdir( os.environ['HOME'] + "/git/carltons-karoo/pics/seeds")):
	if line.endswith(('.jpg')):
		print line.replace('.', '	').replace('jpg', 'jpg')







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

