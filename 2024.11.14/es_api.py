import requests
import json 

risposta = requests.get("https://api.open-meteo.com/v1/forecast?latitude=40.8011&longitude=14.5407&current=apparent_temperature")

# risposta status
print("risposta status")
print(risposta.status_code) # risposta 200 significa che la richiesta è andata a buon fine
print()

print("risposta text")
risposta_text = risposta.text
print()

print("risposta json")
risposta_json = json.loads(risposta_text)
print(risposta_json)
print()

print(f"previsione ora corrente: {risposta_json['current']['apparent_temperature']}°C")