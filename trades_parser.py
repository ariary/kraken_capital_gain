class trades_parser(object):
    """docstring for ClassName"""

    def __init__(self, trades_dict):
        self.trades_dict = trades_dict

    def get_trades_for(self, currency_str):
        """
		return all th trade for a specific currency
		"""
        result = {}
        for trade_id, trade in self.trades_dict.items():
            pair = trade["pair"]
            if pair == currency_str:
                result.update({trade_id: trade})

        return result
