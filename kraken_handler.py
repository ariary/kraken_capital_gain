import datetime
import calendar
import krakenex


class KrakenHandler:
    """docstring for kraken_handler"""

    def __init__(self, key_path):
        self.kraken_api = krakenex.API()
        self.kraken_api.load_key(key_path)

    def pull_orders_from_to(self, start, end):
        """retrieve your own kraken closed orders using krakenex"""
        req_history = self.kraken_api.query_private(
            "ClosedOrders", self.__date(start, end, 1)
        )
        return req_history["result"]["closed"]

    def pull_orders_from(self, start):
        """pull closed orders from a starting point to now"""
        now = datetime.datetime.now()
        return self.pull_order_from_to(start, now)

    def pull_orders_to(self, end):
        """pull closed orders until a specfic date """
        start = datetime.datetime(2017, 8, 1)  # from August 2017
        return self.pull_orders_from_to(start, end)

    def pull_orders_last_year(self):
        """ return all closed orders from last year"""
        return self.__pull_timedelta(days=365)

    def pull_orders_last_month(self):
        """ return all closed orders from last year"""
        return self.__pull_timedelta(days=31)

    def pull_orders_last_day(self):
        """ return all closed orders from the last 24 hours"""
        return self.__pull_timedelta(hours=24)

    def pull_orders_last_hour(self):
        """ return all  closed orders from last hour"""
        return self.__pull_timedelta(hours=1)

    def get_open_positions(self):
        """ use the Kraken API to retrieve the open positions """
        req_data = {"docalcs": "true"}
        req_history = self.kraken_api.query_private("OpenPositions", req_data)
        return req_history

    def __date_nix(self, str_date):
        return calendar.timegm(str_date.timetuple())

    def __date_str(self, nix_time):
        return datetime.datetime.fromtimestamp(nix_time).strftime("%m, %d, %Y")

    def __date(self, start, end, ofs):
        req_data = {
            "type": "all",
            "trades": "false",
            "start": str(self.__date_nix(start)),
            "end": str(self.__date_nix(end)),
            "ofs": str(ofs),
        }
        return req_data

    def __pull_timedelta(self, **args):
        """
        Pull the closed orders with a specified delta from now
        Call @datetime.timedelta()
        Available delta are thus the same as timedelta:
        timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
        """
        now = datetime.datetime.now()
        delta = now - datetime.timedelta(**args)
        return self.pull_orders_from_to(delta, now)
