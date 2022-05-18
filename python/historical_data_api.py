"""Functions for using the API for historical DEX prices for DeFiChain

API available at:
https://rapidapi.com/chrizogAPI/api/historical-dex-data-for-defichain/
"""

from typing import List
import requests


def get_poolpairs(rapid_api_key: str) -> List:
    """Retrieve the list of available poolpair symbols from the API.

    Returns a list of strings like ["BTC-DFI", "GOOGL-DUSD", ..]
    """

    headers = {
        "X-RapidAPI-Host": "historical-dex-data-for-defichain.p.rapidapi.com",
        "X-RapidAPI-Key": rapid_api_key,
    }

    url = "https://historical-dex-data-for-defichain.p.rapidapi.com/v1/dexprices/pools"
    try:
        resp = requests.get(url=url, headers=headers)
        if resp.status_code == 200:
            return resp.json()
        else:
            print(resp.json())
            return []
    except requests.exceptions.HTTPError as err:
        print(err)
        return []


def get_price(poolpair: str, date_str: str, rapid_api_key: str) -> float:
    """Query the price (i.e. the pool ratio) of a poolpair of a given date.

    Parameters:
      - poolpair symbol, e.g. "BTC-DFI"
      - date in format YYYY-MM-DD, e.g. "2022-05-01"
      - RapidAPI key

    Returns a float. If the poolpair or date is not found the error is logged and 0.0 is returned
    """

    headers = {
        "X-RapidAPI-Host": "historical-dex-data-for-defichain.p.rapidapi.com",
        "X-RapidAPI-Key": rapid_api_key,
    }

    url = f"https://historical-dex-data-for-defichain.p.rapidapi.com/v1/dexprices/price/{poolpair}/{date_str}"
    try:
        resp = requests.get(url=url, headers=headers)
        if resp.status_code == 200:
            return float(resp.json()["price"])
        else:
            print(resp.json())
            return 0.0
    except requests.exceptions.HTTPError as err:
        print(err)
        return 0.0
