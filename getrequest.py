import requests
from termcolor import colored, cprint

def ordbook(threshold,length):
    v_length=length
    BTCthreshold=threshold
    f_tick = ''
    v_buytot = 0
    v_selltot = 0
    n=0
    j=0
    input_coin= input("Input Coin:")

    #if not input_coin:
    pair = 'btc-strat'
    #else:
    #    pair = "btc-"+input_coin

    cprint(pair.upper(),"green", 'on_white')

    ticker = requests.get("https://bittrex.com/api/v1.1/public/getticker?market="+pair)
    orderbook = requests.get("https://bittrex.com/api/v1.1/public/getorderbook?market=BTC-strat&type=both&depth=50")
    #print (orderbook.json())
    for tick_res in ticker.json()["result"]:
        v_tikval = format(ticker.json()["result"][tick_res], '0.8f')
        f_tick = f_tick + tick_res + " : "+ colored(v_tikval,"red") + " "
    print (f_tick)

    cprint("BUY","white", "on_blue")
    for i in orderbook.json()["result"]["buy"]:
        v_buyqty = i["Quantity"]
        v_buyrate = i["Rate"]
        v_buybtc = v_buyrate * v_buyqty
        v_buytot = v_buytot + v_buybtc
        if (v_buybtc>BTCthreshold):
            if(n<v_length):
                print (colored(format(v_buybtc,'0.8f'),"blue") + "@" + colored(format(v_buyrate,'0.8f'),"red") + "-TOT-" + format(v_buytot,'0.3f'))
                n +=1
    cprint(("Total Buy: " + format(v_buytot,'0.3f') + "BTC"),'white', 'on_blue')

    cprint("SELL","white", "on_green")
    for h in orderbook.json()["result"]["sell"]:
        v_sellqty = h["Quantity"]
        v_sellrate = h["Rate"]
        v_sellbtc = v_sellrate * v_sellqty
        v_selltot = v_selltot + v_sellbtc
        if (v_sellbtc>BTCthreshold):
            if(j<v_length):
                print (colored(format(v_sellbtc,'0.8f'),"green") + "@" + colored(format(v_sellrate,'0.8f'),"red") + "-TOT-" + format(v_selltot,'0.3f'))
                j +=1
    cprint(("Total Sell: " + format(v_selltot,'0.3f') + "BTC"),'white', 'on_green')



"""#print (ticker.json())
#print (ticker.json()["result"]["Last"])
#v_last = format(ticker.json()["result"]["Last"], '0.8f')
#print (ticker.json()["result"])
#print ("Last: " +v_last)
"""

"""
 # example of json data object group with two values of key id
jsonstufftest = '{'group':{'id':'2','id':'3'}}
 # always set your headers
headers = {'User-Agent': 'Moz & Woz'}
 # the url you are trying to load and get json from
url = 'http://www.cooljson.com/cooljson.json'
 # in python 3 you can build the request using request.Request
req = urllib.request.Request(url,None,headers)
 # try to connect or fail gracefully
try:
    response = urllib.request.urlopen(req) # new python 3 code -jc
except:
    exit('could not load page, check connection')
 # read the response and DECODE
html=response.read().decode('utf8') # new python3 code
 # now convert the decoded string into real JSON
loadedjson = json.loads(html)
 # print to make sure it worked
print (loadedjson) # works like a charm
 # iterate through each key value
for testdata in loadedjson["group"]:
    print (accesscount["id"]) # should print 2 then 3 if using test json
"""
"""
 # example of json data object group with two values of key id
jsonstufftest = '{'group':{'id':'2','id':'3'}}
 # always set your headers
headers = {'User-Agent': 'Moz & Woz'}
 # the url you are trying to load and get json from
url = 'http://www.cooljson.com/cooljson.json'
 # in python 3 you can build the request using request.Request
req = urllib.request.Request(url,None,headers)
 # try to connect or fail gracefully
try:
    response = urllib.request.urlopen(req) # new python 3 code -jc
except:
    exit('could not load page, check connection')
 # read the response and DECODE
html=response.read().decode('utf8') # new python3 code
 # now convert the decoded string into real JSON
loadedjson = json.loads(html)
 # print to make sure it worked
print (loadedjson) # works like a charm
 # iterate through each key value
for testdata in loadedjson["group"]:
    print (accesscount["id"]) # should print 2 then 3 if using test json
"""
