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

#func for changing llifle family list copied to lists and abbr. list
def famgen(family):
	f = open('/Users/carlyd95/Downloads/cactus.txt')
	longlist = []
	shortlist = []
	for line in f:
		longlist.append(line.replace('+', 'x').replace('\tx ', '\tx%').replace('undefined\t', '').split(' ')[0].replace('%',' '))
	caclonglist:
		shortlist.append(line.replace(' ','').lower()[:2] + line[-1:])
	if len(longlist) != len(shortlist):
		print "!! ERROR SHORT LIST AND LONG LIST DO NOT HAVE EQUAL ENTRIES !!"
	else:
		print family + ' = '
		print longlist
		print family.lower()[:5] + ' = '
		print shortlist


#Families based on llifle (gen. abbr. = first 2 char. + last char.)
asp = ['Aloe', 'Aloiampelos', 'Aloidendron', 'Aloinella', 'x Alworthia', 'Apicra', 'Aristaloe', 'Astroloba', 'x Astroworthia', 'Busipho', 'Catevala', 'x Gasteraloe', 'x Gasterhaworthia', 'Gasteria', 'x Gastrolea', 'Guillauminia', 'Haworthia', 'Haworthiopsis', 'Kumara', 'Kumaria', 'Lemeea', 'Leptaloe', 'Pachidendron', 'Poellnitzia', 'Ptyas', 'Rhipidodendrum', 'Tulista']
asc = ['Angolluma', 'Anomalluma', 'Apoxyanthera', 'Apteranthes', 'Asclepias', 'Australluma', 'Baynesia', 'Boucerosia', 'Brachystelma', 'Caralluma', 'Caruncularia', 'Caudanthera', 'Centrostemma', 'Ceramanthus', 'Ceropegia', 'Chymocormus', 'Cibirhiza', 'Collyris', 'Crenulluma', 'Cryptolluma', 'Cynanchum', 'Cynoctonum', 'Cyrtoceras', 'Decabelone', 'Decanemopsis', 'Desmidorchis', 'Dichaelia', 'Diplocyatha', 'Diplocyathus', 'Diplolepis', 'Dischidia', 'Drakebrockmania', 'Duvalia', 'Duvaliandra', 'Echidnopsis', 'Edithcolea', 'Fockea', 'Frerea', 'Funastrum', 'Gongronema', 'Gonolobus', 'Gonostemon', 'Gymnema', 'Hermanschwartzia', 'Hoodia', 'x Hoodiapelia', 'Hoya', 'Huernia', 'Huerniopsis', 'Hutchinia', 'Ischnolepis', 'Larryleachia', 'Lasiostelma', 'Lavrania', 'Leachia', 'Leachiella', 'Leptostemma', 'Lithocaulon', 'Luckhoffia', 'Macropetalum', 'Mafekingia', 'Matelea', 'Micraster', 'Monolluma', 'Monothylaceum', 'Neopectinaria', 'Notechidnopsis', 'Obesia', 'Ophionella', 'Orbea', 'Orbeanthus', 'Orbeopsis', 'Otostemma', 'Pachycymbium', 'Pectinaria', 'Pentagonanthus', 'Pentopetia', 'Pergularia', 'Petopentia', 'Philibertella', 'Philibertia', 'Physostelma', 'Piaranthus', 'Plocostemma', 'Podanthes', 'Pseudolithos', 'Pseudopectinaria', 'Quaqua', 'Raphiacme', 'Raphionacme', 'Rhytidocaulon', 'Richtersveldia', 'Sanguilluma', 'Sarcocodon', 'Sarcophagophilus', 'Sarcostemma', 'Schizoglossum', 'Schlechterella', 'Schollia', 'Scytanthus', 'Socotrella', 'Spathulopetalum', 'Spiralluma', 'x Staparesia', 'Stapelia', 'Stapelianthus', 'Stapeliopsis', 'Stathmostelma', 'Stissera', 'Stisseria', 'Stultitia', 'Sulcolluma', 'Tacazzea', 'Tapeinostelma', 'Tavaresia', 'x Tavarorbea', 'x Tavastemon', 'Trichocaulon', 'Tridentea', 'Triodoglossum', 'Tromotriche', 'Vincetoxicum', 'Whitesloanea', 'Zaczatea', 'Zucchellia']
aiz = ['Abryanthemum', 'Acaulon', 'Acrodon', 'Aistocaulon', 'Aizoon', 'Aloinopsis', 'Amphibolia', 'Anisocalyx', 'Antegibbaeum', 'Antimima', 'Aptenia', 'Argeta', 'Argyroderma', 'Aridaria', 'Astridia', 'Bergeranthus', 'Bijlia', 'Bolusanthemum', 'Braunsia', 'Carpobrotus', 'Carruanthus', 'Cephalophyllum', 'Cerochlamys', 'Chasmatophyllum', 'Cheiridopsis', 'Conophyllum', 'Conophytum', 'Corpuscularia', 'Crocanthus', 'Cryophytum', 'Cylindrophyllum', 'Dactylopsis', 'Deilanthe', 'Delosperma', 'Depacarpus', 'Derenbergia', 'Dicrocaulon', 'Dinteranthus', 'Diplosoma', 'Dracophilus', 'Drosanthemopsis', 'Drosanthemum', 'Ebracteola', 'Echinus', 'Erepsia', 'Faucaria', 'Fenestraria', 'Frithia', 'Gasoul', 'Gibbaeum', 'Glottiphyllum', 'Halenbergia', 'Halimus', 'Hammeria', 'Hartmanthus', 'Henricia', 'Hereroa', 'Hymenocyclus', 'Ihlenfeldtia', 'Imitaria', 'Jacobsenia', 'Jensenobotrya', 'Juttadinteria', 'Lampranthus', 'Lapidaria', 'Lithops', 'Litocarpus', 'Ludolfia', 'Machairophyllum', 'Malephora', 'Marlothistella', 'Maughaniella', 'Mentocalyx', 'Mesembryanthemum', 'Mestoklema', 'Meyerophytum', 'Mimetophytum', 'Mitrophyllum', 'Monilaria', 'Mossia', 'Namibia', 'Nananthus', 'Neohenricia', 'Neorhine', 'Nycteranthus', 'Odontophorus', 'Ophthalmophyllum', 'Opophytum', 'Orthopterum', 'Oscularia', 'Peersia', 'Pentacoilanthus', 'Perapentacoilanthus', 'Phyllobolus', 'Platythyra', 'Pleiospilos', 'Prenia', 'Prepodesma', 'Psammanthe', 'Psammophora', 'Psilocaulon', 'Pteropentacoilanthus', 'Punctillaria', 'Pyxipoma', 'Rabiea', 'Rhinephyllum', 'Rhombophyllum', 'Rimaria', 'Roodia', 'Ruschia', 'Ruschianthus', 'Sceletium', 'Schonlandia', 'Schwantesia', 'Sesuvium', 'Smicrostigma', 'Sphalmanthus', 'Stigmatocarpum', 'Stomatium', 'Synaptophyllum', 'Tanquana', 'Tetracoilanthus', 'Tetragonia', 'Titanopsis', 'Trianthema', 'Trichodiadema', 'Vanheerdea', 'Verrucifera', 'Veslingia']
eup = ['Euphorbia']
cra = ['Adromischus', 'Aeonium', 'Aichryson', 'Aithales', 'Aldasorea', 'Asterosedum', 'Bryophyllum', 'Bulliarda', 'Byrnesia', 'Combesia', 'Cotyledon', 'Cotyliphyllum', 'Crassula', 'Crassuvia', 'Creusa', 'Curtogyne', 'Danielia', 'Dietrichia', 'Diopogon', 'Diotostemon', 'Disporocarpa', 'Dudleya', 'Echeveria', 'Geaya', 'Globulea', 'Gomara', 'Gormania', 'Graptopetalum', 'x Graptosedum', 'x Graptoveria', 'Greenovia', 'Hydrophila', 'Hylotelephium', 'Jovibarba', 'Kalanchoe', 'Kitchingia', 'Larochea', 'Lenophyllum', 'Leucosedum', 'Macrobia', 'Meristostylus', 'Mesanchum', 'Monanthes', 'Oreosedum', 'Orostachys', 'Pachyphytum', 'x Pachyveria', 'Petrogeton', 'Petrophyes', 'Petrosedum', 'Phedimus', 'Procrassula', 'Purgosea', 'Rhodiola', 'Rochea', 'Rosularia', 'x Sedeveria', 'Sedum', 'Sempervivum', 'Septas', 'Septimia', 'Sinocrassula', 'Spathulata', 'Sphaeritis', 'Stylophyllum', 'Tacitus', 'Tetraphyle', 'Thisantha', 'Thysantha', 'Tillaea', 'Tillaeastrum', 'Toelkenia', 'Tolmachevia', 'Turgosea', 'Tylecodon', 'Umbilicus', 'Urbinia', 'Verea', 'Vereia', 'Villadia']
hya = ['Adenotheca', 'Albuca', 'Basaltogeton', 'Bowiea', 'Caloscilla', 'Charybdis', 'Coilonox', 'Daubenya', 'Dipcadi', 'Drimia', 'Drimiopsis', 'Eliokarmos', 'Falconera', 'Fenelonia', 'Hyacinthus', 'Ledebouria', 'Loncomelos', 'Massonia', 'Melomphis', 'Nicipe', 'Oncostema', 'Ornithogalum', 'Podocallis', 'Polyxena', 'Resnova', 'Schizobasis', 'Schizobasopsis', 'Scilla', 'Stellarioides', 'Urginavia', 'Urginea', 'Urophyllon', 'Veltheimia']
por = ['Anacampseros', 'Avonia', 'Calandrinia', 'Ceraria', 'Cistanthe', 'Claytonia', 'Grahamia', 'Helianthemoides', 'Lewisia', 'Oreobroma', 'Phemeranthus', 'Portulaca', 'Portulacaria', 'Ruelingia', 'Talinum']
cac = ['Acanthanthus', 'Acanthocalycium', 'Acanthocephala', 'Acanthocereus', 'Acantholobivia', 'Acanthopetalus', 'Acanthorhipsalis', 'Acharagma', 'Airampoa', 'Akersia', 'Ancistrocactus', 'Andenea', 'Andinopuntia', 'Anhalonium', 'Anisocereus', 'Aparadoa', 'Aporocactus', 'x Aporoheliocereus', 'Arequipa', 'Arequipiopsis', 'Ariocarpus', 'Armatocereus', 'Arrojadoa', 'Arrojadoopsis', 'Arthrocereus', 'Arthrophyllum', 'Astrobergia', 'Astrophytum', 'Aulacothele', 'Austrocactus', 'Austrocephalocereus', 'Austrocylindropuntia', 'Aylostera', 'Aztekium', 'Azureocereus', 'Backebergia', 'Banfiopuntia', 'Bartschella', 'Bergerocactus', 'Bergerocereus', 'Binghamia', 'Bisnaga', 'Blossfeldia', 'Bolivicactus', 'Bolivicereus', 'Bonifazia', 'Borzicactella', 'Borzicactus', 'x Borzipostoa', 'Brachycalycium', 'Brachycereus', 'Bragaia', 'Brasilicactus', 'Brasilicereus', 'Brasiliopuntia', 'Brasiliparodia', 'Brasilocactus', 'Bravocactus', 'Bridgesia', 'Brittonia', 'Brittonrosea', 'Browningia', 'Buiningia', 'Cactodendron', 'Cactus', 'Calymmanthium', 'Carnegiea', 'Carpophillus', 'Cassyta', 'Cassytha', 'Castellanosia', 'Cephalocereus', 'Cephalocleistocactus', 'Cephalomamillaria', 'Cephalophorus', 'Ceratistes', 'Cereus', 'Chaffeyopuntia', 'Chamaecereus', 'x Chamaelobivia', 'Chiapasia', 'Chichipia', 'Chilenia', 'Chileniopsis', 'Chileocactus', 'Chileorebutia', 'Chilita', 'Chrysocactus', 'Cinnabarinea', 'Cintia', 'Cipocereus', 'Cirinosum', 'Clavarioidia', 'Clavatopuntia', 'Cleistocactus', 'Cleistocereus', 'Clistanthocereus', 'Cochemiea', 'Cochiseia', 'Coleocephalocereus', 'Coloradoa', 'Consolea', 'Copiapoa', 'Corryocactus', 'Corryocereus', 'Corynopuntia', 'Coryphantha', 'Cryptocereus', 'Cullmannia', 'Cumarinia', 'Cumulopuntia', 'Cylindrolobivia', 'Cylindropuntia', 'Cylindrorebutia', 'Dactylanthocactus', 'Deamia', 'Delaetia', 'Dendrocereus', 'Denmoza', 'Digitorebutia', 'Digitostigma', 'Diploperianthium', 'Discocactus', 'Disisocactus', 'Disisorhipsalis', 'Disocactus', 'Disocereus', 'Dolichothele', 'Ebnerella', 'Eccremocactus', 'Echinocactus', 'Echinocereus', 'x Echinoferocactus', 'Echinofossulocactus', 'Echinolobivia', 'Echinomastus', 'Echinonyctanthus', 'Echinopsis', 'Echinorebutia', 'Efossus', 'Emorycactus', 'Encephalocarpus', 'Eomatucana', 'x Epinicereus', 'Epiphyllanthus', 'Epiphyllopsis', 'Epiphyllum', 'Epithelantha', 'Erdisia', 'Eriocactus', 'Eriocephala', 'x Eriocereopsis', 'Eriocereus', 'Eriosyce', 'Erythrocereus', 'Erythrorhipsalis', 'Escobaria', 'Escobariopsis', 'Escobesseya', 'Escobrittonia', 'Escocoryphantha', 'Escontria', 'Espostoa', 'x Espostocactus', 'Espostoopsis', 'Estevesia', 'Eulychnia', 'Euporteria', 'Eurebutia', 'Facheiroa', 'x Ferenocactus', 'x Ferobergia', 'Ferocactus', 'x Ferofossulocactus', 'Floribunda', 'Fobea', 'Frailea', 'Friesia', 'Furiolobivia', 'Geohintonia', 'Gerocephalus', 'Glandulicactus', 'Glandulifera', 'Grusonia', 'Gymnantha', 'Gymnanthocereus', 'Gymnocactus', 'Gymnocalycium', 'Gymnocereus', 'Gymnorebutia', 'Haagea', 'Haageocereus', 'x Haagespostoa', 'Hamatocactus', 'Hariota', 'Harrisia', 'x Harrisinopsis', 'Haseltonia', 'Hatiora', 'Heliabravoa', 'Helianthocereus', 'x Heliaporus', 'Heliocereus', 'Hertrichocereus', 'Hickenia', 'Hildewintera', 'Hildmannia', 'Homalocephala', 'Horridocactus', 'Hylocereus', 'Hylorhipsalis', 'Hymenolobivia', 'Hymenorebutia', 'Islaya', 'Isolatocereus', 'Jasminocereus', 'Kadenicarpus', 'Krainzia', 'Lactomamillaria', 'Lagenosocereus', 'Lasiocereus', 'Lemaireocereus', 'Leocereus', 'Lepidocoryphantha', 'Lepismium', 'Leptocereus', 'Leptocladia', 'Leptocladodia', 'Leuchtenbergia', 'Leucostele', 'Leuenbergeria', 'Lobeira', 'Lobivia', 'Lobiviopsis', 'Lodia', 'Lophocereus', 'Lophophora', 'Loxanthocereus', 'Lymanbensonia', 'Machaerocereus', 'Maierocactus', 'Maihuenia', 'Maihueniopsis', 'Malacocarpus', 'Mamillopsis', 'Mammillaria', 'Mammilloydia', 'Marenopuntia', 'Marginatocereus', 'Maritinocereus', 'Marniera', 'Marshallocereus', 'Masarykia', 'Matucana', 'Mediocactus', 'Mediolobivia', 'Mediorebutia', 'Melocactus', 'Mesechinopsis', 'Meyenia', 'Meyerocactus', 'Micranthocereus', 'Micropuntia', 'Microspermia', 'Mila', 'Miqueliopuntia', 'Mirabella', 'Mitrocereus', 'Monvillea', 'Morangaya', 'Morawetzia', 'x Myrtgerocactus', 'Myrtillocactus', 'x Myrtillocalycium', 'Myrtillocereus', 'Napina', 'Navajoa', 'Neoabbottia', 'Neobesseya', 'x Neobinghamia', 'Neobuxbaumia', 'Neocardenasia', 'Neochilenia', 'Neodawsonia', 'Neodiscocactus', 'Neoevansia', 'Neogomesia', 'Neohickenia', 'Neolemaireocereus', 'Neolloydia', 'Neolobivia', 'Neomammillaria', 'Neomatucana', 'Neonavajoa', 'Neoporteria', 'Neoraimondia', 'Neotanahashia', 'Neowerdermannia', 'Nichelia', 'Nopalea', 'Nopalxochia', 'Normanbokea', 'Nothorhipsalis', 'Notocactus', 'Nyctocereus', 'Obregonia', 'Oehmea', 'Ophiorhipsalis', 'Opuntia', 'Opuntiopsis', 'Oreocereus', 'Oroya', 'Ortegocactus', 'x Ortegopuntia', 'x Pacherocactus', 'x Pachgerocereus', 'Pachycereus', 'Parodia', 'Parrycactus', 'Parviopuntia', 'Pediocactus', 'Pelecyphora', 'Peniocereus', 'Pereskia', 'Pereskiopsis', 'Peronocactus', 'Peruvocereus', 'Peyotl', 'Pfeiffera', 'Phellosperma', 'Philippicereus', 'Phyllarthus', 'Phyllocactus', 'Pierrebraunia', 'Pilocanthus', 'Pilocereus', 'Pilocopiapoa', 'Pilosocereus', 'Piptanthocereus', 'Platyopuntia', 'Polaskia', 'Porfiria', 'Praecereus', 'Pseudoacanthocereus', 'Pseudoechinopsis', 'Pseudoespostoa', 'Pseudolobivia', 'Pseudomaihueniopsis', 'Pseudomammillaria', 'Pseudomitrocereus', 'Pseudonopalxochia', 'Pseudopilocereus', 'Pseudorhipsalis', 'Pseudoselenicereus', 'Pseudosolisia', 'Pseudotephrocactus', 'Pseudozygocactus', 'Pterocactus', 'Pterocereus', 'Puebloa', 'Puna', 'Punotia', 'Pygmaeocereus', 'Pyrrhocactus', 'Quiabentia', 'Rapicactus', 'Rathbunia', 'Rauhocereus', 'Rebulobivia', 'Rebutia', 'Reicheocactus', 'Rhipsalidopsis', 'Rhipsalis', 'Rhipsaphyllopsis', 'Rhodocactus', 'Rimacactus', 'Ritterocactus', 'Ritterocereus', 'Rodentiophila', 'Rooksbya', 'Roseocactus', 'Roseocereus', 'Rowleyara', 'Salmonopuntia', 'Salpingolobivia', 'Samaipaticereus', 'Schlumbergera', 'Sclerocactus', 'Scoparebutia', 'Selenicereus', 'x Seleniphyllum', 'Sericocactus', 'Seticereus', 'Seticleistocactus', 'Setiechinopsis', 'Setirebutia', 'Siccobaccatus', 'Soehrensia', 'Solisia', 'Spegazzinia', 'Sphaeropuntia', 'Spinicalycium', 'Stenocactus', 'Stenocereus', 'x Stenogonia', 'Stephanocereus', 'Stetsonia', 'Strombocactus', 'Strophocactus', 'Submatucana', 'Subpilocereus', 'Sulcorebutia', 'Tacinga', 'Tephrocactus', 'x Thelobergia', 'Thelocactus', 'Thelocephala', 'Thelomastus', 'Thrixanthocereus', 'Torreycactus', 'Toumeya', 'Trichocereus', 'x Trichopsis', 'Tunas', 'Tunilla', 'Turbinicarpus', 'Uebelmannia', 'Ursopuntia', 'Utahia', 'Vatricania', 'Weberbauerocereus', 'Weberiopuntia', 'Weberocereus', 'Weingartia', 'Werckleocereus', 'Wigginsia', 'Wilcoxia', 'Wilmattea', 'Winteria', 'Winterocereus', 'Wittia', 'Wittiocactus', 'Yavia', 'Yungasocereus', 'Zehntnerella', 'Zygocactus', 'Zygocereus']


