import requests


API_KEY = "7a66cffc4cd10f28ce2d2383b025ae30"
LAT = 60.982571
LONG = 25.661640
PARAMETER = {
    "lat" : LAT,
    "lon" : LONG,
    "appid" : API_KEY
}

response = requests.get(url = f"https://api.openweathermap.org/data/2.5/forecast", params = PARAMETER)
data = response.json()
status_code = f"cod:{data["cod"]}"

print(status_code)

for i in data["list"]:
  for j in i["weather"]:
    print("Bring an umberlla" if j["id"] < 700 else "No need")



party = {
  "cod": "200",
  "message": 0,
  "cnt": 40,
  "list": [
    {
      "dt": 1712880000,
      "main": {
        "temp": 297.9,
        "feels_like": 297.34,
        "temp_min": 297.9,
        "temp_max": 299.35,
        "pressure": 1009,
        "sea_level": 1009,
        "grnd_level": 995,
        "humidity": 35,
        "temp_kf": -1.45
      },
      "weather": [
        {
          "id": 801,
          "main": "Clouds",
          "description": "few clouds",
          "icon": "02n"
        }
      ],
      "clouds": {
        "all": 20
      },
      "wind": {
        "speed": 1.05,
        "deg": 229,
        "gust": 1.15
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2024-04-12 00:00:00"
    },
    {
      "dt": 1712890800,
      "main": {
        "temp": 303.34,
        "feels_like": 301.66,
        "temp_min": 303.34,
        "temp_max": 306.42,
        "pressure": 1010,
        "sea_level": 1010,
        "grnd_level": 997,
        "humidity": 23,
        "temp_kf": -3.08
      },
      "weather": [
        {
          "id": 803,
          "main": "Clouds",
          "description": "broken clouds",
          "icon": "04d"
        }
      ],
      "clouds": {
        "all": 73
      },
      "wind": {
        "speed": 0.9,
        "deg": 252,
        "gust": 1.17
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2024-04-12 03:00:00"
    },
    {
      "dt": 1712901600,
      "main": {
        "temp": 311.72,
        "feels_like": 308.65,
        "temp_min": 311.72,
        "temp_max": 311.72,
        "pressure": 1010,
        "sea_level": 1010,
        "grnd_level": 997,
        "humidity": 9,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 804,
          "main": "Clouds",
          "description": "overcast clouds",
          "icon": "04d"
        }
      ],
      "clouds": {
        "all": 98
      },
      "wind": {
        "speed": 2.02,
        "deg": 283,
        "gust": 1.91
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2024-04-12 06:00:00"
    },
    {
      "dt": 1712912400,
      "main": {
        "temp": 313.03,
        "feels_like": 309.72,
        "temp_min": 313.03,
        "temp_max": 313.03,
        "pressure": 1007,
        "sea_level": 1007,
        "grnd_level": 993,
        "humidity": 8,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 804,
          "main": "Clouds",
          "description": "overcast clouds",
          "icon": "04d"
        }
      ],
      "clouds": {
        "all": 100
      },
      "wind": {
        "speed": 2.65,
        "deg": 337,
        "gust": 3.32
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2024-04-12 09:00:00"
    },
    {
      "dt": 1712923200,
      "main": {
        "temp": 311.74,
        "feels_like": 308.57,
        "temp_min": 311.74,
        "temp_max": 311.74,
        "pressure": 1005,
        "sea_level": 1005,
        "grnd_level": 992,
        "humidity": 8,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 803,
          "main": "Clouds",
          "description": "broken clouds",
          "icon": "04d"
        }
      ],
      "clouds": {
        "all": 84
      },
      "wind": {
        "speed": 1,
        "deg": 346,
        "gust": 1.9
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2024-04-12 12:00:00"
    },
    {
      "dt": 1712934000,
      "main": {
        "temp": 306.1,
        "feels_like": 303.72,
        "temp_min": 306.1,
        "temp_max": 306.1,
        "pressure": 1007,
        "sea_level": 1007,
        "grnd_level": 994,
        "humidity": 12,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 801,
          "main": "Clouds",
          "description": "few clouds",
          "icon": "02n"
        }
      ],
      "clouds": {
        "all": 22
      },
      "wind": {
        "speed": 2.19,
        "deg": 205,
        "gust": 2.26
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2024-04-12 15:00:00"
    },
    {
      "dt": 1712944800,
      "main": {
        "temp": 303.08,
        "feels_like": 301.3,
        "temp_min": 303.08,
        "temp_max": 303.08,
        "pressure": 1008,
        "sea_level": 1008,
        "grnd_level": 994,
        "humidity": 19,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 801,
          "main": "Clouds",
          "description": "few clouds",
          "icon": "02n"
        }
      ],
      "clouds": {
        "all": 19
      },
      "wind": {
        "speed": 3.38,
        "deg": 229,
        "gust": 6.42
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2024-04-12 18:00:00"
    },
    {
      "dt": 1712955600,
      "main": {
        "temp": 301.82,
        "feels_like": 300.53,
        "temp_min": 301.82,
        "temp_max": 301.82,
        "pressure": 1007,
        "sea_level": 1007,
        "grnd_level": 993,
        "humidity": 25,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 803,
          "main": "Clouds",
          "description": "broken clouds",
          "icon": "04n"
        }
      ],
      "clouds": {
        "all": 82
      },
      "wind": {
        "speed": 2.61,
        "deg": 284,
        "gust": 3.96
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2024-04-12 21:00:00"
    },
    {
      "dt": 1712966400,
      "main": {
        "temp": 300.83,
        "feels_like": 299.9,
        "temp_min": 300.83,
        "temp_max": 300.83,
        "pressure": 1008,
        "sea_level": 1008,
        "grnd_level": 994,
        "humidity": 27,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 804,
          "main": "Clouds",
          "description": "overcast clouds",
          "icon": "04n"
        }
      ],
      "clouds": {
        "all": 85
      },
      "wind": {
        "speed": 3.73,
        "deg": 306,
        "gust": 6.31
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2024-04-13 00:00:00"
    },
    {
      "dt": 1712977200,
      "main": {
        "temp": 306.39,
        "feels_like": 304.33,
        "temp_min": 306.39,
        "temp_max": 306.39,
        "pressure": 1010,
        "sea_level": 1010,
        "grnd_level": 997,
        "humidity": 20,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 804,
          "main": "Clouds",
          "description": "overcast clouds",
          "icon": "04d"
        }
      ],
      "clouds": {
        "all": 100
      },
      "wind": {
        "speed": 3.04,
        "deg": 271,
        "gust": 4.29
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2024-04-13 03:00:00"
    },
    {
      "dt": 1712988000,
      "main": {
        "temp": 311.59,
        "feels_like": 309.19,
        "temp_min": 311.59,
        "temp_max": 311.59,
        "pressure": 1009,
        "sea_level": 1009,
        "grnd_level": 996,
        "humidity": 14,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 804,
          "main": "Clouds",
          "description": "overcast clouds",
          "icon": "04d"
        }
      ],
      "clouds": {
        "all": 100
      },
      "wind": {
        "speed": 3.19,
        "deg": 294,
        "gust": 3.22
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2024-04-13 06:00:00"
    },
    {
      "dt": 1712998800,
      "main": {
        "temp": 313.9,
        "feels_like": 310.88,
        "temp_min": 313.9,
        "temp_max": 313.9,
        "pressure": 1005,
        "sea_level": 1005,
        "grnd_level": 992,
        "humidity": 10,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 802,
          "main": "Clouds",
          "description": "scattered clouds",
          "icon": "03d"
        }
      ],
      "clouds": {
        "all": 50
      },
      "wind": {
        "speed": 1.87,
        "deg": 298,
        "gust": 3.38
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2024-04-13 09:00:00"
    },
    {
      "dt": 1713009600,
      "main": {
        "temp": 312.38,
        "feels_like": 309.54,
        "temp_min": 312.38,
        "temp_max": 312.38,
        "pressure": 1003,
        "sea_level": 1003,
        "grnd_level": 990,
        "humidity": 11,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 803,
          "main": "Clouds",
          "description": "broken clouds",
          "icon": "04d"
        }
      ],
      "clouds": {
        "all": 74
      },
      "wind": {
        "speed": 0.97,
        "deg": 220,
        "gust": 1.71
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2024-04-13 12:00:00"
    },
    {
      "dt": 1713020400,
      "main": {
        "temp": 306.63,
        "feels_like": 304.66,
        "temp_min": 306.63,
        "temp_max": 306.63,
        "pressure": 1006,
        "sea_level": 1006,
        "grnd_level": 993,
        "humidity": 21,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 804,
          "main": "Clouds",
          "description": "overcast clouds",
          "icon": "04n"
        }
      ],
      "clouds": {
        "all": 100
      },
      "wind": {
        "speed": 5.66,
        "deg": 240,
        "gust": 11.34
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2024-04-13 15:00:00"
    },
    {
      "dt": 1713031200,
      "main": {
        "temp": 305.2,
        "feels_like": 303.44,
        "temp_min": 305.2,
        "temp_max": 305.2,
        "pressure": 1008,
        "sea_level": 1008,
        "grnd_level": 994,
        "humidity": 24,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 804,
          "main": "Clouds",
          "description": "overcast clouds",
          "icon": "04n"
        }
      ],
      "clouds": {
        "all": 100
      },
      "wind": {
        "speed": 6.51,
        "deg": 295,
        "gust": 10.83
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2024-04-13 18:00:00"
    },
    {
      "dt": 1713042000,
      "main": {
        "temp": 303.25,
        "feels_like": 302.07,
        "temp_min": 303.25,
        "temp_max": 303.25,
        "pressure": 1007,
        "sea_level": 1007,
        "grnd_level": 993,
        "humidity": 31,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 804,
          "main": "Clouds",
          "description": "overcast clouds",
          "icon": "04n"
        }
      ],
      "clouds": {
        "all": 96
      },
      "wind": {
        "speed": 3.35,
        "deg": 272,
        "gust": 9.32
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2024-04-13 21:00:00"
    },
    {
      "dt": 1713052800,
      "main": {
        "temp": 301.63,
        "feels_like": 300.89,
        "temp_min": 301.63,
        "temp_max": 301.63,
        "pressure": 1009,
        "sea_level": 1009,
        "grnd_level": 995,
        "humidity": 35,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 804,
          "main": "Clouds",
          "description": "overcast clouds",
          "icon": "04n"
        }
      ],
      "clouds": {
        "all": 96
      },
      "wind": {
        "speed": 0.56,
        "deg": 20,
        "gust": 1.11
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2024-04-14 00:00:00"
    },
    {
      "dt": 1713063600,
      "main": {
        "temp": 306.89,
        "feels_like": 305.25,
        "temp_min": 306.89,
        "temp_max": 306.89,
        "pressure": 1010,
        "sea_level": 1010,
        "grnd_level": 997,
        "humidity": 24,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 802,
          "main": "Clouds",
          "description": "scattered clouds",
          "icon": "03d"
        }
      ],
      "clouds": {
        "all": 42
      },
      "wind": {
        "speed": 2.12,
        "deg": 314,
        "gust": 2.64
      },
      "visibility": 10000,
      "pop": 0.04,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2024-04-14 03:00:00"
    },
    {
      "dt": 1713074400,
      "main": {
        "temp": 310.84,
        "feels_like": 309.21,
        "temp_min": 310.84,
        "temp_max": 310.84,
        "pressure": 1009,
        "sea_level": 1009,
        "grnd_level": 996,
        "humidity": 19,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 802,
          "main": "Clouds",
          "description": "scattered clouds",
          "icon": "03d"
        }
      ],
      "clouds": {
        "all": 41
      },
      "wind": {
        "speed": 2.99,
        "deg": 263,
        "gust": 4.24
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2024-04-14 06:00:00"
    },
    {
      "dt": 1713085200,
      "main": {
        "temp": 311.3,
        "feels_like": 309.58,
        "temp_min": 311.3,
        "temp_max": 311.3,
        "pressure": 1006,
        "sea_level": 1006,
        "grnd_level": 993,
        "humidity": 18,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 803,
          "main": "Clouds",
          "description": "broken clouds",
          "icon": "04d"
        }
      ],
      "clouds": {
        "all": 74
      },
      "wind": {
        "speed": 3.11,
        "deg": 329,
        "gust": 4.68
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2024-04-14 09:00:00"
    },
    {
      "dt": 1713096000,
      "main": {
        "temp": 311.16,
        "feels_like": 309.41,
        "temp_min": 311.16,
        "temp_max": 311.16,
        "pressure": 1005,
        "sea_level": 1005,
        "grnd_level": 992,
        "humidity": 18,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 803,
          "main": "Clouds",
          "description": "broken clouds",
          "icon": "04d"
        }
      ],
      "clouds": {
        "all": 56
      },
      "wind": {
        "speed": 3.83,
        "deg": 336,
        "gust": 4.52
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2024-04-14 12:00:00"
    },
    {
      "dt": 1713106800,
      "main": {
        "temp": 306.1,
        "feels_like": 304.28,
        "temp_min": 306.1,
        "temp_max": 306.1,
        "pressure": 1007,
        "sea_level": 1007,
        "grnd_level": 993,
        "humidity": 23,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 803,
          "main": "Clouds",
          "description": "broken clouds",
          "icon": "04n"
        }
      ],
      "clouds": {
        "all": 55
      },
      "wind": {
        "speed": 1.24,
        "deg": 6,
        "gust": 1.47
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2024-04-14 15:00:00"
    },
    {
      "dt": 1713117600,
      "main": {
        "temp": 304.24,
        "feels_like": 302.57,
        "temp_min": 304.24,
        "temp_max": 304.24,
        "pressure": 1008,
        "sea_level": 1008,
        "grnd_level": 994,
        "humidity": 25,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 803,
          "main": "Clouds",
          "description": "broken clouds",
          "icon": "04n"
        }
      ],
      "clouds": {
        "all": 55
      },
      "wind": {
        "speed": 1.46,
        "deg": 12,
        "gust": 1.64
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2024-04-14 18:00:00"
    },
    {
      "dt": 1713128400,
      "main": {
        "temp": 302.65,
        "feels_like": 301.27,
        "temp_min": 302.65,
        "temp_max": 302.65,
        "pressure": 1007,
        "sea_level": 1007,
        "grnd_level": 993,
        "humidity": 27,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 802,
          "main": "Clouds",
          "description": "scattered clouds",
          "icon": "03n"
        }
      ],
      "clouds": {
        "all": 40
      },
      "wind": {
        "speed": 2.72,
        "deg": 344,
        "gust": 5.33
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2024-04-14 21:00:00"
    },
    {
      "dt": 1713139200,
      "main": {
        "temp": 301.4,
        "feels_like": 300.64,
        "temp_min": 301.4,
        "temp_max": 301.4,
        "pressure": 1008,
        "sea_level": 1008,
        "grnd_level": 994,
        "humidity": 34,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 802,
          "main": "Clouds",
          "description": "scattered clouds",
          "icon": "03n"
        }
      ],
      "clouds": {
        "all": 45
      },
      "wind": {
        "speed": 2.85,
        "deg": 319,
        "gust": 4.94
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2024-04-15 00:00:00"
    },
    {
      "dt": 1713150000,
      "main": {
        "temp": 307.57,
        "feels_like": 306.03,
        "temp_min": 307.57,
        "temp_max": 307.57,
        "pressure": 1010,
        "sea_level": 1010,
        "grnd_level": 996,
        "humidity": 24,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 803,
          "main": "Clouds",
          "description": "broken clouds",
          "icon": "04d"
        }
      ],
      "clouds": {
        "all": 66
      },
      "wind": {
        "speed": 4.73,
        "deg": 316,
        "gust": 6.86
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2024-04-15 03:00:00"
    },
    {
      "dt": 1713160800,
      "main": {
        "temp": 312.83,
        "feels_like": 311.02,
        "temp_min": 312.83,
        "temp_max": 312.83,
        "pressure": 1008,
        "sea_level": 1008,
        "grnd_level": 995,
        "humidity": 16,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 803,
          "main": "Clouds",
          "description": "broken clouds",
          "icon": "04d"
        }
      ],
      "clouds": {
        "all": 56
      },
      "wind": {
        "speed": 4.48,
        "deg": 299,
        "gust": 6.05
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2024-04-15 06:00:00"
    },
    {
      "dt": 1713171600,
      "main": {
        "temp": 314.24,
        "feels_like": 312.48,
        "temp_min": 314.24,
        "temp_max": 314.24,
        "pressure": 1005,
        "sea_level": 1005,
        "grnd_level": 992,
        "humidity": 15,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 803,
          "main": "Clouds",
          "description": "broken clouds",
          "icon": "04d"
        }
      ],
      "clouds": {
        "all": 80
      },
      "wind": {
        "speed": 5.54,
        "deg": 285,
        "gust": 6.44
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2024-04-15 09:00:00"
    },
    {
      "dt": 1713182400,
      "main": {
        "temp": 313.02,
        "feels_like": 311.01,
        "temp_min": 313.02,
        "temp_max": 313.02,
        "pressure": 1004,
        "sea_level": 1004,
        "grnd_level": 991,
        "humidity": 15,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 803,
          "main": "Clouds",
          "description": "broken clouds",
          "icon": "04d"
        }
      ],
      "clouds": {
        "all": 71
      },
      "wind": {
        "speed": 5.45,
        "deg": 284,
        "gust": 5.9
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2024-04-15 12:00:00"
    },
    {
      "dt": 1713193200,
      "main": {
        "temp": 308.18,
        "feels_like": 306.12,
        "temp_min": 308.18,
        "temp_max": 308.18,
        "pressure": 1006,
        "sea_level": 1006,
        "grnd_level": 993,
        "humidity": 19,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 801,
          "main": "Clouds",
          "description": "few clouds",
          "icon": "02n"
        }
      ],
      "clouds": {
        "all": 11
      },
      "wind": {
        "speed": 4.24,
        "deg": 283,
        "gust": 9.8
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2024-04-15 15:00:00"
    },
    {
      "dt": 1713204000,
      "main": {
        "temp": 305.55,
        "feels_like": 303.64,
        "temp_min": 305.55,
        "temp_max": 305.55,
        "pressure": 1006,
        "sea_level": 1006,
        "grnd_level": 993,
        "humidity": 22,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 800,
          "main": "Clear",
          "description": "clear sky",
          "icon": "01n"
        }
      ],
      "clouds": {
        "all": 10
      },
      "wind": {
        "speed": 3.61,
        "deg": 294,
        "gust": 8.11
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2024-04-15 18:00:00"
    },
    {
      "dt": 1713214800,
      "main": {
        "temp": 303.99,
        "feels_like": 302.34,
        "temp_min": 303.99,
        "temp_max": 303.99,
        "pressure": 1005,
        "sea_level": 1005,
        "grnd_level": 991,
        "humidity": 25,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 802,
          "main": "Clouds",
          "description": "scattered clouds",
          "icon": "03n"
        }
      ],
      "clouds": {
        "all": 35
      },
      "wind": {
        "speed": 3.21,
        "deg": 312,
        "gust": 5.71
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2024-04-15 21:00:00"
    },
    {
      "dt": 1713225600,
      "main": {
        "temp": 302.49,
        "feels_like": 301.14,
        "temp_min": 302.49,
        "temp_max": 302.49,
        "pressure": 1006,
        "sea_level": 1006,
        "grnd_level": 992,
        "humidity": 27,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 802,
          "main": "Clouds",
          "description": "scattered clouds",
          "icon": "03n"
        }
      ],
      "clouds": {
        "all": 38
      },
      "wind": {
        "speed": 3.15,
        "deg": 286,
        "gust": 5.46
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2024-04-16 00:00:00"
    },
    {
      "dt": 1713236400,
      "main": {
        "temp": 308.7,
        "feels_like": 306.69,
        "temp_min": 308.7,
        "temp_max": 308.7,
        "pressure": 1007,
        "sea_level": 1007,
        "grnd_level": 994,
        "humidity": 19,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 802,
          "main": "Clouds",
          "description": "scattered clouds",
          "icon": "03d"
        }
      ],
      "clouds": {
        "all": 47
      },
      "wind": {
        "speed": 4.85,
        "deg": 302,
        "gust": 6.88
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2024-04-16 03:00:00"
    },
    {
      "dt": 1713247200,
      "main": {
        "temp": 313.72,
        "feels_like": 311.59,
        "temp_min": 313.72,
        "temp_max": 313.72,
        "pressure": 1006,
        "sea_level": 1006,
        "grnd_level": 993,
        "humidity": 14,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 802,
          "main": "Clouds",
          "description": "scattered clouds",
          "icon": "03d"
        }
      ],
      "clouds": {
        "all": 27
      },
      "wind": {
        "speed": 5.7,
        "deg": 285,
        "gust": 7.56
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2024-04-16 06:00:00"
    },
    {
      "dt": 1713258000,
      "main": {
        "temp": 315.21,
        "feels_like": 312.75,
        "temp_min": 315.21,
        "temp_max": 315.21,
        "pressure": 1002,
        "sea_level": 1002,
        "grnd_level": 989,
        "humidity": 12,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 801,
          "main": "Clouds",
          "description": "few clouds",
          "icon": "02d"
        }
      ],
      "clouds": {
        "all": 20
      },
      "wind": {
        "speed": 6.52,
        "deg": 278,
        "gust": 8.24
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2024-04-16 09:00:00"
    },
    {
      "dt": 1713268800,
      "main": {
        "temp": 313.73,
        "feels_like": 311.13,
        "temp_min": 313.73,
        "temp_max": 313.73,
        "pressure": 1002,
        "sea_level": 1002,
        "grnd_level": 989,
        "humidity": 12,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 802,
          "main": "Clouds",
          "description": "scattered clouds",
          "icon": "03d"
        }
      ],
      "clouds": {
        "all": 33
      },
      "wind": {
        "speed": 7.12,
        "deg": 274,
        "gust": 8.44
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "d"
      },
      "dt_txt": "2024-04-16 12:00:00"
    },
    {
      "dt": 1713279600,
      "main": {
        "temp": 308.29,
        "feels_like": 305.94,
        "temp_min": 308.29,
        "temp_max": 308.29,
        "pressure": 1004,
        "sea_level": 1004,
        "grnd_level": 991,
        "humidity": 16,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 802,
          "main": "Clouds",
          "description": "scattered clouds",
          "icon": "03n"
        }
      ],
      "clouds": {
        "all": 50
      },
      "wind": {
        "speed": 4.94,
        "deg": 275,
        "gust": 12.2
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2024-04-16 15:00:00"
    },
    {
      "dt": 1713290400,
      "main": {
        "temp": 306.81,
        "feels_like": 304.54,
        "temp_min": 306.81,
        "temp_max": 306.81,
        "pressure": 1005,
        "sea_level": 1005,
        "grnd_level": 991,
        "humidity": 17,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 802,
          "main": "Clouds",
          "description": "scattered clouds",
          "icon": "03n"
        }
      ],
      "clouds": {
        "all": 46
      },
      "wind": {
        "speed": 5.76,
        "deg": 289,
        "gust": 13.8
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2024-04-16 18:00:00"
    },
    {
      "dt": 1713301200,
      "main": {
        "temp": 305.21,
        "feels_like": 303.13,
        "temp_min": 305.21,
        "temp_max": 305.21,
        "pressure": 1004,
        "sea_level": 1004,
        "grnd_level": 990,
        "humidity": 19,
        "temp_kf": 0
      },
      "weather": [
        {
          "id": 803,
          "main": "Clouds",
          "description": "broken clouds",
          "icon": "04n"
        }
      ],
      "clouds": {
        "all": 71
      },
      "wind": {
        "speed": 6.63,
        "deg": 308,
        "gust": 15.1
      },
      "visibility": 10000,
      "pop": 0,
      "sys": {
        "pod": "n"
      },
      "dt_txt": "2024-04-16 21:00:00"
    }
  ],
  "city": {
    "id": 1275683,
    "name": "Bijnaur",
    "coord": {
      "lat": 26.7746,
      "lon": 80.9581
    },
    "country": "IN",
    "population": 0,
    "timezone": 19800,
    "sunrise": 1712880905,
    "sunset": 1712926699
  }
}