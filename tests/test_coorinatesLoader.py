from unittest import TestCase

from wxflightpath.coordinatesLoader import *


class TestcoordinatesLoader(TestCase):
    frenchAirports = aerodromesDict()
    def test_init(self):
        self.assertEqual(self.frenchAirports.ADict["LFRO"].lat, 48.754444)
        self.assertEqual(self.frenchAirports.ADict["LFRO"].long, -3.471944)
        self.assertEqual(self.frenchAirports.ADictNames["LFRO"], "LANNION")
