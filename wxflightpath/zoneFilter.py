from re import match
from wxflightpath.coordinatesLoader import aerodromesDict
from wxflightpath.geoTools import *
from wxflightpath import config

def getAirfieldsInFlightPath(origin='LFPT', destination='LFRU', aerodromes_file=config['DATA']['AERODROMES_FILE']):
    frenchAirports = aerodromesDict(aerodromes_file)
    contour = bipolarGeoZone(frenchAirports.ADict[origin], frenchAirports.ADict[destination]).setContour()
    flightZone = geoZone(contour)
    airportsWithinZone = filter(lambda x: flightZone.contains(aerodromesDict.ADict[x]), aerodromesDict.ADict.keys())
    pattern = r'\b[a-zA-Z]{4}\b'
    validAirports = filter(lambda x: match(pattern, x), airportsWithinZone)
    return list(validAirports)

if __name__ == '__main__':
    print(getAirfieldsInFlightPath())