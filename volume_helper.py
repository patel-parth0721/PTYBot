import ccxt


def total_volume_bids_btc(exchange, sym):
    total = 0
    bids = exchange.fetch_order_book(sym)['bids']
    print(bids)
    for bid in bids:
        total += bid[1]
    return total


def total_volume_bids_usd(exchange, sym):
    total = 0
    bids = exchange.fetch_order_book(sym)['bids']
    print(bids)
    for bid in bids:
        total += bid[0]
    return total


def total_volume_asks_btc(exchange, sym):
    total = 0
    asks = exchange.fetch_order_book(sym)['asks']
    print(asks)
    for ask in asks:
        total += ask[1]
    return total


def total_volume_asks_usd(exchange, sym):
    total = 0
    asks = exchange.fetch_order_book(sym)['asks']
    print(asks)
    for ask in asks:
        total += ask[0]
    return total

