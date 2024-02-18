from unittest import TestCase

from wxflightpath.zoneFilter import *


class TestZoneFilter(TestCase):
    airport_List = getAirfieldsInFlightPath()
    def test_init(self):
        self.assertEqual(self.airport_List,['LFPT',
 'LFRU',
 'LFPN',
 'LFPV',
 'LFOB',
 'LFPB',
 'LFPO',
 'LFPC',
 'LFPG',
 'LFPY',
 'LFPM',
 'LFOR',
 'LFOE',
 'LFOP',
 'LFAQ',
 'LFRD',
 'LFRT',
 'LFRO',
 'LFRJ',
 'LFRQ',
 'LFRB',
 'LFRL']
)

