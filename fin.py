import csv
import tqdm
import datetime
import pandas
import numpy
import math

def load_yahoo_csv(file_name):
    rows = []
    with open(file_name, 'r') as f:
        with tqdm.tqdm(unit='row', desc='Read prices') as pbar:
            for row in csv.DictReader(f,
                                      delimiter=',',
                                      quotechar='"',
                                      quoting=csv.QUOTE_MINIMAL):
                rows.append((
                    datetime.datetime.strptime(row['Date'], '%Y-%m-%d'),
                    float(row['Open']),
                    float(row['Close']),
                    float(row['High']),
                    float(row['Low']),
                    float(row['Adj Close']),
                    float(row['Volume'])))
                pbar.update(1)
    df = pandas.DataFrame(data=rows, columns=['date', 'open', 'close', 'high', 'low', 'adjusted_close', 'volume'])
    return df.set_index('date')


def percentage_change(prices):
    """Percentage change between subsequent prices."""
    return prices.pct_change()


def annualized_volatility(deltas):
    """
    Calculate annualized volatility.

    Assume 252 trading days in a year.
    """
    return numpy.std(deltas) * math.sqrt(252) 