all = asp + asc + aiz + eup + cra + hya + por + cac

cac = ['acs', 'acm', 'aca', 'acs', 'aca', 'acs', 'acs', 'aca', 'aia', 'aka', 'ans', 'ana', 'ana', 'anm', 'ans', 'apa', 'aps', 'xas', 'ara', 'ars', 'ars', 'ars', 'ara', 'ars', 'ars', 'arm', 'asa', 'asm', 'aue', 'aus', 'aus', 'aua', 'aya', 'azm', 'azs', 'baa', 'baa', 'baa', 'bes', 'bes', 'bia', 'bia', 'bla', 'bos', 'bos', 'boa', 'boa', 'bos', 'xba', 'brm', 'brs', 'bra', 'brs', 'brs', 'bra', 'bra', 'brs', 'brs', 'bra', 'bra', 'bra', 'bra', 'bua', 'can', 'cas', 'cam', 'caa', 'cas', 'caa', 'caa', 'caa', 'ces', 'ces', 'cea', 'ces', 'ces', 'ces', 'cha', 'chs', 'xca', 'cha', 'cha', 'cha', 'chs', 'chs', 'cha', 'cha', 'chs', 'cia', 'cia', 'cis', 'cim', 'cla', 'cla', 'cls', 'cls', 'cls', 'coa', 'coa', 'cos', 'coa', 'coa', 'coa', 'cos', 'cos', 'coa', 'coa', 'crs', 'cua', 'cua', 'cua', 'cya', 'cya', 'cya', 'das', 'dea', 'dea', 'des', 'dea', 'dia', 'dia', 'dim', 'dis', 'dis', 'dis', 'dis', 'dis', 'doe', 'eba', 'ecs', 'ecs', 'ecs', 'xes', 'ecs', 'eca', 'ecs', 'ecs', 'ecs', 'eca', 'efs', 'ems', 'ens', 'eoa', 'xes', 'eps', 'eps', 'epm', 'epa', 'era', 'ers', 'era', 'xes', 'ers', 'ere', 'ers', 'ers', 'esa', 'ess', 'esa', 'esa', 'esa', 'esa', 'esa', 'xes', 'ess', 'esa', 'eua', 'eua', 'eua', 'faa', 'xfs', 'xfa', 'fes', 'xfs', 'fla', 'foa', 'fra', 'fra', 'fua', 'gea', 'ges', 'gls', 'gla', 'gra', 'gya', 'gys', 'gys', 'gym', 'gys', 'gya', 'haa', 'has', 'xha', 'has', 'haa', 'haa', 'xhs', 'haa', 'haa', 'hea', 'hes', 'xhs', 'hes', 'hes', 'hia', 'hia', 'hia', 'hoa', 'hos', 'hys', 'hys', 'hya', 'hya', 'isa', 'iss', 'jas', 'kas', 'kra', 'laa', 'las', 'las', 'les', 'les', 'lea', 'lem', 'les', 'lea', 'lea', 'lea', 'lee', 'lea', 'loa', 'loa', 'los', 'loa', 'los', 'loa', 'los', 'lya', 'mas', 'mas', 'maa', 'mas', 'mas', 'mas', 'maa', 'maa', 'maa', 'mas', 'mas', 'maa', 'mas', 'maa', 'maa', 'mes', 'mea', 'mea', 'mes', 'mes', 'mea', 'mes', 'mis', 'mia', 'mia', 'mia', 'mia', 'mia', 'mis', 'moa', 'moa', 'moa', 'xms', 'mys', 'xmm', 'mys', 'naa', 'naa', 'nea', 'nea', 'xna', 'nea', 'nea', 'nea', 'nea', 'nes', 'nea', 'nea', 'nea', 'nes', 'nea', 'nea', 'nea', 'nea', 'nea', 'nea', 'nea', 'nea', 'nea', 'nia', 'noa', 'noa', 'noa', 'nos', 'nos', 'nys', 'oba', 'oea', 'ops', 'opa', 'ops', 'ors', 'ora', 'ors', 'xoa', 'xps', 'xps', 'pas', 'paa', 'pas', 'paa', 'pes', 'pea', 'pes', 'pea', 'pes', 'pes', 'pes', 'pel', 'pfa', 'pha', 'phs', 'phs', 'phs', 'pia', 'pis', 'pis', 'pia', 'pis', 'pis', 'pla', 'poa', 'poa', 'prs', 'pss', 'pss', 'psa', 'psa', 'pss', 'psa', 'pss', 'psa', 'pss', 'pss', 'pss', 'psa', 'pss', 'pss', 'pts', 'pts', 'pua', 'pua', 'pua', 'pys', 'pys', 'qua', 'ras', 'raa', 'ras', 'rea', 'rea', 'res', 'rhs', 'rhs', 'rhs', 'rhs', 'ris', 'ris', 'ris', 'roa', 'roa', 'ros', 'ros', 'roa', 'saa', 'saa', 'sas', 'sca', 'scs', 'sca', 'ses', 'xsm', 'ses', 'ses', 'ses', 'ses', 'sea', 'sis', 'soa', 'soa', 'spa', 'spa', 'spm', 'sts', 'sts', 'xsa', 'sts', 'sta', 'sts', 'sts', 'sua', 'sus', 'sua', 'taa', 'tes', 'xta', 'ths', 'tha', 'ths', 'ths', 'tos', 'toa', 'trs', 'xts', 'tus', 'tua', 'tus', 'uea', 'ura', 'uta', 'vaa', 'wes', 'wea', 'wes', 'wea', 'wes', 'wia', 'wia', 'wia', 'wia', 'wis', 'wia', 'wis', 'yaa', 'yus', 'zea', 'zys', 'zys']

