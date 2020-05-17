# Kraken Capital Gain
## Description
This repo is used to know ***your capital gain using Kraken***. You can play with different parameters, e.g you can have an overview of your capital gain for a specific currency or for a specific timeframe

## Requirement

 - Python 3
 - [krakenex](https://github.com/veox/python3-krakenex) (`pip install krakenex`)

## Usage

 - `kraken_handler.py`
The class used for all interactions with the [KrakenAPI](https://www.kraken.com/fr-fr/features/api)
 - `trades_handler.py`
The class used for all the treatments of the trades recolted with the KrakenAPI

In the directory `examples` you will have a non-exhaustive list of code uses:
For example if you want the review of your trades for the last 24hours call u `last_day_review_for_specific_currency.py`

More examples will be added later, in the meantime you can mix the code as you want to match with your use case

## Security advisory
The krakenex use your Kraken key (`kraken.key`: first line the secret, second one the private key). It is sensitive data and it would not be part of a git repo, it why I put it in the .gitignore. However, If you rename it to use the repo please be sure to ignore it before commiting.

As well, I suggest you to use a specific key when you used this repo (w/ the minimum right needed)


## Contribution
This repo is public although at the beginning it was only used for personal purpose. I think it could be useful to share it!

Obviously, like any code/algo, it could have some mistakes within. It is also why I made it public, **don't hesitate to contribute if you want to correct, enrich, enhance the code.**

*PS: the repo use `precommit`*
