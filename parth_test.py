import ccxt
import json

cb = ccxt.coinbasepro()
bn = ccxt.binance()

ex_data = {}
with open('exchanges.json') as json_file:
    ex_data = json.load(json_file)

ask_exchanges
print(ex_data)