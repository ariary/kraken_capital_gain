import kraken_handler
import pickle

trades_history = {}
krakenAPI = kraken_handler.kraken_handler("/home/kali/Documents/keys/kraken.key")
krakenAPI.pullTrades()
trades_history.update(krakenAPI.getTrades())

print(trades_history)
pickle.dump(trades_history, open("./pickles/trades_history.p", "wb"))
# trades_history.update(pickle.load( open( "./pickles/trade_history.p", "rb" ) ))

# for i in range(1,11):
#     start_date = datetime.datetime(2020, i+1, 1)
#     end_date = datetime.datetime(2020, i+2, 30)

# year = timedelta(days=365)
# print(str(year))

# sdate = datetime.datetime(2008, 8, 15)   # start date
# edate = datetime.datetime(2010, 9, 15)   # end date

# delta = edate - sdate       # as timedelta

# for i in range(delta.days + 1):
#     day = sdate + timedelta(days=i)
#     print(day)
