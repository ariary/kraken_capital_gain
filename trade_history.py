import pickle
import kraken_handler
import trades_handler
import trades_parser

# RETRIEVING TRADES
trades_history = {}

# krakenAPI = kraken_handler.KrakenHandler("./kraken.key")
# krakenAPI.pull_trades()
# trades_history.update(krakenAPI.get_trades())
# pickle.dump(trades_history, open("pickles/trades_history.p", "wb"))

trades_history.update(pickle.load(open("pickles/trades_history.p", "rb")))


# PARSING TRADES
parser = trades_parser.TradesParser(trades_history)
eth_trades = parser.get_trades_for("XETHZEUR")

# ANALYZING TRADES
trades_analyzer = trades_handler.TradesHandler(eth_trades)
buy, sell = trades_analyzer.get_buy_and_host_costs()
print("BUY: " + str(buy))
print("SELL: " + str(sell))
