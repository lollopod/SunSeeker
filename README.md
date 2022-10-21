# SunSeeker
This simple script is intended to find the closest train station, reachable by train, where the sun is shining.

It is based on the great Direkt Bahn API https://github.com/juliuste/api.direkt.bahn.guru and OpeWeatherMap.

you should provide a '.config' file as follows:


{ 
    "owm_api_key" : "you own api key",
    "station_name" : "Linz",
    "owm_decision_parameter" : "clouds",
    "owm_decision_threshold" : 10,
    "owm_forecast" : "current", # alternative ex: forecast daily
    "klimaticket" : 1  # limits the search within the stations in Austria
}
