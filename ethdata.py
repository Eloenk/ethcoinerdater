

import requests

def coiner(coin,curr):
    url = "https://api.coingecko.com/api/v3/simple/price"

    params = {  
         'ids': coin,
         'vs_currencies': curr
    }

    return requests.get(url, params = params)

def resnises(r,c,d):
    if r.status_code == 200:
         data = r.json()
         Ethereum_price = data[c][d]
         return f"The price of Ethereum in USD is ${Ethereum_price}"
    else:
         return "Failed to retrieve data from the API"

def main():
    r = coiner('ethereum','usd')
    price = resnises(r,'ethereum','usd')
    print(price)

main()
