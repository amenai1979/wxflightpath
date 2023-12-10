from unittest import TestCase
from wxflightpath.geoTools import *


class TestgeoCoordinate(TestCase):
    paris = geoCoordinate(48.8752778, 2.1644444444444444)
    def test_init(self):
        self.assertEqual(self.paris.long, 2.1644444444444444)
        self.assertEqual(self.paris.lat, 48.8752778)

    def test__str__(self):
        self.assertEqual(str(self.paris), "latitude: 48.8752778 longitude: 2.1644444444444444")


class TestbipolarGeoZone(TestCase):
    paris = geoCoordinate(48.8752778, 2.1644444444444444)
    morlaix = geoCoordinate(48.58333, -3.83333)
    contour = bipolarGeoZone(paris, morlaix).setContour()
    def test_set_contour(self):
        self.assertEqual(len(self.contour),4)
        self.assertEqual(type(self.contour[0]), geoCoordinate)
        self.assertLess(self.contour[1].lat, self.contour[0].lat)
        self.assertEqual(self.contour[1].long, self.contour[0].long)
        self.assertLess(self.contour[1].long, self.contour[2].long)
        self.assertEqual(self.contour[2].long, self.contour[3].long)
        self.assertLess(self.contour[3].lat, self.contour[2].lat)

class TestgeoZone(TestCase):
    paris = geoCoordinate(48.8752778, 2.1644444444444444)
    morlaix = geoCoordinate(48.58333, -3.83333)
    contour = bipolarGeoZone(paris, morlaix).setContour()
    flightZone = geoZone(contour)
    def test_geoZone(self):
        #self.assertEqual(self.flightZone.contains(self.paris),True)
        #self.assertEqual(self.flightZone.contains(self.morlaix), True)
        self.assertEqual(self.flightZone.contains(self.contour[0]), False)
        self.assertEqual(self.flightZone.contains(self.contour[1]), False)
        self.assertEqual(self.flightZone.contains(self.contour[2]), False)
        self.assertEqual(self.flightZone.contains(self.contour[3]), False)


