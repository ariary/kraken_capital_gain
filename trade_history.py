import pickle
import kraken_handler
import trades_handler

# RETRIEVING TRADES
trades_history = {}

krakenAPI = kraken_handler.KrakenHandler("./kraken.key")
trades_history.update(krakenAPI.pull_trades_last_month())
pickle.dump(trades_history, open("pickles/last_month.p", "wb"))


# PARSING TRADES
parser = trades_handler.TradesHandler(trades_history)
etc_trades = parser.get_trades_for("XETCZEUR")

# ANALYZING TRADES
print("ETC Analysis:")
buy, sell = parser.get_buy_and_sell_costs(etc_trades)
print("BUY: " + str(buy))
print("SELL: " + str(sell))
print("traded pairs:")
pairs = parser.get_pairs()
print(pairs)
print("Overview:\n" + str(parser.report()))
