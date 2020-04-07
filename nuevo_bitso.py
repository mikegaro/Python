import requests
import colored
from colored import stylize
URL = 'https://api.bitso.com/v3/ticker/'

def ultimo_precio_criptomoneda():
    respuesta = requests.get(URL)
    respuesta_json = respuesta.json()
    return float(respuesta_json['payload'][0]['vwap'])

def main():

    ultimo_precio = -1
    while True:
        precio_actual = ultimo_precio_criptomoneda()

        if precio_actual != ultimo_precio:
            if precio_actual < ultimo_precio:
                print(' BTC: ',round(ultimo_precio,2))
                ultimo_precio = precio_actual
            else:
                print(' BTC: ',round(ultimo_precio,2))
                ultimo_precio = precio_actual

main()
