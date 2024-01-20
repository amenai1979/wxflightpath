import logging
import re
import threading
import time
from json import load, dumps
from urllib import request

from wxflightpath import config
from wxflightpath.openaitranslator import translate
from wxflightpath.zoneFilter import *


@lru_cache(maxsize=None)
def sayInternational(input="LFRU"):
    output_text = ""
    international_alphabet_dict = {
        'A': 'Alpha',
        'B': 'Bravo',
        'C': 'Charlie',
        'D': 'Delta',
        'E': 'Echo',
        'F': 'Foxtrot',
        'G': 'Golf',
        'H': 'Hotel',
        'I': 'India',
        'J': 'Juliet',
        'K': 'Kilo',
        'L': 'Lima',
        'M': 'Mike',
        'N': 'November',
        'O': 'Oscar',
        'P': 'Papa',
        'Q': 'Quebec',
        'R': 'Romeo',
        'S': 'Sierra',
        'T': 'Tango',
        'U': 'Uniform',
        'V': 'Victor',
        'W': 'Whiskey',
        'X': 'X-ray',
        'Y': 'Yankee',
        'Z': 'Zulu',
    }
    if input:
        output_text = " ".join([international_alphabet_dict[char] for char in input.upper()])
    return output_text


@lru_cache(maxsize=None)
def sayNumbers(input="1800", lang='en'):
    output_text = ""
    spoken_numbers_dict = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine',
    }
    spoken_numbers_fr_dict = {
        '0': 'zéro',
        '1': 'unité',
        '2': 'deux',
        '3': 'trois',
        '4': 'quatre',
        '5': 'cinq',
        '6': 'six',
        '7': 'sept',
        '8': 'huit',
        '9': 'neuf'
    }

    if input and lang == 'en':
        output_text = " ".join([spoken_numbers_dict[char] for char in list(input)])
    else:
        output_text = " ".join([spoken_numbers_fr_dict[char] for char in list(input)])
    return output_text


