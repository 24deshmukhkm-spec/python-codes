# __________________________________________________________________________________________________
# hw- sum of nine digit number & reverse it 

no=int(input("enter the sequence fo num "))
n1=no%10
no=no//10

n2=no%10
no=no//10

n3=no%10
no=no//10

n4=no%10
no=no//10

n5=no%10
no=no//10

n6=no%10
no=no//10

n7=no%10
no=no//10

n8=no%10
no=no//10

n9=no%10

res=n1+n2+n3+n4+n5+n6+n7+n8+n9
out=n1*100000000+n2*10000000+n3*1000000+n4*100000+n5*10000+n6*1000+n7*100+n8*10+n9
print(res)
print(out)
# ____________________________________________________________________________________________________

# cw- 

# find last digit
no=int(input("enter the sequence fo num "))
a=no%10
print(a)

# sum of  numbers by taking single two digit value
no=int(input("enter the sequence fo num "))
a=no%10
b=no//10
c=a+b
print(c)

# sum of numbers by taking single three digit value
no=int(input("enter the sequence fo num "))
n1=no%10
no=no//10
n2=no%10
n3=no//10
res=n1+n2+n3
print(res)

# sum of numbers by taking single five digit value

no=int(input("enter the sequence fo num "))
n1=no%10
n2=no//10000
no=no//10
n3=no%10
no=no//10
n4=no%10
no=no//10
n5=no%10
res=n1+n2+n3+n4+n5
print(res)

# reverse of five digit number
no=int(input("enter the sequence fo num "))
n1=no%10
no=no//10
n2=no%10
no=no//10
n3=no%10
no=no//10
n4=no%10
no=no//10
n5=no%10
res=n1*10000+n2*1000+n3*100+n4*10+n5
print(res)

# accept 9 digit num and find sum of first and last digit
no=int(input("enter the sequence fo num "))
n1=no%10
n2=no//100000000
res=n1+n2
print(res)

# accept basic salary and calculate cross salary whare ta=30,da=20,hra=40
bs=int(input("enter salary"))
ta=bs*.20
da=bs*.30
hra=bs*.40
gs=ta+da+hra
print(gs)
