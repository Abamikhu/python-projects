#! /usr/bin/env python3.7

import random
import re 
#

number_of_names = input("Number of EC2 names? ")
number_of_names = int(number_of_names)
department = input("What is your department? ")
number_of_password = 1

print("Your EC2 random generated names are: ")
while number_of_password <= number_of_names:

    count = 1
    choice = random.randrange(2,6)
    password = []
    while count < 14:
        if (choice %2) == 0:
            letter_for_password = random.randrange(0,10)
            letter_for_password = str(letter_for_password)
            password.append(letter_for_password)
            count += 1
            choice = random.randrange(2,6)
        else:    
            letter_for_password = random.randrange(97,122)  # 97,122
            password.append(chr(letter_for_password))
            count += 1
            choice = random.randrange(2,6)
            
    def convert(password):
        new = ""
        for x in password:
            new += x
        return new
    
    print(department + "_" + convert(password))
    number_of_password +=1
