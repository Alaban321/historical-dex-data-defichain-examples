from historical_data_api import get_poolpairs, get_price

rapid_api_key = "<Place your RapidAPI key here>"

if __name__ == "__main__":

    # First get all available poolpairs
    available_poolpairs = get_poolpairs(rapid_api_key)
    print(available_poolpairs)

    query_date = "2022-06-19"

    for pair in available_poolpairs:
      price_high_low = get_price(pair, query_date, rapid_api_key)

      # Average between high and low
      price = (price_high_low["high"] +  price_high_low["low"]) / 2.0

      print(f"Price of {pair} on {query_date}: {price} {price_high_low['unit']}")
