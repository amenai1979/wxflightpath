import xmltodict
from wxflightpath import geoTools, config
class aerodromesDict:
    aerodromes = []
    ADict = {}
    ADictNames={}

    def __init__(self, aerodromes_file=config['DATA']['AERODROMES_FILE']):
        try:
            self.aerodromes_file = aerodromes_file
            with open(self.aerodromes_file, 'r', encoding='ISO-8859-1') as xml_file:
                # Parse the XML data into a Python dictionary
                xml_data = xmltodict.parse(xml_file.read())
                self.aerodromes = xml_data['SiaExport']['Situation']['AdS']['Ad']
                self.loadAerodromesDict()
        except:
            raise 'Error loading aerodromes file'

    def loadAerodromesDict(self):
        for x in range(0, len(self.aerodromes)):
            key = str(self.aerodromes[x]['@lk']).replace("[", "").replace(']', "")
            name = str(self.aerodromes[x]['AdNomComplet'])
            self.ADict[key] = geoTools.geoCoordinate(float(self.aerodromes[x]['ArpLat']),
                                                     float(self.aerodromes[x]['ArpLong']))
            self.ADictNames[key]=name

    def prettyPrint(self):
        dictPrint = ""
        for x in self.ADict.keys():
            dictPrint += str("Airfield OACI code: %s, Airfield Name: %s, lat: %.5f, long: %.5f" % (x, self.ADictNames[x], self.ADict[x].lat, self.ADict[x].long))
            dictPrint += "\n"
        return dictPrint

if __name__ == "__main__":
    frenchAirports = aerodromesDict()
    print(frenchAirports.ADict)
    print(frenchAirports.prettyPrint())
