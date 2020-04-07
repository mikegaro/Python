import requests
import sys
URL = 'https://api.bitso.com/v3/ticker/'

def ultimo_precio_criptomoneda():
    respuesta = requests.get(URL)
    respuesta_json = respuesta.json()
    return float(respuesta_json['payload'][0]['ask'])

def main():
    print('\n\tConectando con el servidor de BITSO\n')
    ultimo_precio = -1
    while True:
        precio_actual = ultimo_precio_criptomoneda()
        precio_actual = round(precio_actual,2)

        if precio_actual != ultimo_precio:
            if precio_actual < ultimo_precio:
                print('\033[1;31;40m \tBTC: $ ' + str(precio_actual) + " MXN")
                ultimo_precio = precio_actual
            else:
                print('\033[1;32;40m \tBTC: $ ' + str(precio_actual) + " MXN")
                ultimo_precio = precio_actual

main()
