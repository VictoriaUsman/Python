import requests


ISS = requests.get(url = "http://api.open-notify.org/iss-now.json")
ISS = ISS.json()
longitude = ISS["iss_position"]["longitude"]
latitude = ISS["iss_position"]["latitude"]

ISS_Position = (latitude, longitude)
print(ISS_Position)