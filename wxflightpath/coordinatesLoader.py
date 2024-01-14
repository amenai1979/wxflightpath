import json
import logging

import xmltodict

from wxflightpath import config
from wxflightpath import geoTools


class aerodromesDict:
    aerodromes = []
    ADict = {}
    ADictNames = {}

    def __init__(self):
        try:
            with open(config['DATA']['ADICT_FILE'], 'r') as json_file:
                self.ADict = json.load(json_file, object_hook=geoTools.geoCoordinateDecoder)
            with open(config['DATA']['ADICTNAMES_FILE'], 'r') as json_file:
                self.ADictNames = json.load(json_file)
            logging.info("Successfully loaded aerodromes dict from serialized json files %s and %s",
                         config['DATA']['ADICT_FILE'], config['DATA']['ADICTNAMES_FILE'])
        except Exception as e:
            logging.error(
                "failed to load serialized aerodromes data from %s and %s , attempting the hard way (loading from xml file). details : %s ",
                config['DATA']['ADICT_FILE'], config['DATA']['ADICTNAMES_FILE'], e)
            self.loadFromFile()
            # serialize for next time
            self.serialize_to_json()
            pass

    def loadFromFile(self, aerodromes_file=config['DATA']['AERODROMES_FILE']):
        try:
            self.aerodromes_file = aerodromes_file
            with open(self.aerodromes_file, 'r', encoding='ISO-8859-1') as xml_file:
                # Parse the XML data into a Python dictionary
                xml_data = xmltodict.parse(xml_file.read())
                self.aerodromes = xml_data['SiaExport']['Situation']['AdS']['Ad']
                self.loadAerodromesDict()
        except Exception as e:
            logging.error("failed to load from xml file. details : %s", e)

    def loadAerodromesDict(self):
        for x in range(0, len(self.aerodromes)):
            key = str(self.aerodromes[x]['@lk']).replace("[", "").replace(']', "")
            name = str(self.aerodromes[x]['AdNomComplet'])
            self.ADict[key] = geoTools.geoCoordinate(float(self.aerodromes[x]['ArpLat']),
                                                     float(self.aerodromes[x]['ArpLong']))
            self.ADictNames[key] = name

    def prettyPrint(self):
        dictPrint = ""
        for x in self.ADict.keys():
            dictPrint += str("Airfield OACI code: %s, Airfield Name: %s, lat: %.5f, long: %.5f" % (
            x, self.ADictNames[x], self.ADict[x].lat, self.ADict[x].long))
            dictPrint += "\n"
        return dictPrint

    def serialize_to_json(self):
        with open(config['DATA']['ADICT_FILE'], 'w') as json_file:
            json.dump(self.ADict, json_file, cls=geoTools.geoCoordinateEncoder)
        with open(config['DATA']['ADICTNAMES_FILE'], 'w') as json_file:
            json.dump(self.ADictNames, json_file)


if __name__ == "__main__":
    frenchAirports = aerodromesDict()
    # print(frenchAirports.ADict)
    print(frenchAirports.prettyPrint())
    # frenchAirports.serialize_to_json()
