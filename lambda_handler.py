import json
from shipping import Shipping

def lambda_handler(event, context):
    print(event)
    method = event['requestContext']['http']['method']
    path = event['requestContext']['http']['path']
    if 'queryStringParameters' in event:
        query_string = event['queryStringParameters']
    else:
        query_string = None
    if 'body' in event:
        body = json.loads(event['body'])
    else:
        body = None

    run = Shipping(None)
    return run.run_lambda_action(path, method, query_string, body)