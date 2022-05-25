import datetime
from typing import Generator
from historical_data_api import get_poolpairs, get_price

rapid_api_key = "<Place your API key here>"


def date_to_year_month_day(date: datetime.date) -> str:
    """Convert a date object to a string of format YYYY-MM-DD"""

    return f"{date.year}-{str(date.month).zfill(2)}-{str(date.day).zfill(2)}"


def daterange(
    start_date: datetime.date, end_date: datetime.date
) -> Generator[datetime.date, None, None]:
    """A generator a series of days. From start to end date. The end date is included."""

    for n in range(int((end_date - start_date).days) + 1):
        yield start_date + datetime.timedelta(n)


if __name__ == "__main__":

    # Define start and end date objects
    start_date = datetime.datetime.strptime("2021-12-01", "%Y-%m-%d")
    end_date = datetime.datetime.strptime("2022-05-01", "%Y-%m-%d")

    # First get all available poolpairs
    available_poolpairs = get_poolpairs(rapid_api_key)
    print("Available poolpairs:")
    print(available_poolpairs)

    poolpair = "GOOGL-DUSD"
    if not poolpair in available_poolpairs:
        print(f"Poolpair {poolpair} is not available!")
        exit(0)

    for d in daterange(start_date, end_date):
        # Query the price of the poolpair
        query_date = date_to_year_month_day(d)
        price_high_low = get_price(poolpair, query_date, rapid_api_key)

        # Average between high and low
        price = (price_high_low["high"] +  price_high_low["low"]) / 2.0
        print(f"Price of {poolpair} on {query_date}: {price}")
