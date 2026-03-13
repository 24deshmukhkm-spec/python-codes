# Task
# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird
# Input Format

# A single line containing a positive integer, .

# Constraints

# Output Format

# Print Weird if the number is weird. Otherwise, print Not Weird.

# Sample Input 0

# 3
# Sample Output 0

# Weird
# Explanation 0


#  is odd and odd numbers are weird, so print Weird.

# Sample Input 1

# 24
# Sample Output 1

# Not Weird
# Explanation 1


#  and  is even, so it is not weird.

# !/bin/python3

# import math
# import os
# import random
# import re
# import sys



# if __name__ == '__main__':
#     n = int(input().strip())
#     if n%2== 0:
#         if 2<n<5:
#             print("Not Weird")
#         elif 6<n<20:
#             print(" weird")
#         else:
#             print("Not Weird")
        
#     else: 
#         print("Weird")


# ---------------------------------------------------------------------------
# Task
# The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.
# Example


# Print the following:

# 8
# -2
# 15
# Input Format

# The first line contains the first integer, .
# The second line contains the second integer, .

# Constraints



# Output Format

# Print the three lines as explained above.

# Sample Input 0

# 3
# 2
# Sample Output 0

# 5
# 1
# 6
# Explanation 0

# ----------------------------------------------------------------------------------
# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())
#     res=a+b
#     sub=a-b
#     mul=a*b
#     print(res)
#     print(sub)
#     print(mul)
# ------------------------------------------------------------------------------------

# *************DATA STRUCTURES & ALGORITHMS*******************************************

# what is data structure? 

# data structure are different ways of organizing data that can be 



#function
# def add():
#     a=int(input('enter the num'))
#     b=int(input('enter the num'))
#     res=a+b
#     print(res)
# if __name__ == '__main__':
#     add()


#function with paramter no return value
# def add(x,y):
#     res=x+y
#     print(res)
# if __name__ == '__main__':
#         a=int(input('enter the num'))
#         b=int(input('enter the num'))
#         add(a,b)

#function with parameter return value
# def add(x,y):
#     res=x+y
#     return res
# if __name__ == '__main__':
#         a=int(input('enter the num'))
#         b=int(input('enter the num'))
#         r=add(a,b)
#         print(r)

#mulitple function value

def add(x,y):
    res1=x+y
    res2=x-y
    res3=x*y
    
    return res1,res2,res3
if __name__ == '__main__':
        a=int(input('enter the num'))
        b=int(input('enter the num'))
        r1,r2,r3=add(a,b)
        print(r1,r2,r3)