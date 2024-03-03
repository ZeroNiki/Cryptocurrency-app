import json
import requests
from config import ALL_DATA_LINK, SPECIFIC_DATA_LINK, API_TOKEN

HEADERS = {
    'Authorization': f'{API_TOKEN}'
}
#
# url = f'{ALL_DATA_LINK}'
#
# r = requests.get(url, headers=HEADERS)
#
# data = r.json()
#
# symbols = [item['symbol'] for item in data['data']]


symbol = 'LINK'

clear = {}
link = f'{SPECIFIC_DATA_LINK}{symbol}'

req = requests.get(link, headers=HEADERS)

data_req = req.json()

price = data_req['data']['price']
name = data_req['data']['name']
logo = data_req['data']['logo']

clear['price'] = price
clear['name'] = name
clear['logo'] = logo


print(clear)
