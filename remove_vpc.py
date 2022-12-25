#tutorial 22, how to remove aws vpc
import boto3

client=boto3.client("ec2")
responce = client.delete_vpc(
        VpcId = 'vpc-090e8f95cac8bea02',

    )
responce