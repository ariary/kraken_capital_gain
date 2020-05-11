import krakenex

import datetime
import calendar
import time


class kraken_handler(object):
    """docstring for kraken_handler"""

    def __init__(self, key_path):
        self.krakenAPI = krakenex.API()
        self.krakenAPI.load_key(key_path)

        self.trades = {}

    def pull_trades(self):
        for i in range(1, 11):
            start_date = datetime.datetime(2020, i + 1, 1)
            end_date = datetime.datetime(2020, i + 2, 30)
            req_history = self.krakenAPI.query_private(
                "TradesHistory", self.__date(start_date, end_date, 1)
            )
            time.sleep(0.25)
            self.trades.update(req_history["result"]["trades"])

    def get_trades(self):
        return self.trades

    # takes date and returns nix time
    def __date_nix(self, str_date):
        return calendar.timegm(str_date.timetuple())

    # takes nix time and returns date
    def __date_str(self, nix_time):
        return datetime.datetime.fromtimestamp(nix_time).strftime("%m, %d, %Y")

    # return formatted TradesHistory request data
    def __date(self, start, end, ofs):
        req_data = {
            "type": "all",
            "trades": "true",
            "start": str(self.__date_nix(start)),
            "end": str(self.__date_nix(end)),
            "ofs": str(ofs),
        }
        return req_data
