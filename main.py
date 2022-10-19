import requests
import json
import weatherFinder


SunSeeker = weatherFinder()




response = requests.get(SunSeeker.DBGendpoint+"/stations", params={'query' : SunSeeker.stationName})

#first output of the query will be taken as departure station
departure_station = response.json()[0]

#I check first the weather at the departure station
WeatherAtDeparture = SunSeeker.getWeatherAtStation(departure_station)
if (WeatherAtDeparture) :
    #parameter to be selected here, I think I will choose cloudiness
    pass

data = requests.get(SunSeeker.DBGendpoint+"/"+departure_station['id'])


# I will get here an array of reachable train station by direct train connection
# they are already sorted with increasing departure
# I need to check the weather for each of these points until I find one that satisfy the requirements (ex: cloudiness < 10%)
#for loop WeatherAtLocation = SunSeeker.getWeatherAtStation(departure_station)

#######

# I need to check if this location is in Austria 
station = requests.get(SunSeeker.DBGendpoint+"/stations"+departure_station['id'])
# I can eventually check if the country is Austria (I could also do this upfront for all the stations)
country = station['country']

# I can then stop and:
# 
# provide the result with the name of the station and the weather
# eventually check the next departing train (dep to destination) 