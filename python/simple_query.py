from historical_data_api import get_poolpairs, get_price

rapid_api_key = "<Place your API key here>"

if __name__ == "__main__":

    # First get all available poolpairs
    available_poolpairs = get_poolpairs(rapid_api_key)
    print(available_poolpairs)

    # Query the price for the first poolpair
    query_date = "2022-05-01"
    poolpair = available_poolpairs[0]

    price_high_low = get_price(poolpair, query_date, rapid_api_key)

    # Average between high and low
    price = (price_high_low["high"] +  price_high_low["low"]) / 2.0

    print(f"Price of {poolpair} on {query_date}: {price}")
