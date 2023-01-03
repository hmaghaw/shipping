import requests
from requests.auth import HTTPBasicAuth
import json
class Shiptime():
    def rate(self, body):
        response = requests.post('https://restapi.shiptime.com/rest/rates/',
                                 auth=HTTPBasicAuth('hanyelgaml@ideationmax.com', 'Canada2012'), data=body)

        x = response.json()

        z = self.result(x)
        return z
    def result(self, y):
        result = []
        for i in range(len(y['availableRates'])):
            obj = {}
            obj['carrierId'] = y['availableRates'][i]['carrierId']
            obj['carrierName'] = y['availableRates'][i]['carrierName']
            obj['serviceName'] = y['availableRates'][i]['serviceName']
            obj['totalCharge'] = y['availableRates'][i]['totalCharge']['amount']
            result.append(obj)
        return result

