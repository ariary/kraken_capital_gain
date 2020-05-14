import datetime
import pickle
import kraken_handler
import trades_handler

# RETRIEVING TRADES
trades_history = {}

krakenAPI = kraken_handler.KrakenHandler("./kraken.key")
start = datetime.datetime(2017, 8, 1)
trades_history.update(krakenAPI.pull_trades_from(start))
pickle.dump(trades_history, open("pickles/trades_history_from.p", "wb"))
th_last_year = krakenAPI.pull_trades_last_year()
pickle.dump(th_last_year, open("pickles/last_year.p", "wb"))
# trades_history.update(pickle.load(open("pickles/trades_history_from.p", "rb")))


# PARSING TRADES
parser = trades_handler.TradesHandler(trades_history)
parser.get_trades_for("XETCZEUR")

# ANALYZING TRADES
buy, sell = parser.get_buy_and_host_costs()
print("BUY: " + str(buy))
print("SELL: " + str(sell))
