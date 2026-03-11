# for i in range (1,5):
#     for j in range (1,5):
#         print(i,end="")
#     print()
#  output
#  1 1 1 1
#  2 2 2 2
#  3 3 3 3        
#  4 4 4 4   

# n=1
# for i in range (1,5):
#     for j in range (1,5):
#         print(n,end="\t")
#         n=n+1
#     print()
# #  output
# 1       2       3       4
# 5       6       7       8
# 9       10      11      12
# 13      14      15      16

# n=65
# for i in range (1,5):
#     for j in range (1,5):
#         print(chr(n),end="")
#         n=n+1
#     print()

# output
# ABCD
# EFGH
# IJKL
# MNOP


# for i in range (1,5):
#     for j in range (1,i+1):
#         print(i,end="")
#     print()

# output
# 1
# 22
# 333
# 4444

# for i in range (4,0,-1):
#     for j in range (1,i+1):
#         print("*",end="")
#     print()

# output
# ****
# ***
# **
# *

# ls=[1,2,3,4,5,6,7]
# print(type(ls))
# print(ls)

# output

# <class 'list'>
# [1, 2, 3, 4, 5, 6, 7]


#     0  1  2  3  4
# ls=[12,43,56,76,89]
# for i in range(len(ls)):
#     print(ls[i])

# output

# 12
# 43
# 56
# 76
# 89

# ls=[12,43,56,76,89]
# for i in ls:
#     print(i)

# output
# 12
# 43
# 56
# 76
# 89

# ls=[12,43,56,76,89,77,88,99]
# print(ls)
# ls.append(90)
# print(ls)
# ls.pop(3)
# print(ls)
# print(ls[3])
# print(ls[-1])
# print(ls[2:6])
# print(ls[2:])
# print(ls[:3])
# print(ls[::2])
# print(ls[::-1])


# output

# [12, 43, 56, 76, 89, 77, 88, 99]
# [12, 43, 56, 76, 89, 77, 88, 99, 90]
# [12, 43, 56, 89, 77, 88, 99, 90]
# 89
# 90
# [56, 89, 77, 88]
# [56, 89, 77, 88, 99, 90]
# [12, 43, 56]
# [12, 56, 77, 99]
# [90, 99, 88, 77, 89, 56, 43, 12]

# a="kartik"
# print(a[::-1])  

#output=kitrak

# no=1234
# no=str(no)
# print(no[::-1])

# output
# 4321