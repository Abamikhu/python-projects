import boto3

ec2_resource=boto3.resource("ec2")

ec2_resource.create_instances(ImageId='ami-0b5eea76982371e91',  # string = image/AMI ID
    InstanceType='t2.micro',
        MaxCount=1,
        MinCount=1
        )

#source: https://www.youtube.com/watch?v=q_IC90H2Rbc