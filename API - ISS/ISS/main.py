import requests
from datetime import datetime, timedelta
# Mail requirments
import smtplib
import ssl
from email.message import EmailMessage

MY_LAT = 26.812476
MY_LONG = 80.910011
MY_EMAIL = "dummytest.mail01t@gmail.com"
# ISS_OverHead
MY_PASSWORD = "lggojdserpigesig"
EMAIL_RECEIVER = "dummytestmial@outlook.com"


def near_me():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if (MY_LAT + 5 >= iss_latitude >= MY_LAT - 5) and (MY_LONG + 5 >= iss_longitude >= MY_LONG - 5):
        return True
    return False


def close_to_me():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    subtract_time = timedelta(hours=5, minutes=30)
    time_now = datetime.now()
    time_now = time_now - subtract_time
    print(time_now.hour)
    print(data)

    # If the ISS is close to my current position,
    # and it is currently dark
    if near_me() and sunset <= time_now.hour <= sunrise:
        return True
    return False


# Then email me to tell me to look up.
# BONUS: run the code every 60 seconds.

if close_to_me():
    connection = smtplib.SMTP()
    subject = "ISS Alert"
    body = """
    ISS upar hai.... XD !!
    """
    em = EmailMessage()
    em["From"] = MY_EMAIL
    em["To"] = EMAIL_RECEIVER
    em["Subject"] = subject
    em.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
        smtp.login(MY_EMAIL, MY_PASSWORD)
        smtp.sendmail(MY_EMAIL, EMAIL_RECEIVER, em.as_string())