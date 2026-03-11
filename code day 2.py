
# reverse number using while loop :

n0=int(input("enter the number"))
rev=0
while n0>0:
    rem=n0%10
    rev=rev*10+rem
    n0=n0//10
print(rev)
    
# case study...................................

# pass1 no=34869 rev=0 rem
# pass2 no=3486 rev=9 rem=9
# pass3 no=348 rev=96 rem=6
# pass4 no=34 rev=968 rem=8
# pass5 no=3 rev=9684 rem=4
# pass6 no=0 rev=96843 rem=3
 


#  )34869(3486 //
#   34860
# ----------
#       9%  
 
#  )3486(348 //
#   3480
# ----------
#       6%

#  )348(34 //
#   340
# ----------
#     8%


#  )34(3 //
#   30
# ----------
#    4%

#   )3(0 //
#    0
# ----------
#    3%


x=int(input('enter the number'))
rev=0
while x>0:
    rem=x%10
    rev=rev*10+rem
    x=x//10
print(rev)
# ____________________________________________
# count number of digit
# ____________________________________________

x=int("input(enter the number")
count=0
while x>0:
	
	x=x//10
	count=count+1
print(count)
# ___________________________________________
# sum of digit
# ____________________________________________
x=int(input("enter the number"))
sum=0
while x>0:
	rem=x%10
	sum=sum+rem
	x=x//10
print(sum)
# ____________________________________________
# check the number is palindrome
# ____________________________________________

x=int(input("enter the number"))
rev=0
temp=x
while x>0:
	rem=x%10
	rev=rev*10+rem
	x=x//10
if temp==x:
    print("number is palindrome")
else:
    print("number is not palindrome")
    print(rev)
# _____________________________________________________
# check no is armstrong number 
# _____________________________________________________

x=int(input("enter the number"))
sum=0
temp=x
count=0
while x>0:
	
	x=x//10
	count=count+1
x=temp
while x>0:
	rem=x%10
	sum=sum+rem**count
	x=x//10
	
if temp==sum:
    print("number is armstrong number")
else:
    print("number is not armstrong number")

# _____________________________________________________
# To print all the Armstrong number in between 1_10000
# _____________________________________________________

for i in range (1,10000):
    x=i
    sum=0
    temp=x
    count=0
    while x>0:	
      x=x//10
    count=count+1
    x=temp
while x>0:
    rem=x%10
    sum=sum+rem**count
    x=x//10
    	
if temp==sum:
    print(i)
    
    