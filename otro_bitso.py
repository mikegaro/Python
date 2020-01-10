import requests
from termcolor import colored
TICKER_API_URL = 'https://api.coinmarketcap.com/v1/ticker/'
def get_latest_crypto_price(crypto):
    response = requests.get(TICKER_API_URL+crypto)
    response_json = response.json()
    # Convert the price to a floating point number
    return float(response_json[0]['price_usd'])

def main():
  #Set last_price to -1 to indicate the last price hasn't been recorded ye
    last_price = -1

    while True:
        crypto = 'bitcoin'
        price = get_latest_crypto_price(crypto)

    #Print the price of bitcoin only if the current price is different from the last price
        if price != last_price:
            if price < last_price:
                print(' BTC: ', colored("{:.2f}".format(price), "red"))
                last_price = price #update last_price to be the current price
            else:
                print(' BTC: ', colored("{:.2f}".format(price), "green"))
                last_price = price #update last_price to be the current price
main()