asp = ['ale', 'als', 'aln', 'ala', 'xaa', 'apa', 'are', 'asa', 'xaa', 'buo', 'caa', 'xge', 'xga', 'gaa', 'xga', 'gua', 'haa', 'has', 'kua', 'kua', 'lea', 'lee', 'pan', 'poa', 'pts', 'rhm', 'tua']

asc = ['ana', 'ana', 'apa', 'aps', 'ass', 'aua', 'baa', 'boa', 'bra', 'caa', 'caa', 'caa', 'cea', 'ces', 'cea', 'chs', 'cia', 'cos', 'cra', 'cra', 'cym', 'cym', 'cys', 'dee', 'des', 'des', 'dia', 'dia', 'dis', 'dis', 'dia', 'dra', 'dua', 'dua', 'ecs', 'eda', 'foa', 'fra', 'fum', 'goa', 'gos', 'gon', 'gya', 'hea', 'hoa', 'xha', 'hoa', 'hua', 'hus', 'hua', 'iss', 'laa', 'laa', 'laa', 'lea', 'lea', 'lea', 'lin', 'lua', 'mam', 'maa', 'maa', 'mir', 'moa', 'mom', 'nea', 'nos', 'oba', 'opa', 'ora', 'ors', 'ors', 'ota', 'pam', 'pea', 'pes', 'pea', 'pea', 'pea', 'pha', 'pha', 'pha', 'pis', 'pla', 'pos', 'pss', 'psa', 'qua', 'rae', 'rae', 'rhn', 'ria', 'saa', 'san', 'sas', 'saa', 'scm', 'sca', 'sca', 'scs', 'soa', 'spm', 'spa', 'xsa', 'sta', 'sts', 'sts', 'sta', 'sta', 'sta', 'sta', 'sua', 'taa', 'taa', 'taa', 'xta', 'xtn', 'trn', 'tra', 'trm', 'tre', 'vim', 'wha', 'zaa', 'zua']

