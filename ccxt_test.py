import ccxt

cb = ccxt.coinbasepro()
bn = ccxt.binance()

cb_bids = cb.fetch_order_book('BAT/USDC')['bids']
bn_asks = bn.fetch_order_book('BAT/USDC')['asks']

print('Buying from Binance')
print(bn_asks)

print('Selling from CoinbasePro')
print(cb_bids)
