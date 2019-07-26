import json_loader
import ccxt
import volume_helper

def runner():
    """Runner file to trigger functions"""
    json_file = "exchanges.json"
    ex_data = json_loader.load_json_data(json_file)

    cbp = ccxt.coinbasepro()
    bnb = ccxt.binance()

    ask_exc_obj = {'bnb': bnb}
    bid_exc_obj = {'cbp': cbp}
    for exc in ex_data['ask_exchanges']:
        cur_exc = ask_exc_obj[exc['name']]
        print(cur_exc)
        for sym in exc['pairs']:
            volume_helper.total_volume_asks_btc(cur_exc, sym)

runner()