eup = ['eua']

aiz = ['abm', 'acn', 'acn', 'ain', 'ain', 'als', 'ama', 'anx', 'anm', 'ana', 'apa', 'ara', 'ara', 'ara', 'asa', 'bes', 'bia', 'bom', 'bra', 'cas', 'cas', 'cem', 'ces', 'chm', 'chs', 'com', 'com', 'coa', 'crs', 'crm', 'cym', 'das', 'dee', 'dea', 'des', 'dea', 'din', 'dis', 'dia', 'drs', 'drs', 'drm', 'eba', 'ecs', 'era', 'faa', 'fea', 'fra', 'gal', 'gim', 'glm', 'haa', 'has', 'haa', 'has', 'hea', 'hea', 'hys', 'iha', 'ima', 'jaa', 'jea', 'jua', 'las', 'laa', 'lis', 'lis', 'lua', 'mam', 'maa', 'maa', 'maa', 'mex', 'mem', 'mea', 'mem', 'mim', 'mim', 'moa', 'moa', 'naa', 'nas', 'nea', 'nee', 'nys', 'ods', 'opm', 'opm', 'orm', 'osa', 'pea', 'pes', 'pes', 'phs', 'pla', 'pls', 'pra', 'pra', 'pse', 'psa', 'psn', 'pts', 'pua', 'pya', 'raa', 'rhm', 'rhm', 'ria', 'roa', 'rua', 'rus', 'scm', 'sca', 'sca', 'sem', 'sma', 'sps', 'stm', 'stm', 'sym', 'taa', 'tes', 'tea', 'tis', 'tra', 'tra', 'vaa', 'vea', 'vea']

