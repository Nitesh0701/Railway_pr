import requests

BASE_URL = "https://irctc1.p.rapidapi.com/api/v3/trainBetweenStations"

def get_trains(startStationCode:str,endStationCode:str,dateOfJourney:str):
    querystring = {"fromStationCode":startStationCode,"toStationCode":endStationCode,"dateOfJourney":dateOfJourney}

    headers = {
        "X-RapidAPI-Key": 
        "X-RapidAPI-Host": "irctc1.p.rapidapi.com"
    }
    response = requests.get(BASE_URL, headers=headers, params=querystring)

    return response.json()

