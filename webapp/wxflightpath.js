
const airports= {'EDLF44': 'COLMAR-MEYENHEIM (CLOSED)', 'EGJJ': 'JERSEY', 'ELLX': 'LUXEMBOURG', 'FMCZ': 'DZAOUDZI PAMANDZI', 'FMEE': 'LA REUNION-ROLAND GARROS', 'FMEP': 'SAINT PIERRE PIERREFONDS', 'LF01': 'ALBE', 'LF02': 'BEAUMONT DE LOMAGNE', 'LF03': 'BERDOUES', 'LF04': 'BOULOC', 'LF05': 'BUXEUIL ST REMY / CREUSE', 'LF06': 'CALVIAC', 'LF07': 'CAYLUS', 'LF08': 'LACAVE LE FRAU', 'LF09': 'CORBONOD', 'LF10': 'EYREIN (CLOSED)', 'LF11': 'DAMBLAIN (CLOSED)', 'LF12': 'BROYE LES PESMES (CLOSED)', 'LF13': "L'ISLE EN DODON", 'LF14': 'PEYRELEVADE', 'LF15': 'ROCROI REGNIOWEZ (CLOSED)', 'LF16': 'SAINT BENOIT DU SAULT (CLOSED)', 'LF17': 'MARIGNY LE GRAND (CLOSED)', 'LF18': 'SAINT CYR LA CAMPAGNE', 'LF20': 'SEPTFONDS', 'LF23': 'TALMONT VENDEE AIR PARK', 'LF27': 'ROCHEFORT SOUBISE (CLOSED)', 'LF30': 'SAINT BRIEUC (CLOSED)', 'LF31': 'DREUX SENONCHES (CLOSED)', 'LF32': 'LAON COUVRON (CLOSED)', 'LF33': 'LAON ATHIES (CLOSED)', 'LF34': 'MOUSSOULENS (CLOSED)', 'LF35': 'GROSTENQUIN (CLOSED)', 'LF36': 'FREJUS SAINT RAPHAEL (CLOSED)', 'LF37': 'PERPIGNAN LA SALANQUE (CLOSED)', 'LF38': 'LUCON CHASNAIS', 'LF39': 'CREIL (CLOSED)', 'LF40': 'SAINT CHRISTOL (CLOSED)', 'LF41': 'BRETIGNY SUR ORGE (CLOSED)', 'LF42': 'CAMBRAI EPINOY (CLOSED)', 'LF43': 'REIMS CHAMPAGNE (CLOSED)', 'LF45': 'METZ FRESCATY (CLOSED)', 'LFAB': 'DIEPPE SAINT AUBIN', 'LFAC': 'CALAIS MARCK', 'LFAD': 'COMPIEGNE MARGNY', 'LFAE': 'EU MERS LE TREPORT', 'LFAF': 'LAON CHAMBRY', 'LFAG': 'PERONNE SAINT QUENTIN', 'LFAI': 'NANGIS LES LOGES', 'LFAJ': 'ARGENTAN', 'LFAK': 'DUNKERQUE LES MOERES', 'LFAL': 'LA FLECHE THOREE LES PINS', 'LFAM': 'BERCK SUR MER', 'LFAO': "BAGNOLES DE L'ORNE COUTERNE", 'LFAP': 'RETHEL PERTHES', 'LFAQ': 'ALBERT BRAY', 'LFAR': 'MONTDIDIER', 'LFAS': "FALAISE MONTS D'ERAINES", 'LFAT': "LE TOUQUET COTE D'OPALE", 'LFAU': 'VAUVILLE', 'LFAV': 'VALENCIENNES DENAIN', 'LFAW': 'VILLERUPT', 'LFAX': 'MORTAGNE AU PERCHE', 'LFAY': 'AMIENS-GLISY', 'LFBA': 'AGEN LA GARENNE', 'LFBC': 'CAZAUX', 'LFBD': 'BORDEAUX MERIGNAC', 'LFBE': 'BERGERAC DORDOGNE PERIGORD', 'LFBF': 'TOULOUSE FRANCAZAL', 'LFBG': 'COGNAC CHATEAUBERNARD', 'LFBH': 'LA ROCHELLE ILE DE RE', 'LFBI': 'POITIERS BIARD', 'LFBJ': 'SAINT JUNIEN', 'LFBK': 'MONTLUCON GUERET', 'LFBL': 'LIMOGES BELLEGARDE', 'LFBM': 'MONT DE MARSAN', 'LFBN': 'NIORT MARAIS POITEVIN', 'LFBO': 'TOULOUSE BLAGNAC', 'LFBP': 'PAU PYRENEES', 'LFBR': 'MURET LHERM', 'LFBS': 'BISCARROSSE PARENTIS', 'LFBT': 'TARBES LOURDES PYRENEES', 'LFBU': 'ANGOULEME BRIE CHAMPNIERS', 'LFBX': 'PERIGUEUX BASSILLAC', 'LFBY': 'DAX SEYRESSE', 'LFBZ': 'BIARRITZ PAYS BASQUE', 'LFCA': 'CHATELLERAULT TARGE', 'LFCB': 'BAGNERES DE LUCHON', 'LFCC': 'CAHORS LALBENQUE', 'LFCD': 'ANDERNOS LES BAINS', 'LFCE': 'GUERET SAINT LAURENT', 'LFCF': 'FIGEAC LIVERNON', 'LFCG': 'SAINT GIRONS ANTICHAN', 'LFCH': 'ARCACHON LA TESTE DE BUCH', 'LFCI': 'ALBI LE SEQUESTRE', 'LFCJ': 'JONZAC NEULLES', 'LFCK': 'CASTRES MAZAMET', 'LFCL': 'TOULOUSE LASBORDES', 'LFCM': 'MILLAU LARZAC', 'LFCN': 'NOGARO', 'LFCO': 'OLORON HERRERE', 'LFCP': 'PONS AVY', 'LFCQ': 'GRAULHET MONTDRAGON', 'LFCR': 'RODEZ AVEYRON', 'LFCS': 'BORDEAUX LEOGNAN SAUCATS', 'LFCT': 'THOUARS', 'LFCU': 'USSEL THALAMY', 'LFCV': 'VILLEFRANCHE DE ROUERGUE', 'LFCW': 'VILLENEUVE SUR LOT', 'LFCX': 'CASTELSARRASIN MOISSAC', 'LFCY': 'ROYAN MEDIS', 'LFCZ': 'MIMIZAN', 'LFDA': "AIRE SUR L'ADOUR", 'LFDB': 'MONTAUBAN', 'LFDC': 'MONTENDRE MARCILLAC', 'LFDE': 'EGLETONS', 'LFDF': 'SAINTE FOY LA GRANDE', 'LFDG': 'GAILLAC LISLE SUR TARN', 'LFDH': 'AUCH GERS', 'LFDI': 'LIBOURNE ARTIGUES DE LUSSAC', 'LFDJ': 'PAMIERS LES PUJOLS', 'LFDK': 'SOULAC SUR MER', 'LFDL': 'LOUDUN', 'LFDM': 'MARMANDE VIRAZEIL', 'LFDN': 'ROCHEFORT CHARENTE MARITIME', 'LFDP': "SAINT PIERRE D'OLERON", 'LFDQ': 'CASTELNAU MAGNOAC', 'LFDR': 'LA REOLE FLOUDES', 'LFDS': 'SARLAT DOMME', 'LFDT': 'TARBES LALOUBERE', 'LFDU': 'LESPARRE SAINT LAURENT MEDOC', 'LFDV': 'COUHE VERAC', 'LFDW': 'CHAUVIGNY', 'LFDX': 'FUMEL MONTAYRAL', 'LFDY': 'BORDEAUX YVRAC', 'LFEA': 'BELLE ILE', 'LFEB': 'DINAN TRELIVAN', 'LFEC': 'OUESSANT', 'LFED': 'PONTIVY', 'LFEF': 'AMBOISE DIERRE', 'LFEG': 'ARGENTON SUR CREUSE', 'LFEH': 'AUBIGNY SUR NERE', 'LFEI': 'BRIARE CHATILLON', 'LFEJ': 'CHATEAUROUX VILLERS', 'LFEK': 'ISSOUDUN LE FAY', 'LFEL': 'LE BLANC', 'LFEM': 'MONTARGIS VIMORY', 'LFEN': 'TOURS SORIGNY', 'LFEP': 'POUILLY MACONGE', 'LFEQ': 'QUIBERON', 'LFER': 'REDON BAINS SUR OUST', 'LFES': 'GUISCRIFF SCAER', 'LFET': 'TIL CHATEL', 'LFEU': 'BAR LE DUC LES HAUTS DE CHEE', 'LFEV': 'GRAY SAINT ADRIEN', 'LFEW': 'SAULIEU LIERNAIS', 'LFEX': 'NANCY AZELOT', 'LFEY': "ILE D'YEU", 'LFEZ': 'NANCY MALZEVILLE', 'LFFB': 'BUNO BONNEVAUX', 'LFFC': 'MANTES CHERENCE', 'LFFD': "SAINT ANDRE DE L'EURE", 'LFFE': 'ENGHIEN MOISSELLES', 'LFFG': 'LA FERTE GAUCHER', 'LFFH': 'CHATEAU THIERRY BELLEAU', 'LFFI': 'ANCENIS', 'LFFJ': 'JOINVILLE MUSSEY', 'LFFK': 'FONTENAY LE COMTE', 'LFFL': 'BAILLEAU ARMENONVILLE', 'LFFN': 'BRIENNE LE CHATEAU', 'LFFO': 'BEAUVOIR FROMENTINE', 'LFFP': 'PITHIVIERS', 'LFFQ': 'LA FERTE ALAIS', 'LFFR': 'BAR SUR SEINE', 'LFFT': 'NEUFCHATEAU', 'LFFU': 'CHATEAUNEUF SUR CHER', 'LFFV': 'VIERZON MEREAU', 'LFFW': 'MONTAIGU SAINT GEORGES', 'LFFX': 'TOURNUS CUISERY', 'LFFY': 'ETREPAGNY', 'LFFZ': 'SEZANNE SAINT REMY', 'LFGA': 'COLMAR HOUSSEN', 'LFGB': 'MULHOUSE HABSHEIM', 'LFGC': 'STRASBOURG NEUHOF', 'LFGE': 'AVALLON', 'LFGF': 'BEAUNE CHALLANGES', 'LFGG': 'BELFORT CHAUX', 'LFGH': 'COSNE SUR LOIRE', 'LFGI': 'DIJON DAROIS', 'LFGJ': 'DOLE TAVAUX', 'LFGK': 'JOIGNY', 'LFGL': 'LONS LE SAUNIER COURLAOUX', 'LFGM': 'MONTCEAU LES MINES POUILLOUX', 'LFGN': 'PARAY LE MONIAL', 'LFGO': 'PONT SUR YONNE', 'LFGP': 'SAINT FLORENTIN CHEU', 'LFGQ': 'SEMUR EN AUXOIS', 'LFGR': 'DONCOURT LES CONFLANS', 'LFGS': 'LONGUYON VILLETTE', 'LFGT': 'SARREBOURG BUHL', 'LFGU': 'SARREGUEMINES NEUNKIRCH', 'LFGW': 'VERDUN SOMMEDIEUE', 'LFGX': 'CHAMPAGNOLE CROTENAY', 'LFGY': 'SAINT DIE REMOMEIX', 'LFGZ': 'NUITS SAINT GEORGES', 'LFHA': 'ISSOIRE LE BROC', 'LFHB': 'BISCARROSSE HYDROBASE', 'LFHC': 'PEROUGES MEXIMIEUX', 'LFHD': 'PIERRELATTE', 'LFHE': 'ROMANS SAINT PAUL', 'LFHF': 'RUOMS', 'LFHG': "SAINT CHAMOND L'HORME", 'LFHH': 'VIENNE REVENTIN', 'LFHI': 'MORESTEL', 'LFHJ': 'LYON CORBAS', 'LFHL': 'LANGOGNE LESPERON', 'LFHM': 'MEGEVE', 'LFHN': 'BELLEGARDE VOUVRAY', 'LFHO': 'AUBENAS ARDECHE MERIDIONALE', 'LFHP': 'LE PUY LOUDES', 'LFHQ': 'SAINT FLOUR COLTINES', 'LFHR': 'BRIOUDE BEAUMONT', 'LFHS': 'BOURG CEYZERIAT', 'LFHT': 'AMBERT LE POYET', 'LFHU': "L'ALPE D'HUEZ", 'LFHV': 'VILLEFRANCHE TARARE', 'LFHW': 'BELLEVILLE VILLIE MORGON', 'LFHX': 'LAPALISSE PERIGNY', 'LFHY': 'MOULINS MONTBEUGNY', 'LFIB': 'BELVES SAINT PARDOUX', 'LFID': 'CONDOM VALENCE SUR BAISE', 'LFIF': 'SAINT AFFRIQUE BELMONT', 'LFIG': 'CASSAGNES BEGONHES', 'LFIH': 'CHALAIS', 'LFIK': 'RIBERAC-TOURETTE', 'LFIL': 'RION DES LANDES', 'LFIM': 'SAINT GAUDENS MONTREJEAU', 'LFIP': 'PEYRESOURDE BALESTAS', 'LFIR': 'REVEL MONTGEY', 'LFIS': 'SAINT INGLEVERT LES DEUX CAPS', 'LFIT': 'TOULOUSE BOURG SAINT BERNARD', 'LFIV': 'VENDAYS MONTALIVET', 'LFIX': 'ITXASSOU', 'LFIY': "SAINT JEAN D'ANGELY SAINT DENIS DU PIN", 'LFJA': 'CHAUMONT SEMOUTIERS', 'LFJB': 'MAULEON', 'LFJC': 'CLAMECY', 'LFJD': 'CORLIER', 'LFJF': 'AUBENASSON', 'LFJH': 'CAZERES PALAMINY', 'LFJI': 'MARENNES', 'LFJL': 'METZ NANCY LORRAINE', 'LFJR': 'ANGERS MARCE', 'LFJS': 'SOISSONS COURMELLES', 'LFJT': 'TOURS LE LOUROUX', 'LFJU': 'LURCY LEVIS', 'LFJV': 'LASCLAVERIES', 'LFJY': 'CHAMBLEY', 'LFKA': 'ALBERTVILLE GENERAL PIERRE DELACHENAL', 'LFKB': 'BASTIA PORETTA', 'LFKC': 'CALVI SAINTE CATHERINE', 'LFKD': 'SOLLIERES SARDIERES', 'LFKE': 'SAINT JEAN EN ROYANS', 'LFKF': 'FIGARI SUD CORSE', 'LFKG': 'GHISONACCIA ALZITONE', 'LFKH': "SAINT JEAN D'AVELANNE", 'LFKJ': 'AJACCIO NAPOLEON BONAPARTE', 'LFKK': 'MONTMEILLEUR', 'LFKL': 'LYON BRINDAS', 'LFKM': 'SAINT GALMIER', 'LFKO': 'PROPRIANO', 'LFKP': 'LA TOUR DU PIN CESSIEU', 'LFKR': 'SAINT REMY DE MAURIENNE', 'LFKS': 'SOLENZARA', 'LFKT': 'CORTE', 'LFKX': 'MERIBEL ROBERT MERLOZ', 'LFKY': 'BELLEY-PEYRIEU', 'LFLA': 'AUXERRE BRANCHES', 'LFLB': 'CHAMBERY AIX LES BAINS', 'LFLC': 'CLERMONT FERRAND AUVERGNE', 'LFLD': 'BOURGES', 'LFLE': 'CHAMBERY CHALLES LES EAUX', 'LFLG': 'GRENOBLE LE VERSOUD', 'LFLH': 'CHALON CHAMPFORGEUIL', 'LFLI': 'ANNEMASSE', 'LFLJ': 'COURCHEVEL', 'LFLK': 'OYONNAX ARBENT', 'LFLL': 'LYON SAINT EXUPERY', 'LFLM': 'MACON CHARNAY', 'LFLN': 'SAINT YAN', 'LFLO': 'ROANNE', 'LFLP': 'ANNECY MEYTHET', 'LFLQ': 'MONTELIMAR ANCONE', 'LFLR': "SAINT RAMBERT D'ALBON", 'LFLS': 'GRENOBLE ALPES ISERE', 'LFLT': 'MONTLUCON DOMERAT', 'LFLU': 'VALENCE CHABEUIL', 'LFLV': 'VICHY CHARMEIL', 'LFLW': 'AURILLAC', 'LFLX': 'CHATEAUROUX DEOLS', 'LFLY': 'LYON BRON', 'LFLZ': 'FEURS CHAMBEON', 'LFMA': 'AIX LES MILLES', 'LFMC': 'LE LUC LE CANNET', 'LFMD': 'CANNES MANDELIEU', 'LFME': 'NIMES COURBESSAC', 'LFMF': 'FAYENCE', 'LFMG': 'MONTAGNE NOIRE', 'LFMH': 'SAINT ETIENNE LOIRE', 'LFMI': 'ISTRES LE TUBE', 'LFMK': 'CARCASSONNE SALVAZA', 'LFML': 'MARSEILLE PROVENCE', 'LFMN': "NICE COTE D'AZUR", 'LFMO': 'ORANGE CARITAT', 'LFMP': 'PERPIGNAN RIVESALTES', 'LFMQ': 'LE CASTELLET', 'LFMR': 'BARCELONNETTE SAINT PONS', 'LFMS': 'ALES CEVENNES', 'LFMT': 'MONTPELLIER MEDITERRANEE', 'LFMU': 'BEZIERS VIAS', 'LFMV': 'AVIGNON CAUMONT', 'LFMW': 'CASTELNAUDARY VILLENEUVE', 'LFMX': 'CHATEAU ARNOUX SAINT AUBAN', 'LFMY': 'SALON DE PROVENCE', 'LFMZ': 'LEZIGNAN CORBIERES', 'LFNA': 'GAP TALLARD', 'LFNB': 'MENDE BRENOUX', 'LFNC': 'MONT DAUPHIN SAINT CREPIN', 'LFNE': 'SALON EYGUIERES', 'LFNF': 'VINON', 'LFNG': 'MONTPELLIER CANDILLARGUES', 'LFNH': 'CARPENTRAS', 'LFNJ': 'ASPRES SUR BUECH', 'LFNL': 'SAINT MARTIN DE LONDRES', 'LFNN': 'NARBONNE', 'LFNO': 'FLORAC SAINTE ENIMIE', 'LFNQ': 'LA LLAGONNE LA QUILLANE', 'LFNR': 'BERRE LA FARE', 'LFNS': 'SISTERON VAUMEILH', 'LFNT': 'AVIGNON PUJAUT', 'LFNU': 'UZES', 'LFNV': 'VALREAS VISAN', 'LFNW': 'PUIVERT', 'LFNX': 'BEDARIEUX LA TOUR SUR ORB', 'LFNZ': 'LE MAZET DE ROMANIN', 'LFOA': 'AVORD', 'LFOB': 'BEAUVAIS TILLE', 'LFOC': 'CHATEAUDUN', 'LFOD': 'SAUMUR SAINT FLORENT', 'LFOE': 'EVREUX FAUVILLE', 'LFOF': 'ALENCON VALFRAMBERT', 'LFOG': 'FLERS SAINT PAUL', 'LFOH': 'LE HAVRE OCTEVILLE', 'LFOI': 'ABBEVILLE', 'LFOJ': 'ORLEANS BRICY', 'LFOK': 'CHALONS VATRY', 'LFOL': "L'AIGLE SAINT MICHEL", 'LFOM': 'LESSAY', 'LFON': 'DREUX VERNOUILLET', 'LFOO': "LES SABLES D'OLONNE TALMONT", 'LFOP': 'ROUEN VALLEE DE SEINE', 'LFOQ': 'BLOIS LE BREUIL', 'LFOR': 'CHARTRES METROPOLE', 'LFOS': 'SAINT VALERY VITTEFLEUR', 'LFOT': 'TOURS VAL DE LOIRE', 'LFOU': 'CHOLET LE PONTREAU', 'LFOV': 'LAVAL ENTRAMMES', 'LFOW': 'SAINT QUENTIN ROUPY', 'LFOX': 'ETAMPES MONDESIR', 'LFOY': 'LE HAVRE SAINT ROMAIN', 'LFOZ': "ORLEANS SAINT DENIS DE L'HOTEL", 'LFPA': 'PERSAN BEAUMONT', 'LFPB': 'PARIS LE BOURGET', 'LFPD': 'BERNAY SAINT MARTIN', 'LFPE': 'MEAUX ESBLY', 'LFPF': 'BEYNES THIVERVAL', 'LFPG': 'PARIS CHARLES DE GAULLE', 'LFPH': 'CHELLES LE PIN', 'LFPK': 'COULOMMIERS VOISINS', 'LFPL': 'LOGNES EMERAINVILLE', 'LFPM': 'MELUN VILLAROCHE', 'LFPN': 'TOUSSUS LE NOBLE', 'LFPO': 'PARIS ORLY', 'LFPP': 'LE PLESSIS BELLEVILLE', 'LFPQ': 'FONTENAY TRESIGNY', 'LFPR': 'ORANGE PLAN DE DIEU', 'LFPT': 'PONTOISE CORMEILLES EN VEXIN', 'LFPU': 'MORET EPISY', 'LFPV': 'VILLACOUBLAY VELIZY', 'LFPX': 'CHAVENAY VILLEPREUX', 'LFPZ': "SAINT CYR L'ECOLE", 'LFQA': 'REIMS PRUNAY', 'LFQB': 'TROYES BARBEREY', 'LFQC': 'LUNEVILLE CROISMARE', 'LFQD': 'ARRAS ROCLINCOURT', 'LFQE': 'ETAIN ROUVRES', 'LFQF': 'AUTUN BELLEVUE', 'LFQG': 'NEVERS FOURCHAMBAULT', 'LFQH': 'CHATILLON SUR SEINE', 'LFQJ': 'MAUBEUGE ELESMES', 'LFQK': 'CHALONS ECURY SUR COOLE', 'LFQL': 'LENS BENIFONTAINE', 'LFQM': 'BESANCON LA VEZE', 'LFQN': 'SAINT OMER WIZERNES', 'LFQO': 'LILLE MARCQ EN BAROEUL', 'LFQP': 'PHALSBOURG BOURSCHEID', 'LFQQ': 'LILLE LESQUIN', 'LFQS': 'VITRY EN ARTOIS', 'LFQT': 'MERVILLE CALONNE', 'LFQU': 'SARRE UNION', 'LFQV': 'CHARLEVILLE MEZIERES', 'LFQW': 'VESOUL FROTEY', 'LFQX': 'JUVANCOURT', 'LFQY': 'SAVERNE STEINBOURG', 'LFQZ': 'DIEUZE GUEBLANGE', 'LFRB': 'BREST BRETAGNE', 'LFRC': 'CHERBOURG MANCHE', 'LFRD': 'DINARD PLEURTUIT SAINT MALO', 'LFRE': 'LA BAULE ESCOUBLAC', 'LFRF': 'GRANVILLE-MONT SAINT MICHEL', 'LFRG': 'DEAUVILLE NORMANDIE', 'LFRH': 'LORIENT LANN BIHOUE', 'LFRI': 'LA ROCHE SUR YON LES AJONCS', 'LFRJ': 'LANDIVISIAU', 'LFRK': 'CAEN CARPIQUET', 'LFRL': 'LANVEOC POULMIC', 'LFRM': 'LE MANS ARNAGE', 'LFRN': 'RENNES SAINT JACQUES', 'LFRO': 'LANNION', 'LFRP': 'PLOERMEL LOYAT', 'LFRQ': 'QUIMPER PLUGUFFAN', 'LFRS': 'NANTES ATLANTIQUE', 'LFRT': 'SAINT BRIEUC ARMOR', 'LFRU': 'MORLAIX PLOUJEAN', 'LFRV': 'VANNES MEUCON', 'LFRW': 'AVRANCHES LE VAL SAINT PERE', 'LFRZ': 'SAINT NAZAIRE MONTOIR', 'LFSA': 'BESANCON THISE', 'LFSB': 'BALE-MULHOUSE', 'LFSC': 'COLMAR-MEYENHEIM', 'LFSD': 'DIJON-LONGVIC', 'LFSE': 'EPINAL DOGNEVILLE', 'LFSG': 'EPINAL MIRECOURT', 'LFSH': 'HAGUENAU', 'LFSI': 'SAINT DIZIER ROBINSON', 'LFSJ': 'SEDAN DOUZY', 'LFSK': 'VITRY LE FRANCOIS VAUCLERC', 'LFSL': 'BRIVE SOUILLAC', 'LFSM': 'MONTBELIARD COURCELLES', 'LFSN': 'NANCY ESSEY', 'LFSO': 'NANCY OCHEY', 'LFSP': 'PONTARLIER', 'LFSQ': 'BELFORT FONTAINE (CLOSED)', 'LFSS': 'SAINT SULPICE DES LANDES', 'LFST': 'STRASBOURG ENTZHEIM', 'LFSU': 'LANGRES ROLAMPONT', 'LFSV': 'PONT SAINT VINCENT', 'LFSW': 'EPERNAY PLIVOT', 'LFSX': 'LUXEUIL SAINT SAUVEUR', 'LFTB': 'MARIGNANE BERRE', 'LFTF': 'CUERS PIERREFEU', 'LFTH': 'HYERES LE PALYVESTRE', 'LFTM': 'SERRES LA BATIE MONTSALEON', 'LFTN': "LA GRAND'COMBE", 'LFTP': 'PUIMOISSON', 'LFTQ': 'CHATEAUBRIANT POUANCE', 'LFTW': 'NIMES GARONS', 'LFTZ': 'LA MOLE', 'LFXA': 'AMBERIEU', 'LFXB': 'SAINTES THENAC', 'LFXQ': 'COETQUIDAN', 'LFXU': 'LES MUREAUX', 'LFYG': 'CAMBRAI NIERGNIES', 'LFYR': 'ROMORANTIN PRUNIERS', 'LFYS': 'SAINTE LEOCADIE', 'LFYV': 'YVETOT-BAONS LE COMTE', 'LSGG': 'GENEVE', 'NLWF': 'FUTUNA POINTE VELE', 'NLWW': 'WALLIS HIHIFO', 'NT01': 'ARATIKA PERLES (CLOSED)', 'NTAA': "TAHITI FAA'A", 'NTAM': 'RIMATARA', 'NTAR': 'RURUTU', 'NTAT': 'TUBUAI MATAURA', 'NTAV': 'RAIVAVAE', 'NTGA': 'ANAA', 'NTGB': 'FANGATAU', 'NTGC': 'TIKEHAU', 'NTGD': 'APATAKI', 'NTGE': 'REAO', 'NTGF': 'FAKARAVA', 'NTGH': 'HIKUERU', 'NTGI': 'MANIHI', 'NTGJ': 'TOTEGEGIE', 'NTGK': 'KAUKURA', 'NTGM': 'MAKEMO', 'NTGN': 'NAPUKA', 'NTGO': 'TATAKOTO', 'NTGP': 'PUKA PUKA', 'NTGQ': 'PUKARUA', 'NTGT': 'TAKAPOTO', 'NTGU': 'ARUTUA', 'NTGV': 'MATAIVA', 'NTGW': 'NUKUTAVAKE', 'NTGY': 'TUREIA', 'NTHE': 'AHE', 'NTKA': 'KAUEHI', 'NTKF': 'FAAITE', 'NTKH': 'FAKAHINA', 'NTKK': 'ARATIKA NORD', 'NTKM': 'TAKUME', 'NTKN': 'NIAU', 'NTKO': 'RAROIA', 'NTKR': 'TAKAROA', 'NTKT': 'KATIU', 'NTKU': 'NUKUTEPIPI', 'NTMD': 'NUKU HIVA', 'NTMN': 'HIVA OA ATUONA', 'NTMP': 'UA POU', 'NTMU': 'UA HUKA', 'NTTB': 'BORA BORA MOTU MUTE', 'NTTE': 'TETIAROA', 'NTTG': 'RANGIROA', 'NTTH': 'HUAHINE FARE', 'NTTM': 'MOOREA TEMAE', 'NTTO': 'HAO', 'NTTP': 'MAUPITI', 'NTTR': 'RAIATEA UTUROA', 'NTTU': 'TUPAI', 'NTUV': 'VAHITAHI', 'NW01': 'POUM MALABOU (CLOSED)', 'NWWA': 'TIGA', 'NWWB': 'BOURAIL POE', 'NWWC': 'ILE ART WAALA', 'NWWD': 'KONE', 'NWWE': 'ILE DES PINS MOUE', 'NWWK': 'KOUMAC', 'NWWL': 'LIFOU OUANAHAM', 'NWWM': 'NOUMEA MAGENTA', 'NWWR': 'MARE LA ROCHE', 'NWWT': 'LA FOA OUA TOM', 'NWWU': 'TOUHO', 'NWWV': 'OUVEA OULOUP', 'NWWW': 'NOUMEA LA TONTOUTA', 'NWWX': 'CANALA', 'SOCA': 'CAYENNE FELIX EBOUE', 'SOGS': 'GRAND SANTI', 'SOOA': 'MARIPASOULA', 'SOOC': 'CAMOPI', 'SOOG': "SAINT GEORGES DE L'OYAPOCK", 'SOOM': 'SAINT LAURENT DU MARONI', 'SOOR': 'REGINA', 'SOOS': 'SAUL', 'TFFA': 'DESIRADE GRANDE ANSE', 'TFFB': 'BASSE TERRE BAILLIF', 'TFFC': 'SAINT FRANCOIS', 'TFFF': 'MARTINIQUE AIME CESAIRE', 'TFFG': "SAINT MARTIN GRAND'CASE", 'TFFJ': 'SAINT BARTHELEMY', 'TFFM': 'MARIE GALANTE', 'TFFR': 'POINTE A PITRE LE RAIZET', 'TFFS': 'LES SAINTES TERRE DE HAUT', 'ZZSL': 'TOUL ROSIERES (CLOSED)', 'lfVM': 'MIQUELON', 'lfVP': 'SAINT PIERRE'}
populateDropdowns();
var text = 'Click on the submit button to get your weather briefing..'
var utterance = new SpeechSynthesisUtterance(text);
utterance.lang = 'en-US';
function toggleButton() {
    // Change the color when the button is clicked
    var button = document.getElementById("submitButton");
    var processing = document.getElementById('processingText')
    const resultDiv = document.getElementById("result");
    if (button.disabled) {
        button.disabled = false;
        button.style.backgroundColor = "green";
        processing.style.display = 'none';

    } else {
        button.disabled = true;
        button.style.backgroundColor = "gray";
        processing.style.display = 'inline';
        resultDiv.innerHTML='';
        stop();
    }

}


    function populateDropdowns() {
    const originSelect = document.getElementById("origin");
    const destinationSelect = document.getElementById("destination");
    for (const code in airports) {
        const option = document.createElement("option");
        option.value = code;
        option.text = code+" - "+airports[code];
        option.setAttribute("option", code)
        originSelect.add(option.cloneNode(true));
        destinationSelect.add(option);
    }
    document.getElementById("origin").value = "LFPX";  //the desired default value
    document.getElementById("destination").value = "LFPX";  //the desired default value
}

