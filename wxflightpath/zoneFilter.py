from functools import lru_cache
from functools import partial
from re import match

from wxflightpath import frenchAirports
from wxflightpath.geoTools import *


# define OACI airfield pattern

@lru_cache(maxsize=None)
def validateAirfield(airfield):
    # pattern = r'\b[a-zA-Z]{4}\b'
    # validAirports = filter(lambda x: match(pattern, x), airportsWithinZone)
    pattern = r'\b[a-zA-Z]{4}\b'
    result = match(pattern, airfield)
    return result


@lru_cache(maxsize=None)
def getAirfieldsInFlightPath(origin='LFPT', destination='LFRU'):
    contour = bipolarGeoZone(frenchAirports.ADict[origin], frenchAirports.ADict[destination]).setContour()
    flightZone = geoZone(contour)
    airportsWithinZone = filter(lambda x: flightZone.contains(frenchAirports.ADict[x]), frenchAirports.ADict.keys())
    # exclude none OACI airfields that are unlikely to have a weather station
    validAirports = filter(lambda x: validateAirfield(x), airportsWithinZone)
    return orderedStations(origin, destination, list(validAirports))


@lru_cache(maxsize=None)
def distanceFromOrigin(airfield='LFPG', origin='LFRU'):
    lat, long = frenchAirports.ADict[airfield].lat, frenchAirports.ADict[airfield].long
    lat_org, long_org = frenchAirports.ADict[origin].lat, frenchAirports.ADict[origin].long
    return (lat - lat_org) ** 2 + (long - long_org) ** 2


def orderedStations(origin='LFPT', destination='LFRU', airfields=[]):
    ordered = []
    # Always start with the origin and destination
    ordered.append(origin)
    ordered.append(destination)
    # exclude from the sorting the origin and destination
    filtered_list = [x for x in airfields if x not in ordered]
    # print(filtered_list)
    distanceFromOriginPartial = partial(distanceFromOrigin, origin=origin)
    if filtered_list:
        sorted_airfields = sorted(filtered_list, key=distanceFromOriginPartial)
    ordered += sorted_airfields
    return ordered


if __name__ == '__main__':
    print(getAirfieldsInFlightPath())
    # print(distanceFromOrigin())
