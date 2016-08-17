import pandas
from pandas.io.json import json_normalize
import requests
#from termcolor import colored, cprint
pair = 'btc-strat'
ticker = requests.get("https://bittrex.com/api/v1.1/public/getticker?market="+pair)
orderbook = requests.get("https://bittrex.com/api/v1.1/public/getorderbook?market=btc-strat&type=both&depth=50")
result = json_normalize(ticker.json(),'result')
buy = json_normalize(orderbook.json()['result']['buy']) #=dataframe format
sell = json_normalize(orderbook.json()['result']['sell'])
 f = format(sell['Rate'][0],'0.8f')
 sell.info()
sell['Rate']*sell['Quantity'].sum()
value=[]
value=sell['Rate']*sell['Quantity']
# add element to DataFrame
sell['value']=sell['Rate']*sell['Quantity']
group=sell.groupby('Rate')['value'].sum()
#good
grouped=buy.groupby('Rate').sum()
grouped

"""
http://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/
http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.groupby.html
>>> data = [{'state': 'Florida',
...          'shortname': 'FL',
...          'info': {
...               'governor': 'Rick Scott'
...          },
...          'counties': [{'name': 'Dade', 'population': 12345},
...                      {'name': 'Broward', 'population': 40000},
...                      {'name': 'Palm Beach', 'population': 60000}]},
...         {'state': 'Ohio',
...          'shortname': 'OH',
...          'info': {
...               'governor': 'John Kasich'
...          },
...          'counties': [{'name': 'Summit', 'population': 1234},
...                       {'name': 'Cuyahoga', 'population': 1337}]}]
>>> from pandas.io.json import json_normalize
>>> result = json_normalize(data, 'counties', ['state', 'shortname',
...                                           ['info', 'governor']])
>>> result
         name  population info.governor    state shortname
0        Dade       12345    Rick Scott  Florida        FL
1     Broward       40000    Rick Scott  Florida        FL
2  Palm Beach       60000    Rick Scott  Florida        FL
3      Summit        1234   John Kasich     Ohio        OH
4    Cuyahoga        1337   John Kasich     Ohio        OH
"""
