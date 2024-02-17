import requests

BASE_URL = "https://irctc1.p.rapidapi.com/api/v3/trainBetweenStations"

def get_trains(startStationCode:str,endStationCode:str,dateOfJourney:str):
    querystring = {"fromStationCode":startStationCode,"toStationCode":endStationCode,"dateOfJourney":dateOfJourney}

    headers = {
        "X-RapidAPI-Key": "d1a177f3e5mshc45c9a81610c1f9p16b308jsn36e29bdc8ce4",
        "X-RapidAPI-Host": "irctc1.p.rapidapi.com"
    }
    response = requests.get(BASE_URL, headers=headers, params=querystring)

    return response.json()

