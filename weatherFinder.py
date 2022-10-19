from pyowm.owm import OWM
import json

class weatherFinder :

    def __init__(self) -> None:
        self.DBGendpoint = 'https://api.direkt.bahn.guru'

        with open('config.json', 'r') as f:
            self.config = json.load(f)


        self.stationName = self.config['station_name']
        self.owmApiKey = self.config['owm_api_key']

        self.owm = OWM('missing-api-key')
        self.owmMgr = self.owm.weather_manager()



    def getWeatherAtStation (self, station):
        return self.owmMgr.one_call(lat=station['location']['latitude'], lon=station['location']['longitude'])
    