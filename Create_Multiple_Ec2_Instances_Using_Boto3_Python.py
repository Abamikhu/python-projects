import boto3
ec2_resource=boto3.resource('ec2')
ec2_resource.create_instances(ImageId='ami-0b5eea76982371e91',
    InstanceType='t2.micro',
    MaxCount=2,
    MinCount=2
    )



# Source: https://www.youtube.com/watch?v=nlHk3mFSlAY