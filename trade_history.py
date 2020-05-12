import pickle
import kraken_handler
import trades_handler

# RETRIEVING TRADES
trades_history = {}

# krakenAPI = kraken_handler.KrakenHandler("./kraken.key")
# krakenAPI.pull_trades()
# trades_history.update(krakenAPI.get_trades())
# pickle.dump(trades_history, open("pickles/trades_history.p", "wb"))

trades_history.update(pickle.load(open("pickles/trades_history.p", "rb")))


# PARSING TRADES
parser = trades_handler.TradesHandler(trades_history)
parser.get_trades_for("XETHZEUR")

# ANALYZING TRADES
buy, sell = parser.get_buy_and_host_costs()
print("BUY: " + str(buy))
print("SELL: " + str(sell))
