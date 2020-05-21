import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
import kraken_handler


MAKER_FEE = 0.0016
TAKER_FEE = 0.0026

# Retrieve open position
krakenAPI = kraken_handler.KrakenHandler("../kraken.key")
open_positions = krakenAPI.get_open_orders()
for _, order in open_positions["result"].items():
    coin = order["pair"]
    print("For " + coin + ":")
    if order["type"] == "sell":
        print("\t Short position: Vol " + order["vol"])
    else:
        print("\t Long position: Vol " + order["vol"])
    # Fee
    pnl = float(order["net"])
    # margin fees (opening + rollover)
    pnl -= float(order["fee"])
    # Position fees (open & Close if we do now)
    opening = (
        float(order["cost"]) * TAKER_FEE * 2
    )  # fee opening position (as a taker), 2 for leverage
    pnl -= opening
    close_position = float(order["value"]) * 0.0026 * 2
    print("\t Profit & Loss: " + str(pnl))
