# print the given pattern
# *
# **
# ***
# ****
# *****

def right_traingle(n):
    # method 1
    for i in range(n):
        for j in range(i+1):
            print('*',end= " ")
        print()
    

    # method 2
    for i in range(n):
        print('*'*i)
    print()
# size = int(input())
# right_traingle(size)

# print the gievn pattern
# 1
# 12
# 123
# 1234

def cout_traingle(n):
    for i in range(n):
        for j in range(i+1):
            print(j+1,end= " ")
        print()


def count_trainle_1(n):
    for i in range(n):
        for j in range(i+1):
            print(i+1,end= " ")
        print()

# count_trainle_1(size)

def reverse_traingle(n):
    for i in range(n):
        for j in range(n-i):
            print('*',end=" ")
        print()


def Reverse_cout_tri(n):
    for i in range(n):
        for j in range(n-i):
            print(j+1,end= " ")
        print()


def traingle(n):
    for i in range(1 , n+1):
        for j in range(n-i):
            print(" ",end = " ")
        for j in range(i*2-1):
            print('*',end = " ")
        for j in range(n-i):
            print(" ",end = " ")
        print()
print()
def traingle_1(n):
    for i in range(1,n+1):
        for j in range(i):
            print(" ",end = " ")
        for j in range(2*n - (2*i +1)):
            print("*",end = " ")
        for j in range(i):
            print(" ",end = " ")
        print()

        
size = int(input())
# cout_traingle(size)
# reverse_traingle(size)
# Reverse_cout_tri(size)
traingle(size)
traingle_1(size)