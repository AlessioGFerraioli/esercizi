import json
import requests

risposta = requests.get('https://api.open-meteo.com/v1/forecast?latitude=40.8011&longitude=14.5407&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max&timezone=auto&forecast_days=1')

if risposta.status_code == 200:
    data = risposta.json()
    forecast = data['forecast']['forecast_day'][0]
else: 
    print("Errore server")

temperature_max = forecast['temperature']['max']
