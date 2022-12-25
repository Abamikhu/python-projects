'''
Use case: EC2 w/o proper tag. Need to stop EC2 and send reminder email to employee
Source: https://www.youtube.com/watch?v=RL-mQWFWJcM

1) Create IAM Role :
    Lambda > permissions: AmazonEC2FullAccess & 

2) Set up the event:
    A) Cloudwatch:
        a) Create Event: Events > Rules > Create Rules > Service Name: "EC2" & Event Type: "EC2 Instance State-change Notification" > Specific state(s): running
        NOTE: Under Show Sample Event, we see what's pushed to the Lambda.  We copied it.
            SAMPLE CODE #1
            {
              "version": "0",
              "id": "ee376907-2647-4179-9203-343cfb3017a4",
              "detail-type": "EC2 Instance State-change Notification",
              "source": "aws.ec2",
              "account": "123456789012",
              "time": "2015-11-11T21:30:34Z",
              "region": "us-east-1",
              "resources": [
                "arn:aws:ec2:us-east-1:123456789012:instance/i-abcd1111"
              ],
              "detail": {
                "instance-id": "i-abcd1111",
                "state": "running"
              }
            }
    B) Lambda
        a) Create Lambda to attach: Create function > [used defaults] > name: ec2_check_tags > Change default execution role : use existing role : lambda_boto3demo
        b) Coding the Lambda: Have Lambda code ready. 
            I) Get Boto3 function to get the tags for EC2s and paste code in Lambda.  Source: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#client
                SAMPLE CODE #2
                import boto3

                client = boto3.client('ec2')

                # under def lambda_handler(event, context):
                response = client.describe_tags(
                    DryRun=True|False,
                    Filters=[
                        {
                            'Name': 'resource-id',
                            'Values': [
                                'i-082dc24de88d5cb6d', #Cloud9 IDE EC2
                            ]
                        },
                    ],
                )
            II) Create Test event: [used defaults] > Paste contents from SAMPLE CODE #1. NOTE: enter instance ID "instance-id:   > 
            
                printed meta data
                    {'Tags': [{'Key': 'Name', 'ResourceId': 'i-082dc24de88d5cb6d', 'ResourceType': 'instance', 'Value': 'aws-cloud9-test-python-IDE-eed39ae9fc9343d4a6ba651c5608a7b3'}, 
                    {'Key': 'aws:cloud9:environment', 'ResourceId': 'i-082dc24de88d5cb6d', 'ResourceType': 'instance', 'Value': 'eed39ae9fc9343d4a6ba651c5608a7b3'}, 
                    {'Key': 'aws:cloud9:owner', 'ResourceId': 'i-082dc24de88d5cb6d', 'ResourceType': 'instance', 'Value': 'AIDARZAJD52XL466IXXY3'}, 
                    'Key': 'aws:cloudformation:logical-id', 'ResourceId': 'i-082dc24de88d5cb6d', 'ResourceType': 'instance', 'Value': 'Instance'}, 
                    {'Key': 'aws:cloudformation:stack-id', 'ResourceId': 'i-082dc24de88d5cb6d', 'ResourceType': 'instance', 'Value': 'arn:aws:cloudformation:us-east-1:122425700014:stack/aws-cloud9-test-python-IDE-eed39ae9fc9343d4a6ba651c5608a7b3/92da9690-70d4-11ed-8c50-0a730c78e8ff'}, 
                    {'Key': 'aws:cloudformation:stack-name', 'ResourceId': 'i-082dc24de88d5cb6d', 'ResourceType': 'instance', 'Value': 'aws-cloud9-test-python-IDE-eed39ae9fc9343d4a6ba651c5608a7b3'}], 'ResponseMetadata': {'RequestId': '9aa8da0d-1a5a-47f7-9b72-73d6c9157298', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '9aa8da0d-1a5a-47f7-9b72-73d6c9157298', 'cache-control': 'no-cache, no-store', 'strict-transport-security': 'max-age=31536000; includeSubDomains', 'content-type': 'text/xml;charset=UTF-8', 'content-length': '1819', 'date': 'Thu, 22 Dec 2022 01:33:17 GMT', 'server': 'AmazonEC2'}, 'RetryAttempts': 0}}
'''