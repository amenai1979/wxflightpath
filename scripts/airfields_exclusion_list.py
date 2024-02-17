import json
from urllib import request
from wxflightpath import config


_token = config['SECURITY']['TOKEN']
_useragent = config['NETWORK']['USERAGENT']
_baseurlmetar = config['NETWORK']['PROTOCOL'] + config['NETWORK']['HOSTNAME'] + config['NETWORK']['METAR']
_baseurltaf = config['NETWORK']['PROTOCOL'] + config['NETWORK']['HOSTNAME'] + config['NETWORK']['TAF']
_baseurlnotam = config['NETWORK']['PROTOCOL'] + config['NETWORK']['HOSTNAME'] + config['NETWORK']['NOTAM']
_params = config['NETWORK']['PARAMS']
_paramstaf = config['NETWORK']['PARAMSTAF']
_timeout = config['NETWORK']['TIMEOUT']

def getObservationWX(airfield='LFRO'):
    req = request.Request(_baseurlmetar + airfield + _params)
    # print(req.get_full_url())
    req.add_header('Authorization', _token)
    req.add_header('User-Agent', _useragent)
    result = False
    try:
        rawResponse = request.urlopen(req, timeout=int(_timeout))
        if rawResponse.getcode() != 200:
            result = True
    except:
        result=True
        pass
    return result

with open("../data/stations.cache.json","r") as input:
  all_stations = json.load(input)
  white_list=[f["icaoId"] for f in all_stations]
  #print(len(white_list))
  with open("../data/stations.filter.json","w") as output:
      json.dump(white_list, output, indent=4)

"""
with open("../data/airports.json","r") as input:
  all_dict = json.load(input)
  print(len(all_dict.keys()))
  exclusion_metar_list=[]
  
  for key in all_dict.keys():
        if getObservationWX(key):
            exclusion_metar_list.append(key)
    print(exclusion_metar_list)
"""

