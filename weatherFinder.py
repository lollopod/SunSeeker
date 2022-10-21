from pyowm.owm import OWM
import json
import requests

class weatherFinder :

    def __init__(self) :
        self.DBGendpoint = 'https://api.direkt.bahn.guru'

        with open('config.json', 'r') as f:
            self.config = json.load(f)


        self.stationName = self.config['station_name']

        self.owm = OWM(self.config['owm_api_key'])
        self.owmMgr = self.owm.weather_manager()



    def getWeatherAtStation (self, station):
        return self.owmMgr.one_call(lat=station['location']['latitude'], lon=station['location']['longitude'])
    

    def checkWeatherAtStation (self, station) :
        Weather = self.getWeatherAtStation(station)

        forecast = getattr(Weather, self.config['owm_forecast'])
        status = getattr(forecast, self.config['owm_decision_parameter'])

        if (status <=  self.config['owm_decision_threshold']) :
            #parameter to be selected here, I think I will choose cloudiness
            return (1, forecast)  #sun has been found
        else : 
            return (0, forecast) # no sun
    def checkStationCountry(self, station) :
       
        station = requests.get(self.DBGendpoint+"/stations/"+station['id']).json()
         # I can eventually check if the country is Austria (I could also do this upfront for all the stations)
        if (station['country'] != 'AT') : return -1
        else : return 0
