#Descripcion: Obtener el precio actual del Bitcoin
from forex_python.bitcoin import BtcConverter
from termcolor import colored
URL = 'https://api.coinmarketcap.com/v1/ticker/'

#Obtiene el ultimo precio del bitcoin
def obtener_ultimo_precio_bitcoin():
    btc = BtcConverter(force_decimal=True)
    return btc.get_latest_price('MXN')

#Desarrolla e imprime en tiempo real precio de bitcoin
def main():
    ultimo_precio = -1
    while True:
        precio = obtener_ultimo_precio_bitcoin()
        if precio != ultimo_precio:
            if precio < ultimo_precio:
                print('BTC: $', colored("{:.2f}".format(precio), "red"), end=" ")
                print("MXN.", "--> Diferencia: $", end=" ")
                print(colored("{:.2f}".format(precio-ultimo_precio), "red"), "MXN")
                ultimo_precio = precio
            else:
                print('BTC: $', colored("{:.2f}".format(precio), "green"), end=" ")
                print("MXN.", "--> Diferencia: $", "{:.2f}".format(precio - ultimo_precio))
                ultimo_precio = precio

main()
