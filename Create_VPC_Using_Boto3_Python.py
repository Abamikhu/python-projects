import boto3

#Create the VPC
client=boto3.client('ec2') #this is associated with teh VPC
client.create_vpc(CidrBlock='10.0.0.0/16') 

# Source: https://www.youtube.com/watch?v=sqo9VUHj_uY