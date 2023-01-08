import requests
from datetime import datetime

MY_LAT = 43.761539
MY_LOG = -79.411079

iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
iss_response.raise_for_status()
iss_data = iss_response.json()

iss_latitude = float(iss_data["iss_position"]["latitude"])
iss_longitude = float(iss_data["iss_position"]["longitude"])


parameters = {
    "lat": MY_LAT,
    "log": MY_LOG,
    "formatted": 0,
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
hour_now = time_now.hour

# Check conditions

if sunset < hour_now < sunrise:
    if MY_LAT-5 < iss_latitude < MY_LAT+5 and MY_LOG-5 < iss_longitude < MY_LOG+5:
        print("Look up! ISS is over you...")
else:
    print("Please wait for your turn")


