import requests

response = requests.get(url = "http://api.open-notify.org/iss-now.json")
# if the response is not successful it will raise an error
response.raise_for_status()

data = response.json()
latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]

iss_position = (longitude, latitude)

print(iss_position)