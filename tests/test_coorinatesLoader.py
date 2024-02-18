from unittest import TestCase

from wxflightpath.coordinatesLoader import *


class TestcoordinatesLoader(TestCase):
    frenchAirports = aerodromesDict()
    def test_init(self):
        self.assertEqual(self.frenchAirports.ADict["LFRO"].lat, 48.7543983459)
        self.assertEqual(self.frenchAirports.ADict["LFRO"].long, -3.4716598988)
        self.assertEqual(self.frenchAirports.ADictNames["LFRO"], "Lannion-Cote de Granit")
