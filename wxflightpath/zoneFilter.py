from functools import lru_cache
from functools import partial
from re import match

from wxflightpath import airports
from wxflightpath.geoTools import *

#load valid stations in the world
@lru_cache(maxsize=None)
def loadStationsFilter():
    with open("../data/stations.filter.json","r") as input:
        input_list=json.load(input)
        #print(input_list)
        airportsWithinZone = filter(lambda x: validateAirfield(x), input_list)
        #print(list(airportsWithinZone))
        return list(airportsWithinZone)



# define OACI airfield pattern

@lru_cache(maxsize=None)
def validateAirfield(airfield):
    # pattern = r'\b[a-zA-Z]{4}\b'
    # validAirports = filter(lambda x: match(pattern, x), airportsWithinZone)
    pattern = r'\b[a-zA-Z]{4}\b'
    result = match(pattern, airfield)
    #print(result)
    return result


@lru_cache(maxsize=None)
def getAirfieldsInFlightPath(origin='LFPT', destination='LFRU'):
    try:
        contour = bipolarGeoZone(airports.ADict[origin], airports.ADict[destination]).setContour()
        flightZone = geoZone(contour)
        airportsWithinZone = filter(lambda x: flightZone.contains(airports.ADict[x]), airports.ADict.keys())
        #print(list(airportsWithinZone))
        # exclude none OACI airfields that are unlikely to have a weather station
        #validICAOAirports = filter(lambda x: validateAirfield(x), airportsWithinZone)
        validAirports = filter(lambda x: x in loadStationsFilter(), airportsWithinZone)
    except:
        validAirports=[origin,destination]
        pass
    #print(list(validAirports))
    return orderedStations(origin, destination, list(validAirports))

@lru_cache(maxsize=None)
def distanceFromOrigin(airfield='LFPG', origin='LFRU'):
    lat, long = airports.ADict[airfield].lat, airports.ADict[airfield].long
    lat_org, long_org = airports.ADict[origin].lat, airports.ADict[origin].long
    return (lat - lat_org) ** 2 + (long - long_org) ** 2


def orderedStations(origin='LFPT', destination='LFRU', airfields=[]):
    sorted_airfields =[]
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

def getTrainingPaths():
    all_stations = loadStationsFilter()
    training_path = [(x,x) for x in all_stations]
    return training_path


if __name__ == '__main__':
    # print(getAirfieldsInFlightPath())
    # print(distanceFromOrigin())
    print(getTrainingPaths())
    print(len(getTrainingPaths()))