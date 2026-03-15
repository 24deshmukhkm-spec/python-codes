# compare 3 nmuber given by user
n1=int(input("enter the nmuber"))
n2=int(input("enter the nmuber"))
n3=int(input("enter the nmuber"))
n4=int(input("enter the nmuber"))
max=n1

if max<n2:
    max=n2
if max<n3:
    max=n3
if max<n4:
    max=n4
print(max)

a= [5,7,87,55,23]
max=a[0]
min=a[0]
for i in range (len(a)):
    if max< a[i]:
        max=a[i]
    if max> a[i]:
        max=a[i]
print(max)
print(min)


# To find year is leep year or not
year=int(input('enter the year'))
if year%100==0:
    if year%4==0:
        print(year,' is leep year')
    else:
        print(year,' is not leep year')
else:
    if year%4==0:
        print(year,' is century leep year')
    else:print(year," is not leep year")

# tech number
no=int(input('enter four digit number'))
n1=no%100
n2=no//100
s=n1+n2
out=s*s
if no==out:
    print(out,'is tech nmuber')
else: print(out,'is not tech number')

# tech number for any nunber
no = int(input("Enter number: "))
temp = no
count = 0
while temp > 0:
    temp = temp // 10
    count += 1

if count % 2 == 0:   
    half = 10 ** (count // 2)
    n1 = no // half
    n2 = no % half
    s = n1 + n2
    out = s * s
    if out == no:
        print(no, "is Tech Number")
    else:
        print(no, "is not Tech Number")

else:
    print("Digits must be even to be a Tech Number")

# rearrange postive -ve nmuber in pattern +-+-+-+-+-+-
arr = [1, -2, -3, -4, 5, 6]

pos = []
neg = []

for i in arr:
    if i >= 0:
        pos.append(i)
    else:
        neg.append(i)

result = []
for i in range(min(len(pos), len(neg))):
    result.append(pos[i])
    result.append(neg[i])

print(result)
#sum of array


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
    # Write your code here
    sum=0
    for i in range (len(ar)):
        sum=sum+ar[i]
    return(sum)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()


#compare 4 number using if else

n1=int(input("enter the nmuber"))
n2=int(input("enter the nmuber"))
n3=int(input("enter the nmuber"))
n4=int(input("enter the nmuber"))
max=n1

if max<n2:
    max=n2
if max<n3:
    max=n3
if max<n4:
    max=n4
print(max)
