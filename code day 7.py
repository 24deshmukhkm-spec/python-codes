# [1] If any of the width or height is less than L, user is prompted to upload another one. Print "UPLOAD ANOTHER" in this case.
# [2] If width and height, both are large enough and
# (a) if the photo is already square then it is accepted. Print "ACCEPTED" in this case.
# (b) else user is prompted to crop it. Print "CROP IT" in this case.
# L = int(input())
# N = int(input())

# for i in range(N):
#     W,H=map(int,input().split())
#     if W<L or H<L :
#         print("UPLOAD ANOTHER")
#     elif W==H :
#         print("ACCEPTED")
#     else:
#         print("CROP IT")

# Monk and Rotation
#    T= int(input())
# for i in range(T):
#     N,K= map(int,input().split())
#     Arr=list(map(int,input().split()))
#     K= K%N
    
#     a3=Arr[N-K:]+Arr[:N-K]
#     print(*a3)
             
# You have been given a String S consisting of uppercase and lowercase English alphabets. You need to change the case of each alphabet in this String. That is, all the uppercase letters should be converted to lowercase and all the lowercase letters should be converted to uppercase. You need to then print the resultant String to output.
# S=(input())
# ans=""
# for i in S:
#     if i.isupper():
#         ans+=i.lower()
#     elif i.islower():
#         ans+=i.upper()
# print (ans)
# ELSE------------------------------------------------------------------------------------------------------
# S=input()
# ans=S. swapcase()
# print (ans)

Arr=list(map(int,input().split()))
K=int(input('num of rotation'))
for i in range(K):
    