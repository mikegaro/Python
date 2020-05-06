#!/usr/bin/python

import sys
import time
import hmac
import hashlib
import requests
import json

#   PARA HACER USO DE LA REST API PRIVADA, Bitso
#   siempre solicitara una 'signature' encriptada en formato
#   HMAC SHA256 concatenada con la 'bitso key' de la API y la
#   'bitso_secret', ademas de un numero creciente y unico para cada
#   vez que llamamos a la API

bitso_key = 'NjeZbAXHKy' #se proporciona en el sitio web
bitso_secret = '4fd5e392f1ab9381bd26939617110dd0' #llave unica secreta al momento de crear la api

def get_request():
    http_method = "GET"
    request_path = "/v3/balance/"
    nonce = str(int(round(time.time() * 1000))) #numero creciente y unico, utiliza el tiempo como parametro
    message = nonce+http_method+request_path
    #el signature debe estar encriptado
    signature = hmac.new(bitso_secret.encode('utf-8'),message.encode('utf-8'),hashlib.sha256).hexdigest()
    auth_header = 'Bitso %s:%s:%s' % (bitso_key,nonce,signature)
    response = requests.get('https://api.bitso.com' + request_path, headers={"Authorization": auth_header})
    response_json = response.json()
    return response_json

def post_request(parametros):
    http_method = "POST"
    request_path ="/v3/orders/"
    nonce = str(int(round(time.time() * 1000))) #numero creciente y unico, utiliza el tiempo como parametro
    message = nonce+http_method+request_path+json.dumps(parametros)
    signature = hmac.new(bitso_secret.encode('utf-8'),message.encode('utf-8'),hashlib.sha256).hexdigest()
    auth_header = 'Bitso %s:%s:%s' % (bitso_key,nonce,signature)
    respuesta = requests.post("https://api.bitso.com" + request_path, json = parametros, headers={"Authorization": auth_header})
    return respuesta

def balance_btc():
    request = get_request()
    totalbtc = request['payload']['balances'][2]['total']
    return float(totalbtc)

def balance_mxn():
    request = get_request()
    totalmxn = request['payload']['balances'][11]['total']
    return float(totalmxn)
