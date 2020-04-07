#!/usr/bin/python

import requests
import sys
import time
import hmac
import hashlib
import requests
import json

bitso_key = 'NjeZbAXHKy'
bitso_secret = '4fd5e392f1ab9381bd26939617110dd0'
http_method = "GET"
request_path = "/v3/balance/"

 # nonce genera un numero unico y siempre creciente
 # basado en el tiempo, necesario para cada vez que
# llamamos a la API.
nonce = str(int(round(time.time() * 1000)))
message = nonce+http_method+request_path

# el signature debe ser generado creando una SHA256 HMAC usando el API Secret
signature = hmac.new(bitso_secret.encode('utf-8'),
                     message.encode('utf-8'),hashlib.sha256).hexdigest()

# las reglas para autorizar en bitso son usando el authorization header
# que se forma de la siguiente manera:
auth_header = 'Bitso %s:%s:%s' % (bitso_key,nonce,signature)

response = requests.get('https://api.bitso.com' + request_path, headers={"Authorization": auth_header})
response_json = response.json()

print("\n\tMis balances:")

for i in range(0,12):
    total = response_json['payload']['balances'][i]['total']
    if float(total) != 0:
        print("\n\t" + response_json['payload']['balances'][i]['currency'] + ": " + total)
