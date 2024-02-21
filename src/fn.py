import boto3
import json
from aws_xray_sdk.core import patch_all

# initialization
session = boto3.session.Session()
patch_all()

class ExampleException(Exception):
    pass

def handler(event, context):
    print(json.dumps(event))
    source = event.get("source")
    status = event.get("status")
    if source is not None and status is not None:
        data = json.loads(status)
        result = data[source]["state"]
        if result == "FAILED":
            raise ExampleException(event["status"])
    return json.dumps(event["status"])
