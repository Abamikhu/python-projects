#! /usr/bin/env python3.7

# Initial text
print("This is a blank list")
aws_list = "Such emptiness!"
print("List contains the string -", aws_list)
print("Now I'm going to print a list of AWS services that use Lambda")
aws_list = ['EC2','S3', 'Lambda'] 
print(aws_list)

# append list to blank list
aws_list.append('Cloud9')
# aws_list = aws_list.append('Cloud9')
print(aws_list)

# Remove two specific services from the list by name or by index.
# pop() method
t = input("Enter the number of the item you want to remove. ")
t = int(t)
# print(type(t))
aws_list.pop(t - 1)
print (aws_list)

# source
# - https://www.w3schools.com/python/ref_list_append.asp
# - 