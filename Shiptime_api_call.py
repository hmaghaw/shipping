import requests
from requests.auth import HTTPBasicAuth
import json
def shiptime_rate(body):
    response = requests.post('https://restapi.shiptime.com/rest/rates/',
            auth = HTTPBasicAuth('hanyelgaml@ideationmax.com', 'Canada2012'), data=body)

    x = response.json()

    return x

def filter_shiptime_json(y):
    result = []
    for i in range (len(y['availableRates'])):
        obj = {}
        obj['carrierId'] = y['availableRates'][i]['carrierId']
        obj['carrierName'] = y['availableRates'][i]['carrierName']
        obj['serviceName'] = y['availableRates'][i]['serviceName']
        obj['totalCharge'] = y['availableRates'][i]['totalCharge']['amount']
        result.append(obj)
    return result


f = open('input.json')

# returns JSON object as
# a dictionary
json_body = json.load(f)
body = json.dumps(json_body)

response = shiptime_rate(body=body)
filterd_response = filter_shiptime_json(response)

pass
