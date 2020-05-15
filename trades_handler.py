class TradesHandler:
    """Class enable us tu do some action on Trades"""

    def __init__(self, trades_dict):
        self.trades_dict = trades_dict
        self.pairs = set()

        # Initialize pairs traded
        for _, trade in self.trades_dict.items():
            self.pairs.add(trade["pair"])

    def get_trades_for(self, currency_str):
        """return all the trades for a specific currency"""
        result = {}
        for trade_id, trade in self.trades_dict.items():
            pair = trade["pair"]
            if pair == currency_str:
                result.update({trade_id: trade})

        return result

    def get_buy_and_sell_costs(self, trades):
        """Retrieve the money spend to buy a currency, and the money received when selling it"""
        buy_cost = 0
        sell_cost = 0

        for _, trade in trades.items():
            if trade["type"] == "buy":
                buy_cost += float(trade["cost"])
            else:
                sell_cost += float(trade["cost"])

        return buy_cost, sell_cost

    def get_pairs(self):
        """ Get the pair trade for the trades history given"""
        return self.pairs

    def report(self):
        """
        Do the same job as get_buy_and_host_costs for all currencies traded
        TODO: Check if set is empty
        TODO: Find a right substraction
        """
        result = {}
        result_buy = 0
        result_sell = 0
        result_outcome = 0
        for pair in self.pairs:
            trades = self.get_trades_for(pair)
            buy, sell = self.get_buy_and_sell_costs(trades)
            outcome = sell - buy
            result_pair = {"buy": buy, "sell": sell, "outcome": outcome}
            result.update({pair: result_pair})
            result_buy += buy
            result_sell += sell
            result_outcome += outcome

        # Add global results
        all = {"buy": result_buy, "sell": result_sell, "outcome": result_outcome}
        result.update({"all": all})
        return result

    def get_trades(self):
        return self.trades_dict
