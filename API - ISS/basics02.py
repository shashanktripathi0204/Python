import requests
from datetime import datetime

MY_LAT = 26.812476
MY_LNG = 80.910011

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted":0
}

response = requests.get(url = "https://api.sunrise-sunset.org/json", params = parameters)
response.raise_for_status()
data = response.json()
# taking only the hour value
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

# time
time_now = datetime.now()
print(time_now.hour)