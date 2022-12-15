import boto3

resource=boto3.resource(s3)
list(resource.bucket.all())