cra = ['ads', 'aem', 'ain', 'ais', 'ala', 'asm', 'brm', 'bua', 'bya', 'coa', 'con', 'com', 'cra', 'cra', 'cra', 'cue', 'daa', 'dia', 'din', 'din', 'dia', 'dua', 'eca', 'gea', 'gla', 'goa', 'goa', 'grm', 'xgm', 'xga', 'gra', 'hya', 'hym', 'joa', 'kae', 'kia', 'laa', 'lem', 'lem', 'maa', 'mes', 'mem', 'mos', 'orm', 'ors', 'pam', 'xpa', 'pen', 'pes', 'pem', 'phs', 'pra', 'pua', 'rha', 'roa', 'roa', 'xsa', 'sem', 'sem', 'ses', 'sea', 'sia', 'spa', 'sps', 'stm', 'tas', 'tee', 'tha', 'tha', 'tia', 'tim', 'toa', 'toa', 'tua', 'tyn', 'ums', 'ura', 'vea', 'vea', 'via']

hya = ['ada', 'ala', 'ban', 'boa', 'caa', 'chs', 'cox', 'daa', 'dii', 'dra', 'drs', 'els', 'faa', 'fea', 'hys', 'lea', 'los', 'maa', 'mes', 'nie', 'ona', 'orm', 'pos', 'poa', 'rea', 'scs', 'scs', 'sca', 'sts', 'ura', 'ura', 'urn', 'vea']

por = ['ans', 'ava', 'caa', 'cea', 'cie', 'cla', 'gra', 'hes', 'lea', 'ora', 'phs', 'poa', 'poa', 'rua', 'tam']


