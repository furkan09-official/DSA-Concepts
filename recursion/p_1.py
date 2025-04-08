# what is recursion
# what is base condition
# what is stack Overflow / stack space
# what is recursion tree : pictorial representation of eventes happening parallely


#print the integers from 1 to 10 using recursion
def print_count(count):
    if count > 10:
        return None
    else:
        print(count)
        print_count(count + 1)
print_count(1)
print('<------------------------------------------------>')

#print the name N times using recursion
def print_name(i,N):
    if i > N:
        return None
    else:
        print('Mohd Furkan')
        print_name(i + 1,N)
print_name(1,5)
print('<------------------------------------------------>')

#print 1 to N using recursion
def print_count(count,N):
    if count > N:
        return None
    else:
        print(count)
        print_count(count + 1,N)
print_count(1,20)
print('<------------------------------------------------>')

# print N to 1 using recursion
def print_count(N,count):
    if N < count:
        return None
    else:
        print(N)
        print_count(N - 1,count)
print_count(20 , 1)
print('<------------------------------------------------>')

#print th sum of frist n Naturan numbers
def sum(n):
    if n == 0:
        return 0 # if i return None the python through an error 'TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'

    else:
        return n + sum(n-1)
print(sum(20))
print('<------------------------------------------------>')

#print the factirial of n using recursion
def factorial(N):
    if N == 0:
        return 1
    else:
        return N * factorial(N - 1)
print(factorial(5))
print('<------------------------------------------------>')

#reverse an array using recursion
def reverse_array(arr , start , end):
    if start >= end:
        return None
    else:
        arr[start],arr[end] = arr[end],arr[start]
        reverse_array(arr , start + 1 , end - 1)
arr = [5,4,3,2,1]
reverse_array(arr , 0 , len(arr) -1)
print(arr)

# another method
def rev_arr(arr):
    if len(arr)  == 0:
        return []
    return [arr[-1]] + rev_arr(arr[:-1])
print(rev_arr([5,4,3,2,1]))