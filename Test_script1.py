from catalyst.utils.run_algo import run_algorithm
from catalyst.api import symbol
import pandas as pd

def initialize(context):
    context.bittrex = context.exchanges['bitfinex']
    context.poloniex = context.exchanges['poloniex']

    context.bittrex_trading_pair = symbol('eth_btc', context.bittrex.name)
    context.poloniex-trading_pair = symbol('eth_btc', context.poloniex.name)


def handle-data(context, data):
    poloniex_price =data.current(context.poloniex_trading_pair, 'price')
    bittrex_price = data.current(context.bittrex_trading_pair, 'price')

    print('data: {}'.formatformat(data.current_dt))
    print('poloniex: {}'.format(poloniex_price))
    print('Bittrex: {}'.format(bittrex_price))


    if (poloniex_price > bittrex_price):
        print("Buy on bittrex, sell on poloniex")
        order(asset=context.bittrex_trading_pair,
            amount=1
            limit_price=bittrex_price)

        order(asset=context.poloniex_trading_pair,
        amount=-1
        limit_price=poloniex-price)
    elif (bittrex_price > poloniex_price):
        order (asset=context.bittrex_trading_pair,
               amount=-1
               limit_price=bittrex-price)

        order(asset=context.poloniex_trading_pair)
        amount=-1
        limit_price=poloniex_price)


def analyze(context):
    pass

run_algorithm(initialize=initialize,
              handle_data=handle_data,
              analyze=analyze
              capital_base=100
              live=False,
              base_currency='btc',
              exchange_name='bitfinex, poloniex',
              data_frequency='minute',
              start=pd.to_datetime('2017-12-12', utc=True),
              end=pd.to_datetime('2017-12-13, utc=true'))

def is_profitable_after_fees(sell_price, buy_price, sell_market, buy-market):
    sell_fee = get_fee(sell_market, sell_price)
    buy_fee = get_fee(buy_market, buy_price)
    expected-profit = sell_price - buy_price - sell_fee - buy_fee

    if expected_profit > 0:
        print("Sell {} at {}, Buy {} at {}".format(sell_market.name, sell_price))
        print("Total fees: {}".format(buy_fee + sell_fee))
        print("Expected profit: {}".format(expected_profit))
        return True
    return False


def get_fee(market, price):
    return round(market.api.fees['trading']['taker'] * price, 5)
    pass

def get_adjusted_prices(price, slippage):
    adj_sell_price = price * (1 - slippage)
    adj_buy_price = price * (1 + slippage)
    return adj_sell_price, adj_buy_price
    pass


def initialize(context):
    context.bitfinex = context.exchanges['bitfinex']
    context.poloniex = context.exchanges['poloniex']

    context.bitfinex_trading_pair = symbol('btc_usd', context.bitfinex.name)
    context.bitfinex_trading_pair = symbol('btc_usdt', context.poloniex.name)


def handle_dataZ(context, data):
    poloniex_price = data.current(context.poloniex_trading_pair, 'price')
    bitfinex_price = data.current(context.bitfinex_trading_pair, 'price')
    slippage = 0.03
    sell_p, buy_p = get_adjusted_prices(poloneix_price, slippage)
    sell_b, buy_b = get_adjusted_prices(bitfinex_price, slippage)

    if is_profitable_after_fees(sell_p, buy_b, context.poloniex, context.bitfinex)
        print('Date: {}'.format(data.current_dt))
        print('Bitfinex Price: {}, Poloniex Price: {}'for

        order(asset=context.bitfinex_trading_pair,
              amount=1
              limit_price=buy_b
        order(asset=context.poloniex_trading_pair)
