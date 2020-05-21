import os
import sys
import inspect
import pickle

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
import kraken_handler
import orders_handler


if len(sys.argv) < 2:
    print(
        "Usage: python last_day_review_for_specific_currency.py pair\nPairs: XLTCZEUR, XTZEUR, XXBTZEUR, XETCZEUR, XXMRZEUR, XETHZEUR, BCHEUR"
    )
    sys.exit(1)
else:
    print(
        " DISCLAIMER: \n\
        print only result for closed orders.\n\
        Also if you have not closed the position the volume of the position is not taking into account\n\
        For open positions look at pnl_with_fees.py\n"
    )
    # RETRIEVING CLOSED ORDERS
    history = {}

    krakenAPI = kraken_handler.KrakenHandler("../kraken.key")
    history.update(krakenAPI.pull_orders_last_day())
    pickle.dump(history, open("../pickles/last_day.p", "wb"))

    # PARSING ORDERS
    parser = orders_handler.OrdersHandler(history)
    orders = parser.get_orders_for(sys.argv[1])

    # ANALYZING ORDERS
    print(sys.argv[1] + " Analysis:")
    buy, sell = parser.get_buy_and_sell_costs(orders)
    print("BUY: " + str(buy))
    print("SELL: " + str(sell))
    print("BENEFITS:" + str(sell - buy))
