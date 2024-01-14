import json
from functools import lru_cache

from wxflightpath import picket


class geoCoordinate:
    lat: float
    long: float

    def __init__(self, lat, long):
        self.lat = lat
        self.long = long

    def __str__(self):
        return " ".join(["latitude:", str(self.lat), "longitude:", str(self.long)])


# Custom JSON encoder for GeoCoordinate
class geoCoordinateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, geoCoordinate):
            return {'lat': obj.lat, 'long': obj.long}
        return super().default(obj)


def geoCoordinateDecoder(obj):
    if 'lat' in obj and 'long' in obj:
        return geoCoordinate(obj['lat'], obj['long'])
    return obj


@lru_cache(maxsize=None)
class bipolarGeoZone():
    westMost = None
    eastMost = None

    def __init__(self, origin, destination):
        if origin.long <= destination.long:
            self.westMost = origin
            self.eastMost = destination
        else:
            self.westMost = destination
            self.eastMost = origin

    @lru_cache(maxsize=None)
    def setContour(self):
        # we try to position the points a degree (60 minutes) North West, South West of the west most , and the North east , South east of the eastmost for most of the globe.
        # todo one day I will be less lazy and cover the edge cases
        # assert (89.5 >= self.westMost.lat >= -89.5 and 179.5 >= self.westMost.long >= -179.5)
        # assert (89.5 >= self.eastMost.lat >= -89.5 and 179.5 >= self.eastMost.long >= -179.5)
        wmlat = self.westMost.lat
        wmlong = self.westMost.long
        emlat = self.eastMost.lat
        emlong = self.eastMost.long
        nwwm = geoCoordinate(wmlat + 1, wmlong - 1)
        swwm = geoCoordinate(wmlat - 1, wmlong - 1)
        neem = geoCoordinate(emlat + 1, emlong + 1)
        seem = geoCoordinate(emlat - 1, emlong + 1)
        return [nwwm, swwm, neem, seem]


class geoZone:
    zone = picket.Fence()

    def __init__(self, coordinates):
        self.navPoints = coordinates
        for p in self.navPoints:
            self.zone.add_point((p.long, p.lat))

    @lru_cache(maxsize=None)
    def contains(self, point):
        status = self.zone.check_point((point.long, point.lat))
        return status


if __name__ == '__main__':
    paris = geoCoordinate(48.8752778, 2.1644444444444444)
    morlaix = geoCoordinate(48.58333, -3.83333)
    # print(paris)
    contour = bipolarGeoZone(paris, morlaix).setContour()
    flightZone = geoZone(contour)

    print(flightZone.contains(paris))
    print(flightZone.contains(morlaix))
    print(flightZone.contains(contour[0]))
    print(flightZone.contains(contour[1]))
    print(flightZone.contains(contour[2]))
    print(flightZone.contains(contour[3]))
