"""funciones muy chidas jejej"""
import time as t
import priv_REST_API_Balance_Info as priv
import precio_btc_real as btc



def balance_actual():
    """regresa el balance total en mxn"""
    btc_mxn = btc.ultimo_precio_ask()*priv.balance_btc()
    mxn_priv = priv.balance_mxn()
    return btc_mxn + mxn_priv


def balance_btc_en_mxn():
    """regresa el balance de bitcoins en mxn
    el precio está dado por la oferta actual ask"""
    return btc.ultimo_precio_ask()*priv.balance_btc()


def balance_mxn_en_mxn():
    """regresa el balance de mxn en bitso"""
    return priv.balance_mxn()

while True:
    #os.system("clear")
    print("\tSaldo actual:")
    print("\t$" + str(round(balance_actual(), 2))+ " mxn" +
          "\tBTC: $" + str(btc.ultimo_precio_ask()) + " mxn\n")
    t.sleep(10)
