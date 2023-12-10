from unittest import TestCase
from wxflightpath.wxcrawler import *
class TestWxcrawler(TestCase):
    #aerodromes_file = "../data/XML_SIA_2023-10-05.xml"
    crawler = Wxcrawler(config=config,secret=config['SECURITY']['TOKEN'])
    result1 = crawler.getObservationWX("LFPT")
    result2 = crawler.getForecastWX("LFPG")
    def test_init(self):
        self.assertEqual(len(self.result1), 5)
        self.assertEqual(self.result1[4], 'LFPT')
        self.assertEqual(len(self.result2),3)


