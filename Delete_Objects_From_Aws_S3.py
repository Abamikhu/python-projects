import boto3
import os
import glob

s3_resource=boto3.client('s3')

# Deletes one file
#s3_resource.delete_object(Bucket="abamikhuboto3sample",
#    Key="Capture.PNG") #
    
# Find all the object from the bucket
objects = s3_resource.list_objects(Bucket="abamikhuboto3sample")["Contents"]
length = len(objects)

#Interation
for object in objects: 
    response=s3_resource.delete_object(Bucket="abamikhuboto3sample",
        Key=object ["Key"]) 
    print(response)
    

    
# Source: https://www.youtube.com/watch?v=ggfvnu4LgCc