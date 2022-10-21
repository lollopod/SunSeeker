import requests
import json
from weatherFinder import weatherFinder



def SeekSunnyStations() :

    SunSeeker = weatherFinder()


    response = requests.get(SunSeeker.DBGendpoint+"/stations", params={'query' : SunSeeker.stationName})

    #first output of the query will be taken as departure station
    departure_station = response.json()[0]

    #I check first the weather at the departure station
    # if (SunSeeker.checkWeatherAtStation(departure_station)) :
        # return (departure_station)



    if (SunSeeker.config['klimaticket'] and SunSeeker.checkStationCountry(departure_station)) : 
        print ("Departure station not in Austria, but klimaticket active")
        return -1
    data = requests.get(SunSeeker.DBGendpoint+"/"+departure_station['id']).json()

    sunny_stations = []
    # I will get here an array of reachable train station by direct train connection
    # they are already sorted with increasing departure
    # I need to check the weather for each of these points until I find one that satisfy the requirements (ex: cloudiness < 10%)
    #for loop 
    for station in data :
        if (SunSeeker.config['klimaticket'] and SunSeeker.checkStationCountry(departure_station)) : 
            print ("Station outside Austria, skipping it.")
            continue
        (sunnyThere, forecast) = SunSeeker.checkWeatherAtStation(station)
        if (sunnyThere) :
            station['forecast'] = forecast
            sunny_stations.append(station)
        if (len(sunny_stations) > 5 ) : break
    #######
    return sunny_stations
    # I can then stop and:
    # 
    # provide the result with the name of the station and the weather
    # eventually check the next departing train (dep to destination) 
    

stationsArray = SeekSunnyStations()

SunnyStations = dict(enumerate(map(str, stationsArray)))

print(SunnyStations)
