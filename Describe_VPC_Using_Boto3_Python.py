import boto3

client=boto3.client('ec2')

# how to describe all VPS in  your account  
# client.describe_vpcs()
# x=client.describe_vpcs()
# prints the list
#print(x)

# prints just VPC data

#print(x["Vpcs"])

#number of VPCs
num_of_vpcs=x["Vpcs"]
length = len(num_of_vpcs)
#print(length)

# Give VPCs names
for vpc in num_of_vpcs:
    print(vpc["VpcId"])
    
# how to view based on vpc id
x=client.describe_vpcs(VpcIds=["vpc-0d4e5b339aca0cadb"])

# Source: https://www.youtube.com/watch?v=IbJFrrk8XAM