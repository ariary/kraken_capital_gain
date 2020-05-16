import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import pickle
import kraken_handler
import trades_handler

# RETRIEVING TRADES
history = {}

krakenAPI = kraken_handler.KrakenHandler("../kraken.key")
history.update(krakenAPI.pull_trades_last_month())
pickle.dump(history, open("../pickles/last_month.p", "wb"))


# PRINTING REVIEW TRADES
parser = trades_handler.TradesHandler(history)

# print("Traded pairs:")
# for pair in parser.get_pairs():
# 	print( pair + " ")

for pair, result in parser.report().items():
    print("For " + pair)
    print("Result: " + str(result.get("outcome")))
    print("(Buy:" + str(result.get("buy")) + ", Sell: " + str(result.get("sell")) + ")")
    print("\n")
