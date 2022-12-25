import boto3

ec2_client=boto3.client("ec2")
x=ec2_client.describe_instances()
data=x["Reservations"]
li=[]
for instances in data:
    instance=instances["Instances"]
    for ids in instance:
        instance_id=ids["InstanceId"]
        li.append(instance_id)
        
    
ec2_client.terminate_instances(InstanceIds=li)
#print(x.keys())

#print(len(x["Reservations"]))
# Source: https://youtu.be/DqEK0OpxEas?t=323