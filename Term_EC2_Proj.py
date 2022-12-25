#!/bin/python3
import boto3

ec2_client=boto3.client("ec2")
x=ec2_client.describe_instances()
data=x["Reservations"][0]
data_instance=data["Instances"]
for i in range (len(data_instance)):
    print(f"Number of open EC2 instance(s): {(len(data_instance))} ")
    

response = input('Do you want to terminate all EC2s running? Please enter "Yes" or "No": ')
if response == "Yes":
    ec2_client=boto3.client("ec2")
    x=ec2_client.describe_instances()
    data=x["Reservations"]
    li=[]
    for instances in data:
        instance=instances["Instances"]
        for ids in instance:
            instance_id=ids["InstanceId"]
            li.append(instance_id)
    ec2_client.stop_instances(InstanceIds=li)
    print("This")
else:
    print("No EC2s terminated")