class Wxcrawler:
    def __init__(self, config, secret=None):
        self.threadObsResults = {}
        self.threadForResults = {}
        try:
            assert secret
            self._load_config(config, secret)
        except AssertionError:
            logging.error("No secret provided")
            raise

    def _load_config(self, config, secret):
        # dev only:
        # self._token = config['SECURITY']['TOKEN']
        self._token = secret
        self._useragent = config['NETWORK']['USERAGENT']
        self._baseurlmetar = config['NETWORK']['PROTOCOL'] + config['NETWORK']['HOSTNAME'] + config['NETWORK']['METAR']
        self._baseurltaf = config['NETWORK']['PROTOCOL'] + config['NETWORK']['HOSTNAME'] + config['NETWORK']['TAF']
        self._baseurlnotam = config['NETWORK']['PROTOCOL'] + config['NETWORK']['HOSTNAME'] + config['NETWORK']['NOTAM']
        self._params = config['NETWORK']['PARAMS']
        self._paramstaf = config['NETWORK']['PARAMSTAF']
        self._timeout = config['NETWORK']['TIMEOUT']

    def getObservationWX(self, airfield='LFRO'):
        req = request.Request(self._baseurlmetar + airfield + self._params)
        # print(req.get_full_url())
        req.add_header('Authorization', self._token)
        req.add_header('User-Agent', self._useragent)
        result = None
        try:
            rawResponse = request.urlopen(req, timeout=int(self._timeout))
            if rawResponse.getcode() == 200:
                response = json.loads(dumps(load(rawResponse)))
                result = (
                    response['raw'], response['speech'], response['density_altitude'], response['pressure_altitude'],
                    airfield)
        except Exception as e:
            logging.exception("url %s Error: %s", req.get_full_url(), e)
            pass
        return result

    def threadGetObservationWX(self, airfield):
        result = self.getObservationWX(airfield)
        if result:
            self.threadObsResults[airfield] = result

    def getForecastWX(self, airfield='LFRO'):
        req = request.Request(self._baseurltaf + airfield + self._paramstaf)
        req.add_header('Authorization', self._token)
        result = None
        try:
            rawResponse = request.urlopen(req, timeout=int(self._timeout))
            if rawResponse.getcode() == 200:
                response = json.loads(dumps(load(rawResponse)))
                result = (response['raw'], response['speech'], airfield)
        except Exception as e:
            logging.exception("url %s Error: %s", req.get_full_url(), e)
            pass
        return result

    def threadGetForecastWX(self, airfield):
        result = self.getForecastWX(airfield)
        if result:
            self.threadForResults[airfield] = result

    def getNOTAM(self, airfield='LFRO'):
        req = request.Request(self._baseurlnotam + airfield)
        req.add_header('Authorization', self._token)
        result = None
        try:
            response = json.loads(dumps(load(request.urlopen(req))))
            print(response)
            # result=(response['raw'],response['speech'], airfield)
        except:
            pass
        return result

    @lru_cache(maxsize=None)
    def extractTime(self, metar="LFRU 121800Z AUTO 22013KT 9999 -RA FEW010 OVC100 13/11 Q1007"):
        metarList = metar.split()
        pattern = re.compile(r'^(\d{2})(\d{4})Z$')
        match = pattern.match(metarList[1])
        # print(match)
        if match:
            day = match.group(1)
            # print(day)
            time = match.group(2)
            return [str(day), str(time)]
        else:
            return None

    def formatObservationWX(self, result=None, lang='en'):
        AirportNames = frenchAirports.ADictNames
        textList = []
        ##for information only result = (response['raw'], response['speech'], response['density_altitude'], response['pressure_altitude'], airfield)
        if result and lang == 'en':
            textList.append("This is the weather observation for")
            textList.append(sayInternational(result[4]))
            textList.append(AirportNames[result[4]])
            textList.append("observed on day")
            textList.append(self.extractTime(result[0])[0])
            textList.append("of the month, at Zulu time")
            textList.append(sayNumbers(self.extractTime(result[0])[1]))
            textList.append(".")
            textList.append(result[1])
            textList.append(".")
            textList.append("density altitude")
            textList.append(str(result[2]))
            textList.append("feet.")
        elif result and lang == 'fr':
            textList.append("Ci-après l'observation météorologique de")
            textList.append(sayInternational(result[4]))
            textList.append(AirportNames[result[4]])
            textList.append("émise le jour")
            textList.append(sayNumbers(self.extractTime(result[0])[0], lang='fr'))
            textList.append("du mois, à l'heure UTC")
            textList.append(sayNumbers(self.extractTime(result[0])[1], lang='fr'))
            textList.append(".")
            textList.append(translate(result[1], lang='fr'))
            textList.append(".")
            textList.append("densité altitude")
            textList.append(str(result[2]))
            textList.append("pieds.")
        return ' '.join(textList)

    def formatForecastWX(self, result=None, lang='en'):
        AirportNames = frenchAirports.ADictNames
        textList = []
        ##for information only result = (response['raw'], response['speech'], airfield)
        if result and lang == 'en':
            textList.append("This is the weather Forecast for")
            textList.append(sayInternational(result[2]))
            textList.append(AirportNames[result[2]])
            textList.append(".")
            textList.append(result[1])
        elif result and lang == 'fr':
            textList.append("Ci-après les prévisions météorologiques de")
            textList.append(sayInternational(result[2]))
            textList.append(AirportNames[result[2]])
            textList.append(".")
            textList.append(translate(result[1], lang='fr'))
        return ' '.join(textList)

    def orderObsResults(self, desired_order):
        try:
            # only apply to threading because we can"'t control teh completion
            return sorted(self.threadObsResults.items(), key=lambda item: desired_order.index(item[0]))
        except ValueError:
            return self.threadObsResults.items()

    def orderForResults(self, desired_order):
        try:
            return sorted(self.threadForResults.items(), key=lambda item: desired_order.index(item[0]))
        except ValueError:
            return self.threadForResults.items()


def demo_wxcrawler():
    try:
        secret = config['SECURITY']['TOKEN']
        assert secret and secret != ''
    except AssertionError:
        logging.error("Please configure the TOKEN param in the default.cfg file.")
        raise
    crawler = Wxcrawler(config=config, secret=secret)
    startTime = time.time()
    logging.info("observations and forcasts collection has started at %i", startTime)
    airfields = getAirfieldsInFlightPath('LFRU', 'LFPT')
    # start threads to get observation weather for each airfield
    [threading.Thread(target=crawler.threadGetObservationWX, args=(airfield,)).start() for airfield in airfields]
    # start threads to get forecast weather for each airfield
    [threading.Thread(target=crawler.threadGetForecastWX, args=(airfield,)).start() for airfield in airfields]
    # join all threads
    [thread.join() for thread in threading.enumerate() if thread != threading.current_thread()]
    endTime = time.time()
    logging.info("observations and forecasts collection has completed in %i seconds", endTime - startTime)
    [print(crawler.formatObservationWX(ro[1])) for ro in crawler.orderObsResults(desired_order=airfields)]
    [print(crawler.formatForecastWX(rf[1])) for rf in crawler.orderForResults(desired_order=airfields)]


