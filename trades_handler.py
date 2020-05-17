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

        # Search Margin trade position to ignore the trades used to close this position
        buy_cost, sell_cost, blacklist = self.__search_margin_position(trades)

        for id, trade in trades.items():
            if id not in blacklist:  # Not a margin position
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

    def __search_margin_position(self, trades):
        """
        Search the margin positions in the dictionnary trades
        Update the Buy/Sell costs accordingly
        Update a list of trades involved in the margin position
        """
        buy_cost = 0
        sell_cost = 0
        blacklist = []

        for id, trade in trades.items():
            if "trades" in trade.keys():
                # update list of trades involved in the position
                for close_trade in trade.get("trades"):
                    blacklist.append(close_trade)
                blacklist.append(id)

                # update buy/sell costs
                if trade["type"] == "buy":
                    buy_cost += float(trade["cost"])
                    sell_cost += float(trade["ccost"])
                else:
                    buy_cost += float(trade["ccost"])
                    sell_cost += float(trade["cost"])
        return buy_cost, sell_cost, blacklist
