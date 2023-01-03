import json
from shiptime import Shiptime
class Shipping():

    def run_lambda_action(self, path,
                          method, query_string=None, body=None):
        project_name = None

        if "/rate" == path:
            s = Shiptime()
            rates = s.rate(body=body)
            result = {"rates": rates}
        elif "/list_couriers" == path:
            result = {"state": self.project_state}
        else:
            message = "Invalid path"

        return {
            'statusCode': 200,
            'headers': {"content-type": "application/json"},
            'body': json.dumps(result)
        }