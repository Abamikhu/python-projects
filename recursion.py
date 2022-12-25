#! /usr/bin/env python3.7

#We can call a function within a function (Recursion)
#NOTE: Don't rely on recurision in Python. Not optimized for that.
#1,1,2,3,5,8,13,

#f(n) = f(n-2) + f(n -1)

#f(5) = f(3) + f(4)
#f(5) = f(1) + 

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    return fib(n - 2) + fib(n-1)
    
item_to_calculate = int(input("What Fibanacii item would like like to calculate?  "))   
print(fib(item_to_calculate))
    
    
    