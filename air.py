import requests

def interpret(pm25):
    if pm25 <= 50:
        return "Good"
    elif pm25 <= 100:
        return "Moderate"
    else:
        return "Unhealthy"


url = "https://air-quality-api.open-meteo.com/v1/air-quality?latitude=12.92&longitude=79.13&current=pm2_5"

response = requests.get(url)
data = response.json()

pm25 = data['current']['pm2_5']
print("Vellore PM2.5 right now:", pm25)
print("Air quality:", interpret(pm25))
