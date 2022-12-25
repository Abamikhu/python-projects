import boto3

client=boto3.client('ec2')

client.delete_vpc(
    VpcId='vpc-0e73ac6204a47d360', # VPC ID is vpc-0faeac7c1f7d07aed
    )


# source: https://www.youtube.com/watch?v=Nec2Do7_9Vw