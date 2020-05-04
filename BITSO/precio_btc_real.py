import requests
import sys
URL = 'https://api.bitso.com/v3/ticker/'

def ultimo_precio_ask():
    respuesta = requests.get(URL)
    respuesta_json = respuesta.json()
    return float(respuesta_json['payload'][0]['ask'])

def ultimo_precio_bid():
    respuesta = requests.get(URL)
    respuesta_json = respuesta.json()
    return float(respuesta_json['payload'][0]['bid'])