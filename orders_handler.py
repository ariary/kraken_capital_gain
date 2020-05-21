class OrdersHandler:
    """Class enable us tu do some action on Orders"""

    def __init__(self, orders_dict):
        self.orders_dict = orders_dict
        self.pairs = set()

        # Clean dict (remove canceled orders)
        self.__clean_orders()

        # Initialize pairs orderd
        for _, order in self.orders_dict.items():
            self.pairs.add(order["descr"]["pair"])

    def get_orders_for(self, currency_str):
        """return all the orders for a specific currency"""
        result = {}
        for order_id, order in self.orders_dict.items():
            pair = order["descr"]["pair"]
            if pair == currency_str:
                result.update({order_id: order})

        return result

    def get_buy_and_sell_costs(self, orders):
        """Retrieve the money spend to buy a currency, and the money received when selling it"""

        buy_cost = sell_cost = 0
        for _, order in orders.items():
            if order["descr"]["type"] == "buy":
                buy_cost += float(order["cost"])
            else:
                sell_cost += float(order["cost"])

        return buy_cost, sell_cost

    def get_pairs(self):
        """ Get the pair order for the orders history given"""
        return self.pairs

    def report(self):
        """
        Do the same job as get_buy_and_host_costs for all currencies orderd
        TODO: Check if set is empty
        """
        result = {}
        result_buy = 0
        result_sell = 0
        result_outcome = 0
        for pair in self.pairs:
            orders = self.get_orders_for(pair)
            buy, sell = self.get_buy_and_sell_costs(orders)
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

    def get_orders(self):
        return self.orders_dict

    def __clean_orders(self):
        """ Cancel canceled orders from the orders dictionnary"""
        canceled_id = []
        for order_id, order in self.orders_dict.items():
            if order["status"] == "canceled":
                canceled_id.append(order_id)
        for id in canceled_id:
            del self.orders_dict[id]