cac = {'NAME':'Cactaceae', 'zea': 'Zehntnerella', 'roa': 'Rodentiophila', 'sca': 'Schlumbergera', 'xes': 'x Echinoferocactus', 'sta': 'Stetsonia', 'pes': 'Pediocactus', 'pts': 'Pterocactus', 'scs': 'Sclerocactus', 'aua': 'Austrocylindropuntia', 'xmm': 'x Myrtillocalycium', 'wea': 'Weberiopuntia', 'aue': 'Aulacothele', 'haa': 'Haagea', 'eua': 'Eulychnia', 'cla': 'Clavarioidia', 'wes': 'Weberbauerocereus', 'aus': 'Austrocactus', 'cua': 'Cullmannia', 'has': 'Haageocereus', 'cls': 'Cleistocactus', 'ges': 'Gerocephalus', 'cea': 'Cephalomamillaria', 'crs': 'Cryptocereus', 'psa': 'Pseudoespostoa', 'xha': 'x Haagespostoa', 'bia': 'Binghamia', 'hia': 'Hickenia', 'gea': 'Geohintonia', 'ces': 'Cephalocereus', 'opa': 'Opuntia', 'das': 'Dactylanthocactus', 'pss': 'Pseudoacanthocereus', 'moa': 'Monvillea', 'faa': 'Facheiroa', 'nos': 'Nothorhipsalis', 'dim': 'Diploperianthium', 'dia': 'Digitorebutia', 'pea': 'Pelecyphora', 'hys': 'Hylocereus', 'ems': 'Emorycactus', 'baa': 'Backebergia', 'trs': 'Trichocereus', 'dis': 'Discocactus', 'ars': 'Arequipiopsis', 'ses': 'Selenicereus', 'eba': 'Ebnerella', 'ops': 'Ophiorhipsalis', 'uea': 'Uebelmannia', 'ara': 'Arequipa', 'sea': 'Setirebutia', 'tes': 'Tephrocactus', 'arm': 'Arthrophyllum', 'xhs': 'x Harrisinopsis', 'ros': 'Roseocactus', 'ess': 'Escobariopsis', 'sua': 'Submatucana', 'res': 'Reicheocactus', 'nea': 'Neoabbottia', 'pel': 'Peyotl', 'xsa': 'x Stenogonia', 'sus': 'Subpilocereus', 'foa': 'Fobea', 'esa': 'Escobaria', 'xoa': 'x Ortegopuntia', 'rea': 'Rebulobivia', 'bla': 'Blossfeldia', 'nes': 'Neodiscocactus', 'can': 'Cactodendron', 'lea': 'Lepidocoryphantha', 'tus': 'Tunas', 'pys': 'Pygmaeocereus', 'mea': 'Mediolobivia', 'lee': 'Leucostele', 'eca': 'Echinolobivia', 'xfa': 'x Ferobergia', 'sts': 'Stenocactus', 'lem': 'Lepismium', 'ors': 'Oreocereus', 'qua': 'Quiabentia', 'asa': 'Astrobergia', 'les': 'Lemaireocereus', 'ecs': 'Eccremocactus', 'mes': 'Mediocactus', 'bes': 'Bergerocactus', 'xts': 'x Trichopsis', 'xfs': 'x Ferenocactus', 'xsm': 'x Seleniphyllum', 'asm': 'Astrophytum', 'ora': 'Oroya', 'maa': 'Maihuenia', 'cos': 'Coleocephalocereus', 'iss': 'Isolatocereus', 'gla': 'Glandulifera', 'yus': 'Yungasocereus', 'bos': 'Bolivicactus', 'acm': 'Acanthocalycium', 'oba': 'Obregonia', 'acs': 'Acanthanthus', 'boa': 'Bonifazia', 'aka': 'Akersia', 'gls': 'Glandulicactus', 'soa': 'Soehrensia', 'vaa': 'Vatricania', 'pla': 'Platyopuntia', 'wia': 'Wigginsia', 'aps': 'Aporocactus', 'brs': 'Brachycereus', 'jas': 'Jasminocereus', 'brm': 'Brachycalycium', 'wis': 'Winterocereus', 'tua': 'Tunilla', 'apa': 'Aparadoa', 'oea': 'Oehmea', 'bra': 'Bragaia', 'poa': 'Polaskia', 'cha': 'Chaffeyopuntia', 'fra': 'Frailea', 'loa': 'Lobeira', 'hes': 'Helianthocereus', 'tos': 'Torreycactus', 'xas': 'x Aporoheliocereus', 'aya': 'Aylostera', 'los': 'Lobiviopsis', 'chs': 'Chamaecereus', 'fes': 'Ferocactus', 'pia': 'Pierrebraunia', 'xps': 'x Pacherocactus', 'toa': 'Toumeya', 'yaa': 'Yavia', 'saa': 'Salmonopuntia', 'hea': 'Heliabravoa', 'pfa': 'Pfeiffera', 'xta': 'x Thelobergia', 'gya': 'Gymnantha', 'taa': 'Tacinga', 'gym': 'Gymnocalycium', 'aca': 'Acanthocephala', 'rhs': 'Rhipsalidopsis', 'cya': 'Cylindrolobivia', 'gys': 'Gymnanthocereus', 'bua': 'Buiningia', 'cia': 'Cinnabarinea', 'uta': 'Utahia', 'azm': 'Aztekium', 'ers': 'Eriocactus', 'cas': 'Cactus', 'des': 'Dendrocereus', 'cim': 'Cirinosum', 'cis': 'Cipocereus', 'ere': 'Eriosyce', 'era': 'Erdisia', 'cam': 'Calymmanthium', 'fua': 'Furiolobivia', 'fla': 'Floribunda', 'dea': 'Deamia', 'caa': 'Carnegiea', 'azs': 'Azureocereus', 'aia': 'Airampoa', 'ras': 'Rapicactus', 'xca': 'x Chamaelobivia', 'ana': 'Andenea', 'raa': 'Rathbunia', 'anm': 'Anhalonium', 'mys': 'Myrtillocactus', 'ris': 'Rimacactus', 'xna': 'x Neobinghamia', 'spm': 'Spinicalycium', 'lya': 'Lymanbensonia', 'prs': 'Praecereus', 'ans': 'Ancistrocactus', 'sas': 'Samaipaticereus', 'spa': 'Spegazzinia', 'pis': 'Pilocanthus', 'sis': 'Siccobaccatus', 'coa': 'Cochemiea', 'pua': 'Puebloa', 'naa': 'Napina', 'hoa': 'Homalocephala', 'mia': 'Micropuntia', 'nys': 'Nyctocereus', 'efs': 'Efossus', 'paa': 'Parodia', 'ens': 'Encephalocarpus', 'hos': 'Horridocactus', 'gra': 'Grusonia', 'mis': 'Micranthocereus', 'mas': 'Machaerocereus', 'xms': 'x Myrtgerocactus', 'pha': 'Phellosperma', 'nia': 'Nichelia', 'laa': 'Lactomamillaria', 'noa': 'Nopalea', 'kas': 'Kadenicarpus', 'pas': 'Pachycereus', 'phs': 'Philippicereus', 'isa': 'Islaya', 'las': 'Lagenosocereus', 'eoa': 'Eomatucana', 'kra': 'Krainzia', 'ura': 'Ursopuntia', 'hya': 'Hymenolobivia', 'ths': 'Thelocactus', 'eps': 'Epiphyllanthus', 'doe': 'Dolichothele', 'epm': 'Epiphyllum', 'zys': 'Zygocactus', 'xba': 'x Borzipostoa', 'tha': 'Thelocephala', 'epa': 'Epithelantha'}
asp = {'NAME':'Asphodelaceae', 'aln': 'Aloidendron', 'xge': 'x Gasteraloe', 'ala': 'Aloinella', 'are': 'Aristaloe', 'apa': 'Apicra', 'pts': 'Ptyas', 'als': 'Aloiampelos', 'poa': 'Poellnitzia', 'haa': 'Haworthia', 'xaa': 'x Astroworthia', 'has': 'Haworthiopsis', 'kua': 'Kumaria', 'lea': 'Lemeea', 'ale': 'Aloe', 'lee': 'Leptaloe', 'asa': 'Astroloba', 'rhm': 'Rhipidodendrum', 'buo': 'Busipho', 'tua': 'Tulista', 'xga': 'x Gastrolea', 'gaa': 'Gasteria', 'gua': 'Guillauminia', 'pan': 'Pachidendron', 'caa': 'Catevala'}
asc = {'NAME':'Asclepiadaceae', 'scm': 'Schizoglossum', 'eda': 'Edithcolea', 'sca': 'Schollia', 'pes': 'Pentagonanthus', 'scs': 'Scytanthus', 'aua': 'Australluma', 'xta': 'x Tavarorbea', 'xtn': 'x Tavastemon', 'cea': 'Ceropegia', 'psa': 'Pseudopectinaria', 'cia': 'Cibirhiza', 'ces': 'Ceramanthus', 'opa': 'Ophionella', 'mom': 'Monothylaceum', 'pss': 'Pseudolithos', 'moa': 'Monolluma', 'zaa': 'Zaczatea', 'nos': 'Notechidnopsis', 'trm': 'Triodoglossum', 'trn': 'Trichocaulon', 'tra': 'Tridentea', 'tre': 'Tromotriche', 'dia': 'Dischidia', 'xsa': 'x Staparesia', 'baa': 'Baynesia', 'dis': 'Diplolepis', 'gon': 'Gonostemon', 'sua': 'Sulcolluma', 'goa': 'Gongronema', 'nea': 'Neopectinaria', 'lua': 'Luckhoffia', 'cra': 'Cryptolluma', 'foa': 'Fockea', 'pea': 'Petopentia', 'gos': 'Gonolobus', 'ass': 'Asclepias', 'lea': 'Leptostemma', 'ors': 'Orbeopsis', 'qua': 'Quaqua', 'ecs': 'Echidnopsis', 'pla': 'Plocostemma', 'ora': 'Orbea', 'cos': 'Collyris', 'iss': 'Ischnolepis', 'oba': 'Obesia', 'zua': 'Zucchellia', 'dra': 'Drakebrockmania', 'boa': 'Boucerosia', 'soa': 'Socotrella', 'aps': 'Apteranthes', 'pos': 'Podanthes', 'vim': 'Vincetoxicum', 'apa': 'Apoxyanthera', 'bra': 'Brachystelma', 'san': 'Sarcocodon', 'fra': 'Frerea', 'dua': 'Duvaliandra', 'chs': 'Chymocormus', 'hea': 'Hermanschwartzia', 'cys': 'Cyrtoceras', 'hua': 'Hutchinia', 'gya': 'Gymnema', 'ota': 'Otostemma', 'hus': 'Huerniopsis', 'cym': 'Cynoctonum', 'xha': 'x Hoodiapelia', 'sta': 'Stultitia', 'des': 'Desmidorchis', 'sts': 'Stapeliopsis', 'caa': 'Caudanthera', 'fum': 'Funastrum', 'dee': 'Decabelone', 'taa': 'Tavaresia', 'rae': 'Raphionacme', 'ana': 'Anomalluma', 'saa': 'Sarcostemma', 'spm': 'Spathulopetalum', 'sas': 'Sarcophagophilus', 'spa': 'Spiralluma', 'pis': 'Piaranthus', 'ria': 'Richtersveldia', 'hoa': 'Hoya', 'lin': 'Lithocaulon', 'mir': 'Micraster', 'pam': 'Pachycymbium', 'wha': 'Whitesloanea', 'pha': 'Physostelma', 'laa': 'Lavrania', 'maa': 'Matelea', 'rhn': 'Rhytidocaulon', 'mam': 'Macropetalum'}
eup = {'NAME':'Euphorbiaceae', 'eua':'Euphorbia'}
aiz = {'NAME':'Aizoaceae', 'scm': 'Sceletium', 'roa': 'Roodia', 'sca': 'Schwantesia', 'osa': 'Oscularia', 'pes': 'Perapentacoilanthus', 'pts': 'Pteropentacoilanthus', 'als': 'Aloinopsis', 'ima': 'Imitaria', 'haa': 'Hammeria', 'vea': 'Veslingia', 'has': 'Hartmanthus', 'jaa': 'Jacobsenia', 'psn': 'Psilocaulon', 'ama': 'Amphibolia', 'cem': 'Cephalophyllum', 'psa': 'Psammophora', 'pse': 'Psammanthe', 'ces': 'Cerochlamys', 'das': 'Dactylopsis', 'opm': 'Opophytum', 'moa': 'Mossia', 'faa': 'Faucaria', 'crs': 'Crocanthus', 'din': 'Dicrocaulon', 'tra': 'Trichodiadema', 'dia': 'Diplosoma', 'hys': 'Hymenocyclus', 'dis': 'Dinteranthus', 'eba': 'Ebracteola', 'tea': 'Tetragonia', 'ods': 'Odontophorus', 'ara': 'Aridaria', 'pls': 'Pleiospilos', 'sem': 'Sesuvium', 'tes': 'Tetracoilanthus', 'iha': 'Ihlenfeldtia', 'nee': 'Neorhine', 'abm': 'Abryanthemum', 'nea': 'Neohenricia', 'lua': 'Ludolfia', 'pea': 'Peersia', 'sma': 'Smicrostigma', 'mea': 'Mestoklema', 'mem': 'Meyerophytum', 'chs': 'Cheiridopsis', 'rua': 'Ruschia', 'pua': 'Punctillaria', 'asa': 'Astridia', 'orm': 'Orthopterum', 'ecs': 'Echinus', 'pla': 'Platythyra', 'bes': 'Bergeranthus', 'rus': 'Ruschianthus', 'mex': 'Mentocalyx', 'glm': 'Glottiphyllum', 'drs': 'Drosanthemopsis', 'acn': 'Acrodon', 'coa': 'Corpuscularia', 'drm': 'Drosanthemum', 'bom': 'Bolusanthemum', 'crm': 'Cryophytum', 'com': 'Conophytum', 'apa': 'Aptenia', 'bra': 'Braunsia', 'fra': 'Frithia', 'fea': 'Fenestraria', 'vaa': 'Vanheerdea', 'chm': 'Chasmatophyllum', 'jea': 'Jensenobotrya', 'hea': 'Hereroa', 'gim': 'Gibbaeum', 'jua': 'Juttadinteria', 'gal': 'Gasoul', 'cym': 'Cylindrophyllum', 'cas': 'Carruanthus', 'stm': 'Stomatium', 'des': 'Depacarpus', 'ain': 'Aizoon', 'era': 'Erepsia', 'dea': 'Derenbergia', 'dee': 'Deilanthe', 'pra': 'Prepodesma', 'ana': 'Antimima', 'raa': 'Rabiea', 'anm': 'Antegibbaeum', 'sps': 'Sphalmanthus', 'taa': 'Tanquana', 'anx': 'Anisocalyx', 'ria': 'Rimaria', 'naa': 'Namibia', 'mim': 'Mitrophyllum', 'nys': 'Nycteranthus', 'tis': 'Titanopsis', 'nas': 'Nananthus', 'lis': 'Litocarpus', 'laa': 'Lapidaria', 'sym': 'Synaptophyllum', 'maa': 'Maughaniella', 'rhm': 'Rhombophyllum', 'phs': 'Phyllobolus', 'pya': 'Pyxipoma', 'bia': 'Bijlia', 'mam': 'Machairophyllum', 'las': 'Lampranthus'}
cra = {'NAME':'Crassulaceae', 'tim': 'Tillaeastrum', 'xgm': 'x Graptosedum', 'pra': 'Procrassula', 'tas': 'Tacitus', 'roa': 'Rosularia', 'sps': 'Sphaeritis', 'tee': 'Tetraphyle', 'ala': 'Aldasorea', 'phs': 'Phedimus', 'brm': 'Bryophyllum', 'via': 'Villadia', 'sea': 'Septimia', 'spa': 'Spathulata', 'ses': 'Septas', 'sem': 'Sempervivum', 'pua': 'Purgosea', 'ads': 'Adromischus', 'ums': 'Umbilicus', 'pem': 'Petrosedum', 'dua': 'Dudleya', 'xpa': 'x Pachyveria', 'goa': 'Gormania', 'pen': 'Petrogeton', 'pes': 'Petrophyes', 'mos': 'Monanthes', 'cue': 'Curtogyne', 'ain': 'Aichryson', 'gra': 'Greenovia', 'grm': 'Graptopetalum', 'ors': 'Orostachys', 'bya': 'Byrnesia', 'lem': 'Leucosedum', 'tyn': 'Tylecodon', 'daa': 'Danielia', 'eca': 'Echeveria', 'mem': 'Mesanchum', 'sia': 'Sinocrassula', 'vea': 'Vereia', 'laa': 'Larochea', 'hym': 'Hylotelephium', 'maa': 'Macrobia', 'joa': 'Jovibarba', 'gea': 'Geaya', 'orm': 'Oreosedum', 'mes': 'Meristostylus', 'kae': 'Kalanchoe', 'tua': 'Turgosea', 'kia': 'Kitchingia', 'bua': 'Bulliarda', 'xga': 'x Graptoveria', 'asm': 'Asterosedum', 'tia': 'Tillaea', 'hya': 'Hydrophila', 'din': 'Diotostemon', 'toa': 'Tolmachevia', 'ura': 'Urbinia', 'gla': 'Globulea', 'dia': 'Disporocarpa', 'ais': 'Aithales', 'pam': 'Pachyphytum', 'coa': 'Combesia', 'aem': 'Aeonium', 'cra': 'Creusa', 'rha': 'Rhodiola', 'stm': 'Stylophyllum', 'xsa': 'x Sedeveria', 'com': 'Cotyliphyllum', 'tha': 'Thysantha', 'con': 'Cotyledon'}
hya = {'NAME':'Hyacinthaceae', 'ona': 'Oncostema', 'sca': 'Scilla', 'pos': 'Podocallis', 'ala': 'Albuca', 'scs': 'Schizobasopsis', 'poa': 'Polyxena', 'fea': 'Fenelonia', 'los': 'Loncomelos', 'chs': 'Charybdis', 'ada': 'Adenotheca', 'els': 'Eliokarmos', 'rea': 'Resnova', 'lea': 'Ledebouria', 'daa': 'Daubenya', 'vea': 'Veltheimia', 'nie': 'Nicipe', 'maa': 'Massonia', 'ban': 'Basaltogeton', 'orm': 'Ornithogalum', 'mes': 'Melomphis', 'faa': 'Falconera', 'ura': 'Urginea', 'dii': 'Dipcadi', 'cox': 'Coilonox', 'drs': 'Drimiopsis', 'hys': 'Hyacinthus', 'sts': 'Stellarioides', 'dra': 'Drimia', 'boa': 'Bowiea', 'caa': 'Caloscilla', 'urn': 'Urophyllon'}
por = {'NAME':'Portulacaceae', 'lea': 'Lewisia', 'rua': 'Ruelingia', 'cea': 'Ceraria', 'cie': 'Cistanthe', 'hes': 'Helianthemoides', 'gra': 'Grahamia', 'cla': 'Claytonia', 'ans': 'Anacampseros', 'phs': 'Phemeranthus', 'tam': 'Talinum', 'caa': 'Calandrinia', 'poa': 'Portulacaria', 'ava': 'Avonia', 'ora': 'Oreobroma'}

 
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





