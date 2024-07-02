#birdeye

'''
STRATEGY

1.Pull all data from birdeye and get volume, tvl, 24h trade, 24h volume, marketcap (500k)
2. analyze that data to decide which is best to buy
    --use llms
    --use gpt vision
3. buy 5 top memes
'''

import requests
import dontshare as d
import json

HEADERS = {"X-API-KEY": d.api}

def get_solana_24H():
    url = "https://public-api.birdeye.so/defi/tokenlist?sort_by=v24hUSD&sort_type=desc"
    response = requests.get(url, headers=HEADERS)
    return response.text

response = json.loads(get_solana_24H())
json_formatted_str = json.dumps(response, indent=2)
print(json_formatted_str)




