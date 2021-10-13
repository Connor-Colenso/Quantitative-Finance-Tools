from datetime import datetime
import requests

strp = datetime.strptime


def stock_data(ticker, condition):  # Get stock data.

    # Put together the link to the page we will request
    # data from.
    api = "API_KEY"  # Private API key removed from code extract.
    start = "https://www.alphavantage.co/query?"
    mid = "function=TIME_SERIES_DAILY_ADJUSTED&symbol="
    end = "&outputsize=full&apikey="

    link = (start + mid + ticker + end + api)

    # Make the API request and turn it into a dict object.
    response = requests.get(link)

    reply = response.json()["Time Series (Daily)"]

    # More easily maps the condition to valid terms.
    condition_dict = {"open": "1. open",
                      "high": "2. high",
                      "low": "3. low",
                      "close": "4. close",
                      "adj close": "5. adjusted close",
                      "volume": "6. volume",
                      "dividend amount": "7. dividend amount",
                      "split coeff": "8. split coefficient"}

    condition = condition_dict[condition.lower()]

    date_lst = list(reply.keys())
    prices = [float(i[condition]) for i in list(reply.values())]

    # Reverse order of lists then return them.
    return date_lst[::-1], prices[::-1]


def nearest_date(date_lst, date):
    """
    :param date_lst: List of dates to choose from.
    :param date: Date to find nearest to.
    :return: The nearest date to date inside date_lst.

    This function will find the closest date to the one stored
    in the variable date within the date_lst. Because markets
    are not open everyday we must often approximate to the
    closest date available within the data set.
    """

    # Convert date string to datetime object.
    date = strp(date, "%Y-%m-%d")

    # Convert entire date_lst to datetime objects.
    date_lst = [strp(i, "%Y-%m-%d") for i in date_lst]

    # Calculate the smallest distance from the date using
    # the dates provided in date_lst.
    date = min(date_lst, key=lambda i: abs(i - date))

    # Return only the first 10 characters of the datetime
    return str(date)[:10]


def date_extractor(date_lst, prices, start_date, end_date):
    """
    :param date_lst: List of dates.
    :param prices: List of prices.
    :param start_date: Attempted s
    :param end_date:
    :return:

    This function takes the date_lst and price data
    then returns the valid data between the two
    specified dates. Note that if the date is not
    directly in the list it will find the closest
    alternative that is.
    """

    # Use the nearest_date function to find valid
    # dates which are closest to those selected.
    start_date = nearest_date(date_lst, start_date)
    end_date = nearest_date(date_lst, end_date)

    # Find the position in the list of the specified
    # dates.
    start = date_lst.index(start_date)
    end = date_lst.index(end_date) + 1

    # Extract the actual information.
    date_lst = date_lst[start:end]
    prices = prices[start:end]
    # Return out of function.
    return date_lst, prices
