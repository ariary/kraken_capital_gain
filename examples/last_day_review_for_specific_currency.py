import os
import sys
import inspect
import pickle

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
import kraken_handler
import trades_handler


if len(sys.argv) < 2:
    print(
        "Usage: python last_day_review_for_specific_currency.py pair\nPairs: XLTCZEUR, XTZEUR, XXBTZEUR, XETCZEUR, XXMRZEUR, XETHZEUR, BCHEUR"
    )
    sys.exit(1)
else:
    print(
        " DISCLAIMER: print only result for trade (ie positions).\
        Also if you have not closed the position the amount of the position is considered as a loss"
    )
    # RETRIEVING TRADES
    history = {}

    krakenAPI = kraken_handler.KrakenHandler("../kraken.key")
    history.update(krakenAPI.pull_trades_last_day())
    pickle.dump(history, open("../pickles/last_day.p", "wb"))

    # PARSING TRADES
    parser = trades_handler.TradesHandler(history)
    trades = parser.get_trades_for(sys.argv[1])

    # ANALYZING TRADES
    print(sys.argv[1] + " Analysis:")
    buy, sell = parser.get_buy_and_sell_costs(trades)
    print("BUY: " + str(buy))
    print("SELL: " + str(sell))
    print("BENEFITS:" + str(sell - buy))