def demo_wxcrawler_fr():
    try:
        secret = config['SECURITY']['TOKEN']
        assert secret and secret != ''
    except AssertionError:
        logging.error("Please configure the TOKEN param in the default.cfg file.")
        raise
    crawler = Wxcrawler(config=config, secret=secret)
    startTime = time.time()
    logging.info("observations and forcasts collection has started at %i", startTime)
    airfields = getAirfieldsInFlightPath('LFQQ', 'LFBD')
    # start threads to get observation weather for each airfield
    [threading.Thread(target=crawler.threadGetObservationWX, args=(airfield,)).start() for airfield in airfields]
    # start threads to get forecast weather for each airfield
    [threading.Thread(target=crawler.threadGetForecastWX, args=(airfield,)).start() for airfield in airfields]
    # join all threads
    [thread.join() for thread in threading.enumerate() if thread != threading.current_thread()]
    endTime = time.time()
    logging.info("observations and forecasts collection has completed in %i seconds", endTime - startTime)
    [print(crawler.formatObservationWX(ro[1], lang='fr')) for ro in crawler.orderObsResults(desired_order=airfields)]
    [print(crawler.formatForecastWX(rf[1], lang='fr')) for rf in crawler.orderForResults(desired_order=airfields)]


def demo_wxcrawler_fr_trainer():
    try:
        secret = config['SECURITY']['TOKEN']
        assert secret and secret != ''
    except AssertionError:
        logging.error("Please configure the TOKEN param in the default.cfg file.")
        raise
    crawler = Wxcrawler(config=config, secret=secret)
    startTime = time.time()
    # the purpose is to populate the translation db by creating different combinations of paths.

    paths = [("LFQQ", "LFRB"), ("LFAT", "LFRH"), ("LFQQ", "LFRS"), ("LFQQ", "LFBH"), ("LFQQ", "LFBG"),
             ("LFAT", "LFBZ"), ("LFQQ", "LFBT"), ("LFQQ", "LFBO"), ("LFQQ", "LFMP"), ("LFQQ", "LFMT"),
             ("LFQQ", "LFMI"), ("LFQQ", "LFTH"), ("LFQQ", "LFMN"), ("LFQQ", "LFJL"), ("LFQQ", "LFGA"),
             ("LFQQ", "LFSB"), ("LFQQ", "LFSM"), ("LFQQ", "LFSP"), ("LFQQ", "LSGG"), ("LFQQ", "LFLB"),
             ("LFQQ", "LFLS"), ("LFQQ", "LFNA"), ("LFQQ", "LFMR")
             ]
    logging.info("translator training has started at %i", startTime)
    for p in paths:
        airfields = getAirfieldsInFlightPath(p[0], p[1])
        # start threads to get observation weather for each airfield
        [threading.Thread(target=crawler.threadGetObservationWX, args=(airfield,)).start() for airfield in airfields]
        # start threads to get forecast weather for each airfield
        [threading.Thread(target=crawler.threadGetForecastWX, args=(airfield,)).start() for airfield in airfields]
        # join all threads
        [thread.join() for thread in threading.enumerate() if thread != threading.current_thread()]
        endTime = time.time()
        logging.info("observations and forecasts collection has completed in %i seconds for %s > %s",
                     endTime - startTime, p[0], p[1])
        [print(crawler.formatObservationWX(ro[1], lang='fr')) for ro in
         crawler.orderObsResults(desired_order=airfields)]
        [print(crawler.formatForecastWX(rf[1], lang='fr')) for rf in crawler.orderForResults(desired_order=airfields)]
    logging.info("translator training has completed at %i", startTime)


if __name__ == '__main__':
    # demo_wxcrawler()
    # demo_wxcrawler_fr()
    demo_wxcrawler_fr_trainer()