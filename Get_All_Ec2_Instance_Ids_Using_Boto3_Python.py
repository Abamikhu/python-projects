import boto3
ec2_client=boto3.client("ec2")
x=ec2_client.describe_instances()
data=x["Reservations"][0]
data_instance=data["Instances"]
for i in range (len(data_instance)):
    print(f"instance id is {data_instance[i]['InstanceId']}")
    
#print(x.keys())

#print("-----------------------------------")


#print(x['Reservations'])
#print("-----------------------------------")

# print dictionary keys  ------------> print(x.keys())

#Get length of list
#print(len(x['Reservations']))
#print("-----------------------------------")


# data=x['Reservations'][0]
#print(data)

#print("-----------------------------------")

#data_instance=data["Instances"]
#print(data_instance)

#print("-----------------------------------")
#print(len(data_instance))

#print("-----------------------------------")

#for i in range (len(data_instance)):
#    print(f"instance id is {data_instance[i]['InstanceId']}")

# Source - https://youtu.be/gyiGVOkfbuk?t=847