function submitSelection() {
    const originSelect = document.getElementById("origin");
    const destinationSelect = document.getElementById("destination");
    const resultDiv = document.getElementById("result");
    const originCode = originSelect.value;
    const destinationCode = destinationSelect.value;
    var apiUrl = `https://briefer.amenai.net/brief?flightpath=${originCode},${destinationCode}`;
    fetch(apiUrl)
        .then(response => {
                            if (!response.ok) {
                                throw new Error('Network response was not ok');
                            }
                            return response.text();
        })
        .then(data => {
            resultDiv.innerHTML = `Result: <a href="${data}" target="_blank">View Plaintext Briefing</a>`;
            toggleButton();
            return fetch(data);
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.text();
        })
        .then(responseText => {
            text = responseText;
            readText()
        })
        .catch(error => {
            console.error('Error fetching and reading text:', error);
            toggleButton();
        });
        toggleButton()
}

function readText() {
    if (speechSynthesis.paused){
        speechSynthesis.resume()
    }
    else {
        utterance.text = text;
        utterance.lang = 'en-US';
        speechSynthesis.speak(utterance);
    }
}

function pauseSpeech() {
      if (speechSynthesis.speaking) {
        speechSynthesis.pause();
        isPaused = true;
        pausedAt = utterance.elapsedTime;
      }
}
function stop() {
      speechSynthesis.cancel();
      isPaused = false;
      pausedAt = 0;
}

function filterDropdown(id,dropId) {
        // Get the input value
        var input, filter, select, options, i, txtValue;
        input = document.getElementById(id);
        filter = input.value.toUpperCase();
        select = document.getElementById(dropId);
        options=select.querySelectorAll("option");
        //options = select.getElementsByTagName("option");
        // Loop through all dropdown options, and hide those that don't match the search
        for (i = 0; i < options.length; i++) {
            txtValue = options[i].text || options[i].value;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                options[i].style.display = "";
            } else {
                options[i].style.display = "none";
            }
        }
        // Programmatically trigger 'change' event on the first visible option
        var visibleOption = select.querySelector("option[style='']");
        if (visibleOption) {
            visibleOption.selected = true;
        visibleOption.dispatchEvent(new Event('change', { bubbles: true, cancelable: true }));
        }
    }