"""
Asclepiadaceae | 10 seeds
Hyacinthaceae 10 seeds
Asphodelaceae | 10 seeds
Crassulaceae
Aizoaceae | 25 seeds
Cactaceae | 10 seeds
Portulacaceae
Euphorbiaceae | 5 seeds
"""




def orgpics(filename, form):
	form[filename[:3]].append(filename[4:])



aseeds= """<!DOCTYPE html>
<html>
	<head>
		<meta http-equiv="content-type"
content="text/html;charset=utf-8" />
		<title>
		CK: Seeds
		</title>
		<meta name="viewport" content="initial-scale=1, maximum-scale=1, user-scalable=0">
		
		<link rel="stylesheet" type="text/css" href="../depics/css/layoutNew.css">
	</head>

	<body>
		<div class="outer">
		<div class="middle">
		<div id="container">

			<div id="myNav" class="overlay">
			<h1 class="center">Page Navigation</h1>
		  <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>
		  <div class="overlay-content">
		  	<hr>
		    <a href="/">Home</a>
		    <hr>
		    <a href="/carltons-karoo/seeds.html">Seeds</a>
		     <hr>
		    <a href="/carltons-karoo/plants.html">Plants </a>
		    <hr>
		    <a href="/carltons-karoo/cultivation.html">Succulent Cultivation Notes</a>

		    <hr>
		    <a href="/homebrew/index.html">Homebrew</a>
		    <hr>
		  </div>
		</div>

			<div id="contentSingleTop">
				<img src="../depics/images/seeds.jpg" 
				class="croppedImage">
				<h2 class="repoDescriptionHeader">Seeds<br>For Sale</h2>

				<span style="font-size:35px;cursor:pointer" class="right" onclick="openNav()">&#9776;</span>

				<script>
				function openNav() {
				  document.getElementById("myNav").style.width = "100%";
				}

				function closeNav() {
				  document.getElementById("myNav").style.width = "0%";
				}
				</script>
			
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
							The shipping is $2 for up to 6 packs of seeds.  $0.50 for each additional 4 packs.  Seed amount per pack differs according to familial rank and is displayed to the right of each botanical family.  If seeds are the product of unknown hybridization the mother plant will be displayed. 
						</p>
					</li> 
				</ul> 
			</div>

					 <div id="contentSingle">
						     <h3 class="textHeaderLabel">"""
