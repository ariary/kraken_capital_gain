class TradesHandler:
    """Class enable us tu do some action on Trades"""

    def __init__(self, trades_dict):
        self.trades_dict = trades_dict

    def get_trades_for(self, currency_str):
        """return all the trades for a specific currency"""
        result = {}
        for trade_id, trade in self.trades_dict.items():
            pair = trade["pair"]
            if pair == currency_str:
                result.update({trade_id: trade})

        self.trades_dict = result

    def get_buy_and_host_costs(self):
        """Retrieve the money spend to buy a currency, and the money received when selling it"""
        buy_cost = 0
        sell_cost = 0

        for _, trade in self.trades_dict.items():
            if trade["type"] == "buy":
                buy_cost += float(trade["cost"])
            else:
                sell_cost += float(trade["cost"])

        return buy_cost, sell_cost

    def get_Trades(self):
        return self.trades_dict
