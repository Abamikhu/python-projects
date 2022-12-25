import boto3
s3_resource=boto3.client('s3')
bucketlist = s3_resource.list_buckets() 
print(bucketlist)
bucketlist1 = s3_resource.list_buckets() ["Buckets"]

print("-----------------------------------------")
print(bucketlist1)

print("-----------------------------------------")
bucketlist2 = s3_resource.list_buckets() ["Buckets"] [0]["Name"]
print(bucketlist2)

print("-----------------------------------------")
bucketlist3 = s3_resource.list_buckets() ["Buckets"] [0]["CreationDate"]
print(bucketlist3)

print("-----------------------------------------")
creation_date = s3_resource.list_buckets() ["Buckets"] [0]["CreationDate"]
print('This was created on', bucketlist3)

print("-----------------------------------------")
creation_date2 = creation_date.strftime("%d%m%y_%H:%M:%s")
print("The creation date it", creation_date2)

print("-----------------------------------------")
for bucket in s3_resource.list_buckets() ["Buckets"]:
    print(bucket)

print("-----------------------------------------")
print("Here is the list: ")
for bucket in s3_resource.list_buckets() ["Buckets"]:
    print(bucket["Name"])
    print(bucket["CreationDate"])