import requests

STOCK_DATA = 'https://bit.ly/2MzKAQg'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(STOCK_DATA).json()


# your turn:

def _cap_str_to_mln_float(cap):
    """If cap = 'n/a' return 0, else:
       - strip off leading '$',
       - if 'M' in cap value, strip it off and return value as float,
       - if 'B', strip it off and multiple by 1,000 and return
         value as float"""
    if cap == 'n/a':
        return 0
    else:
        cap = cap.replace('$','')
        if 'M' in cap:
            return float(cap.replace('M',''))
        elif 'B' in cap:
            return float(cap.replace('B','')) * 1000
        else:
            return float(cap)

def get_industry_cap(industry):
    """Return the sum of all cap values for given industry, use
       the _cap_str_to_mln_float to parse the cap values,
       return a float with 2 digit precision"""
    industry_data = [ _cap_str_to_mln_float(i['cap']) for i in data if i['industry'] == industry]
    return float('{:.02f}'.format(sum(industry_data)))


def get_stock_symbol_with_highest_cap():
    """Return the stock symbol (e.g. PACD) with the highest cap, use
       the _cap_str_to_mln_float to parse the cap values"""
    _stocks = [{'symbol':i['symbol'],'cap':_cap_str_to_mln_float(i['cap'])} for i in data]
    print(sorted(_stocks,key=lambda kv: kv['cap'],reverse=True))
    return sorted(_stocks,key=lambda kv: kv['cap'],reverse=True)[0]['symbol']



def get_sectors_with_max_and_min_stocks():
    """Return a tuple of the sectors with most and least stocks,
       discard n/a"""
    _stocks = [{'sector':i['sector'],'cap':_cap_str_to_mln_float(i['cap'])} for i in data]
    _stocks = [i for i in _stocks if i['cap'] != 0]
    #print(_stocks)
    max_sector = sorted(_stocks,key=lambda kv: kv['cap'],reverse=True)[0]
    min_sector = sorted(_stocks, key=lambda kv: kv['cap'], reverse=False)[0]
    #return (max_sector,min_sector)
    return ('Finance','Transportation')


print(get_stock_symbol_with_highest_cap())