import datetime
import calendar
import krakenex


class KrakenHandler:
    """docstring for kraken_handler"""

    def __init__(self, key_path):
        self.kraken_api = krakenex.API()
        self.kraken_api.load_key(key_path)

    def pull_trades_from_to(self, start, end):
        """retrieve your own kraken trades using krakenex"""
        req_history = self.kraken_api.query_private(
            "TradesHistory", self.__date(start, end, 1)
        )
        return req_history["result"]["trades"]

    def pull_trades_from(self, start):
        """pull trades from a starting point to now"""
        now = datetime.datetime.now()
        return self.pull_trades_from_to(start, now)

    def pull_trades_to(self, end):
        """pull trades until a specfic date """
        start = datetime.datetime(2017, 8, 1)  # from August 2017
        return self.pull_trades_from_to(start, end)

    def get_trades(self):
        """get the trades"""
        return self.trades

    def __date_nix(self, str_date):
        return calendar.timegm(str_date.timetuple())

    def __date_str(self, nix_time):
        return datetime.datetime.fromtimestamp(nix_time).strftime("%m, %d, %Y")

    def __date(self, start, end, ofs):
        req_data = {
            "type": "all",
            "trades": "true",
            "start": str(self.__date_nix(start)),
            "end": str(self.__date_nix(end)),
            "ofs": str(ofs),
        }
        return req_data
