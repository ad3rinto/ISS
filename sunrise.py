import requests

params = {
    "lat": 53.3801,
    "lng": 2.1932
}

response = requests.get("https://api.sunrise-sunset.org/json", params=params)
response.raise_for_status()
data = response.json()
sunrise = (data["results"]["sunrise"])
sunset = (data["results"]["sunset"])
daily = (sunrise, sunset)
print(daily)
