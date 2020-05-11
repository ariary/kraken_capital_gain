import kraken_handler
import pickle
import trades_parser


"""
RETRIEVING TRADES
"""
trades_history = {}

# krakenAPI = kraken_handler.kraken_handler("./kraken.key")
# krakenAPI.pull_trades()
# trades_history.update(krakenAPI.get_trades())
# pickle.dump(trades_history, open("pickles/trades_history.p", "wb"))

trades_history.update(pickle.load(open("pickles/trades_history.p", "rb")))

"""
PARSING TRADES
"""
parser = trades_parser.trades_parser(trades_history)
eth_trades = parser.get_trades_for("XETHZEUR")
print(eth_trades)

"""
ANALYZING TRADES
"""
