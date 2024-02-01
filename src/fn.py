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
    if event.get("status") is not None:
        raise ExampleException(event["status"])
    return event