ofam = """</h3>
					 </div>
					 <div id="contentBottom">
							<ul>"""
oseeds="""</div>
					</li>
				</ul>			
			</div><!--Close Package Header Div-->

		</div><!--Close Container Div-->
		</div>
		</div>
	</body>
	
</html>
"""

aentry="""
								<li>
									<a href=""""


seeds={'form':['seeds'],'asp':[],'asc':[],'aiz':[],'eup':[],'cra':[],'hya':[],'por':[],'cac':[]}
plants={'form':['plants'],'asp':[],'asc':[],'aiz':[],'eup':[],'cra':[],'hya':[],'por':[],'cac':[]}



dirx=os.environ['HOME'] +'/git/carltons-karoo/'
begin="""<!DOCTYPE html>
<html>
	<head>
		<meta http-equiv="content-type"
content="text/html;charset=utf-8" />
		<title>
		CK: Seeds
		</title>
		<meta name="viewport" content="initial-scale=1, maximum-scale=1, user-scalable=0">
		
		<link rel="stylesheet" type="text/css" href="../depics/css/layoutNew.css">
	</head>

	<body>
		<div class="outer">
		<div class="middle">
		<div id="container">

			<div id="myNav" class="overlay">
			<h1 class="center">Page Navigation</h1>
		  <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>
		  <div class="overlay-content">
		  	<hr>
		    <a href="/">Home</a>
		    <hr>
		    <a href="/carltons-karoo/seeds.html">Seeds</a>
		     <hr>
		    <a href="/carltons-karoo/plants.html">Plants </a>
		    <hr>
		    <a href="/carltons-karoo/cultivation.html">Succulent Cultivation Notes</a>

		    <hr>
		    <a href="/homebrew/index.html">Homebrew</a>
		    <hr>
		  </div>
		</div>

			<div id="contentSingleTop">
				<img src="../depics/images/seeds.jpg" 
				class="croppedImage">
				<h2 class="repoDescriptionHeader">Seeds<br>For Sale</h2>

				<span style="font-size:35px;cursor:pointer" class="right" onclick="openNav()">&#9776;</span>

				<script>
				function openNav() {
				  document.getElementById("myNav").style.width = "100%";
				}

				function closeNav() {
				  document.getElementById("myNav").style.width = "0%";
				}
				</script>
			
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
							The shipping is $2 for up to 6 packs of seeds.  $0.50 for each additional 4 packs.  Seed amount per pack differs according to familial rank and is displayed to the right of each botanical family.  If seeds are the product of unknown hybridization the mother plant will be displayed. 
						</p>
					</li> 
				</ul> 
			</div>
"""

seeds={'form':['seeds'],'asp':['Asphodelaceae | 10 seeds'],'asc':['Asclepiadaceae | 10 seeds'],'aiz':['Aizoaceae | 25 seeds'],'eup':['Euphorbiaceae | 5 seeds'],'cra':['Crassulaceae | 10 seeds'],'hya':['Hyacinthaceae 10 seeds'],'por':['Portulacaceae | 10 seeds'],'cac':['Cactaceae | 10 seeds']}
plants={'form':['seeds'],'asp':['Asphodelaceae | 10 seeds'],'asc':['Asclepiadaceae | 10 seeds'],'aiz':['Aizoaceae | 25 seeds'],'eup':['Euphorbiaceae | 5 seeds'],'cra':['Crassulaceae | 10 seeds'],'hya':['Hyacinthaceae 10 seeds'],'por':['Portulacaceae | 10 seeds'],'cac':['Cactaceae | 10 seeds']}


def orgpics(form):
	for line in (os.listdir(dirx + 'pics/' + form['form'][0])):
		if line != '.DS_Store':
			form[line[:3]].append(line)

def sortnew(dic):
	full=[]
	for key in dic:
		if len(dic[key]) > 1:
			full.append(key)
			full.sort()
	return full

def decy(filename):
	splitname=filename.replace('.JPG', '').split('!')
	splitname[1] = splitname[1][:1].upper() + splitname[1][1:]
	splitname[3] = '$' + splitname[3]
	splitname.append(filename)
	return splitname

fambegin='''<div id="contentSingle">
						     <h3 class="textHeaderLabel">'''
titleend='''</h3>
					 </div>
					 <div id="contentBottom">
					 	<ul>'''
famend='''</ul>
					</div>'''

#def addtosite():
s=open((dirx + 'seeds.html'), 'w+')
linkfix='pics/seeds/'
s.write(begin)
for key in sortnew(seeds):
	s.write( fambegin + seeds[key][0] + titleend)
	x = decy(seeds[key][1])
	s.write('<a href="' + (linkfix + x[4].replace('"', '&#34;')) + '">' + (x[1] + ' ' + x[2]) + '</a> ' + x[3])
	for index in seeds[key]:
		if seeds[key].index(index) > 1:
			x = decy(index)
			s.write('<hr>\n<a href="' + (linkfix + x[4].replace('"', '&#34;')) + '">' + (x[1] + ' ' + x[2]) + '</a> ' + x[3])
	s.write(famend)

s.write('''</ul>
					</div>
					</li>
				</ul>			
			</div><!--Close Package Header Div-->

		</div><!--Close Container Div-->
		</div>
		</div>
	</body>
	
</html>''')
s.close()


	p.close()
	exit














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
