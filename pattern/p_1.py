# print the gievn pattern
# *******
# *******
# *******
# *******

def pattern_1(n):
    # method 1
    for i in range(n):
        for j in range(n):
            print('*', end=" ")
        print()


    # method 2
    for i in range(n):
        print('*'*n)
    print()


def double_traingle(n):
    for i in range((2*n)):
        stars = i
        if (i > n):
            stars= (2*n)-i
        for j in range(stars):
            print('*',end = " ")
        print()

def print10(n):
    start = 1
    for i in range(n):
        if (i %2 == 0): start = 1
        else: start = 0
        for j in range(i+1):
            print(start,end =" ")
            start = 1-start
        print()

def print11(n):
    
    space = 2 * (n-1)
    for i in range(1 ,n+1):
        for j in range(i):
            print(j+1,end = " ")
        
        for j in range(space):
            print(" ",end= " ")

        for j in range(i):
            print(j+1,end = " ")
        print()
        space = space -2


def print12(n):
    num = 1
    for i in range(n+1):
        for j in range(i):
            print(num, end= " ")
            num += 1
        print()

def pattern13(n):
    for i in range(n+1):
        for j in range(i):
            print(chr(65+j) , end= " ")
        print()
def pattern14(n):
    for i in range(n+1):
        for j in range(n-i):
            print(chr(65 + j),end = " ")
        print()

def pattern15(n):
    for i in range(n+1):
        for j in range(i+1):
            print(chr(65 + i),end = " ")
        print()

def pattern16(n):
    for i in range(n+1):
        for j in range(n-i-1):
            print(" ",end = " ")
        char = chr(65)
        for j in range(2 * i -1):
            if (i<n//2):
                print(char,end = " ")
                char += 1
            else:
                print(char , end= " ")
                char -= 1

        for j in range(n - i-1):
            print(" ",end = " ")
        print()

        


size = int(input())
# pattern_1(size)
# double_traingle(size)
# print10(size)
# print11(size)
# print12(size)
# pattern13(5)
# pattern14(size)
# pattern15(size)
pattern16(size)

name = chr(65)
print(name)