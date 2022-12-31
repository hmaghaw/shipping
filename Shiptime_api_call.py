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

# body = """ {
#   "from": {
#     "companyName": "Ideationmax",
#     "streetAddress": "2942 Garnethill way",
#     "streetAddress2": "",
#     "city": "Oakville",
#     "countryCode": "CA",
#     "state": "ON",
#     "postalCode": "L6M5E9",
#     "attention": "Hany Elgaml",
#     "email": "hanyelgaml@ideationmax.com",
#     "phone": "6476248506",
#     "instructions": "Front door on the street",
#     "residential": true,
#     "notify": true
#   },
#   "to": {
#     "companyName": "Dar",
#     "streetAddress": "485 Morden Rd",
#     "streetAddress2": "",
#     "city": "Oakville",
#     "countryCode": "CA",
#     "state": "ON",
#     "postalCode": "L6K3W6",
#     "attention": "Mohamed Osam",
#     "email": "hanyelgaml@ideationmax.com",
#     "phone": "str6476248506ing",
#     "instructions": "Back door",
#     "residential": true,
#     "notify": true
#   },
#   "packageType": "PACKAGE",
#   "lineItems": [
#     {
#       "length": 21,
#       "width": 10,
#       "height": 7,
#       "weight": 8,
#       "declaredValue": {
#         "currency": "CAD",
#         "amount": 0
#       },
#       "description": "Personal Stuff"
#     }
#   ],
#   "unitOfMeasurement": "IMPERIAL",
#   "serviceOptions": [
#     "APPOINTMENT"
#   ],
#   "shipDate": "2022-12-30T01:15:33.039Z",
#   "insuranceType": "SHIPTIME"
# }"""

response = shiptime_rate(body=body)
filterd_response = filter_shiptime_json(response)

pass
