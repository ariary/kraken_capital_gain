#!/usr/bin/env python

# This file is part of krakenex.
# Licensed under the Simplified BSD license. See `examples/LICENSE.txt`.

# Saves trade history to CSV file.
#
# WARNING: submits a lot of queries in rapid succession!

# Maintainer: Austin.Deric@gmail.com (@AustinDeric on github)

import krakenex

import datetime
import calendar

import pickle


# takes date and returns nix time
def date_nix(str_date):
    return calendar.timegm(str_date.timetuple())


# takes nix time and returns date
def date_str(nix_time):
    return datetime.datetime.fromtimestamp(nix_time).strftime("%m, %d, %Y")


# return formatted TradesHistory request data
def date(start, end, ofs):
    req_data = {
        "type": "all",
        "trades": "true",
        "start": str(date_nix(start)),
        "end": str(date_nix(end)),
        "ofs": str(ofs),
    }
    return req_data


k = krakenex.API()
k.load_key("kraken.key")

data = []
count = 0
# for i in range(1,11):
# start_date = datetime.datetime(2020, i+1, 1)
# end_date = datetime.datetime(2020, i+2, 29)
# th = k.query_private('TradesHistory', date(start_date, end_date, 1))
# time.sleep(.25)
# th = pickle.load( open( "./pickles/trade_history.p", "rb" ) )
# print(th)
# th_error = th['error']
# try:
#     if int(th['result']['count'])>0:
#         count += th['result']['count']
#         sell = 0
#         buy = 0
#         for trade_id,trade_content in th['result']['trades'].items():
#             pair = trade_content['pair']
#             if pair == 'XETHZEUR':
#                 if trade_content['type'] == 'sell':
#                     sell += trade_content['cost']
#                 else:
#                     buy += trade_content['cost']
#                 # dataf= pd.DataFrame.from_records(trade_content,index=[0])
#                 # data.append(pd.DataFrame.from_dict(dataf).transpose())
# except Exception as e:
#     print(e)

th = pickle.load(open("./pickles/trade_history.p", "rb"))
sell = 0
buy = 0
print(th)
th_error = th["error"]
try:
    if int(th["result"]["count"]) > 0:
        count += th["result"]["count"]
        for trade_id, trade_content in th["result"]["trades"].items():
            pair = trade_content["pair"]
            if pair == "XETHZEUR":
                if trade_content["type"] == "sell":
                    sell += float(trade_content["cost"])
                else:
                    buy += float(trade_content["cost"])
                # dataf= pd.DataFrame.from_records(trade_content,index=[0])
                # data.append(pd.DataFrame.from_dict(dataf).transpose())
except Exception as e:
    print(e)

print("Buy: " + str(buy))
print("Sell: " + str(sell))
# trades = pd.DataFrame
# trades = pd.concat(data, axis = 0)
# #trades = trades.sort_values(columns='time', ascending=True)
# trades = trades.sort_values(by='time', ascending=True)
# # print("Saving CSV...")
# # trades.to_csv('data.csv')
# print("Saving EXCEL...")
# trades.to_excel('data.xlsx')
