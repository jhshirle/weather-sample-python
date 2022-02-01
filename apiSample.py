import requests


api_key = "YOUR-KEY-HERE"
base_url_current = "https://api.openweathermap.org/data/2.5/weather?units=imperial"
base_url_onecall = "https://api.openweathermap.org/data/2.5/onecall?units=imperial&exclude=daily"


def callCurrentWeather(lat, lng):
    url = base_url_current + "&lat=" + str(lat) + "&lon=" + str(lng) + "&appid=" + api_key
    response = requests.get(url)
    return response

def callOneCall(lat, lng):
    url = base_url_onecall + "&lat=" + str(lat) + "&lon=" + str(lng) + "&appid=" + api_key
    response = requests.get(url)
    return response

print(callOneCall(37, -75).text)

