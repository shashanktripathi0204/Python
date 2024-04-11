import requests

OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "7a66cffc4cd10f28ce2d2383b025ae30"
LAT = 60.982571
LONG = 25.661640
WEATHER_PARAMETER = {
    "lat" : LAT,
    "lon" : LONG,
    "appid" : API_KEY,
    "cnt" : 4
}

response = requests.get(OWM_endpoint, params = WEATHER_PARAMETER)
# To catch the response code other tham 200
response.raise_for_status()
weather_data = response.json()

# This can be used if there are multiple data for a given day
# for i in weather_data["list"]:
#   for j in i["weather"]:
#     print("Bring an umberlla" if j["id"] < 700 else "No need")

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    print("Bring Umbrella")

