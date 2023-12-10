from unittest import TestCase

from wxflightpath.zoneFilter import *


class TestZoneFilter(TestCase):
    aerodromes_file = "../data/XML_SIA_2023-10-05.xml"
    airport_List = getAirfieldsInFlightPath(aerodromes_file=aerodromes_file)
    def test_init(self):
        self.assertEqual(self.airport_List,
                         ['LFPA','LFPE','LFPD','LFPB','LFOX','LFPP','LFPQ','LFPN','LFPO','LFPT','LFPU','LFPH','LFPF','LFPG','LFPL','LFPM','LFPK','LFOB','LFON','LFOP','LFOR','LFOE','LFOL','LFXU','LFRL','LFRO','LFRJ','LFRU','LFRT','LFRQ','LFRD','LFRF','LFRB','LFPZ','LFPX','LFPV','LFFB','LFFC','LFFD','LFFE','LFES','LFFQ','LFFL','LFFY','LFAD','LFAY','LFAQ','LFAR','LFAS','LFAG','LFAI','LFAJ'])

