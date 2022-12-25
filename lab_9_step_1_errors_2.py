import logging
import boto3
from botocore.exceptions import ClientError

try:
    client = boto3.client('translate')
    <snip>
except ClientError as e:
    logging.warning("<your msg> {}".format(e))


# Source: https://catalog.us-east-1.prod.workshops.aws/workshops/3d705026-9edc-40e8-b353-bdabb116c89c/en-US/errors-and-exceptions/lab-9/step-1