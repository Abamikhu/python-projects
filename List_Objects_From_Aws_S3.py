import boto3

s3_resource=boto3.client('s3')
objects=s3_resource.list_objects(Bucket='abamikhuboto3sample') ["Contents"]
length = len(objects)
print(length)

if len(objects) >=0:
    print("object exit")
    
for object in objects:
    print(object["Key"]) # Just the keys/file names.. use print(object) "for everything" 