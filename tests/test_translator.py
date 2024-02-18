from unittest import TestCase
from wxflightpath.wxcrawler import *
class TestOaiTranslator(TestCase):
    totranslate = "This is the weather Forecast for Lima Foxtrot Oscar Papa Rouen . Starting on February 18th - From 6 to 6 zulu, Winds two zero zero at 10 knots. Visibility one zero kilometers. Broken layer at 3000ft. Overcast layer at 6000ft. At 9 zulu becoming Visibility four kilometers. Light Rain. Broken layer at 1200ft. Overcast layer at 2000ft. From 9 to 12 zulu, temporary Visibility two point five kilometers. Rain. Broken layer at 400ft. Overcast layer at 800ft. From 12 to 15 zulu, Winds two six zero at 10 knots. Visibility one zero kilometers. Broken layer at 600ft. Overcast layer at 1400ft. From 13 to 15 zulu, temporary Visibility one point five kilometers. Rain Drizzle. Broken layer at 200ft. Overcast layer at 400ft"
    expectedresult =("Il s'agit de la prévision météorologique pour Lima Foxtrot Oscar Papa "
 'Rouen..à partir du 18 février.De 6 à 6 zulu.vents deux zéro zéro à 10 '
 'nœuds.visibilité de dix kilomètres.couche brisée à 3000 pieds.couche '
 'nuageuse à 6000 pieds.à 9 zulu.devenant.visibilité de quatre '
 'kilomètres.pluie légère.couche brisée à 1200 pieds..couche nuageuse à 2000 '
 'pieds.De 9 à 12 zulu.visibilité temporaire de deux virgule cinq '
 'kilomètres.pluie.couche brisée à 400 pieds.couche nuageuse à 800 pieds.De 12 '
 'à 15 heures en temps universel coordonné (UTC).vents deux six zéro à 10 '
 'nœuds.visibilité de dix kilomètres.couche brisée à 600 pieds.couche nuageuse '
 'à 1400 pieds.De 13 à 15 heures en temps universel coordonné '
 "(ZULU)..visibilité temporaire d'un kilomètre et demi.pluie fine.couche "
 'brisée à 200 pieds.couche nuageuse à 400 pieds')
    def test_init(self):
        self.assertEqual(translate(input=self.totranslate, lang='fr'), self.expectedresult)