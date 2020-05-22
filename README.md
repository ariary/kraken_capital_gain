# Kraken Capital Gain
## Description
This repo is used to know ***your capital gain using Kraken***. You can play with different parameters, e.g you can have an overview of your capital gain for a specific currency or for a specific timeframe

## Requirement

 - Python 3
 - [krakenex](https://github.com/veox/python3-krakenex) (`pip install krakenex`, thus you also need pip ;))
- a kraken APi keys ([https://support.kraken.com/hc/en-us/articles/360022839451-Generate-API-Keys](https://support.kraken.com/hc/en-us/articles/360022839451-Generate-API-Keys))

## Usage

 - `kraken_handler.py`
The class used for all interactions with the [KrakenAPI](https://www.kraken.com/fr-fr/features/api)
 - `orders_handler.py`
The class used for all the treatments of the closed positions recolted with the KrakenAPI

### `examples` directory
In the directory `examples` you will have a non-exhaustive list of code uses:
*By review we mean capital gain + volume exchanged*
 - `last_day_review_for_specific_currency.py`: if you want a review on the last 24h for a specific coin
 - `last_month.py`: do a review of all the coins trading during the last month
 - `pnl_with_fees.py` : provide the Profit & loss for open positions including margin fees (opening + rollover) and fee for closing the position, what Kraken does not include in its PNL



More examples will be added later, in the meantime you can mix the code as you want to match with your use case

## Security advisory
The krakenex use your Kraken key (`kraken.key`: first line the secret, second one the private key). It is sensitive data and it would not be part of a git repo, it why I put it in the .gitignore. However, If you rename it to use the repo please be sure to ignore it before commiting.

As well, I suggest you to use a specific key when you used this repo (w/ the minimum right needed)


## Contribution
This repo is public although at the beginning it was only used for personal purpose. I think it could be useful to share it!

Obviously, like any code/algo, it could have some mistakes within. It is also why I made it public, **don't hesitate to contribute if you want to correct, enrich, enhance the code.**

*PS: the repo use `precommit`*
