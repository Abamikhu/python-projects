import boto3
import os
import glob

# Upload file
#s3_resource=boto3.client('s3')
#s3_resource.upload_file(
#    Filename ='upload.png',  # name of file on system/Linux
#    Bucket ='abamikhuboto3sample', # name of bucket
#    Key ="upload.png"  # Name of file in s3
#    )

cwd=os.getcwd()
cwd=cwd+"/Test/"

files=glob.glob(cwd+"*.png")

for file in files:
    s3_resource=boto3.client('s3')
    s3_resource.upload_file(
    Filename =file,  # name of file on system/Linux
    Bucket ='abamikhuboto3sample', # name of bucket
    Key =file.split("/")) #prints whole list
    #Key =file.split("/")[-1]) #Print last one
    
    #Source: https://www.youtube.com/watch?v=dUm9h3hwXBk