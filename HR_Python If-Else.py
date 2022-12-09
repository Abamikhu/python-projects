#!/bin/python3

import math
import os
import random
import re
import sys
#<<<<<<< ajones-list-proj-final
# Enter
#=======

#>>>>>>> main
if __name__ == '__main__':
    n = int(input().strip())


# if n is even and between 2 - 5, print Not Weird
if (n % 2) == 0 and (n>= 2) and (n<= 5):
    print("Not Weird")
# if n is even and between 6 - 20, print Weird    
else:   # (odd and (2-5 or <20 | 
    if (n % 2) == 0 and (n>= 6) and (n<= 20):
            print("Weird")
    else:  # grade must be C, D or F
        if (n % 2) == 0 and (n>= 20):
            print("Not Weird")
        else: print("Weird")
