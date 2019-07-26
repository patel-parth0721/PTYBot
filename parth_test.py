import ccxt
import json
import json_loader

cbp = ccxt.coinbasepro()
bnb = ccxt.binance()

json_file = "exchanges.json"
ex_data = json_loader.load_json_data(json_file)



ask_exc_obj = {'bnb': bnb}
bid_exc_obj = {'cbp': cbp}

for exc in ex_data['ask_exchanges']:
    cur_exc = ask_exc_obj[exc['name']]
    print(cur_exc)
    for sym in exc['pairs']:
        print(sym)

print()
print()

for exc in ex_data['bid_exchanges']:
    cur_exc = bid_exc_obj[exc['name']]
    print(cur_exc)
    for sym in exc['pairs']:
        print(sym)