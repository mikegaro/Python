import priv_REST_API_Balance_Info as priv
import precio_btc_real as btc
import time as t
import os

def balance_actual():
    btc_mxn = btc.ultimo_precio_btc()*priv.balance_btc()
    mxn_priv = priv.balance_mxn()
    return btc_mxn + mxn_priv

def balance_btc_en_mxn():
    return btc.ultimo_precio_btc()*priv.balance_btc()

def balance_mxn_en_mxn():
    return priv.balance_mxn()

while True:
    #os.system("clear")
    print("\tSaldo actual:")
    print("\t$" + str(round(balance_actual(),2))+ " mxn" + "\tBTC: $" + str(btc.ultimo_precio_btc()) + " mxn\n")
    t.sleep(3)
