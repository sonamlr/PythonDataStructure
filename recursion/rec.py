# recursive function
# print sum of n natural numbers
def fun(n):
    if n == 1:
        return 1
    else:
       s = n + fun(n-1)
       return s
rec = fun(5)
print(rec)

#print n natural number
def natural_number(num):
    if num > 0:
        natural_number(num - 1)
        print(num, end=' ')
natural_number(10)
        
#print n natural number in reverse order
def natural_number(num):
    if num > 0:
        print(num, end=' ')
        natural_number(num-1)
natural_number(10)

# print n odd number
def odd_number(n):
    if n > 0:
        odd_number(n-1)
        print(2*n-1, end=' ')
odd_number(10)

# print n odd number in reverse order
def odd_number(n):
    if n > 0:
            print(2*n-1, end=' ')
            odd_number(n-1)

odd_number(10)

# print n even number
def even_number(n):
    if n > 0:
        even_number(n-1)
        print(2*n, end=' ')
even_number(10)

# print n even number in reverse order
def even_number(n):
    if n > 0:
            print(2*n, end=' ')
            even_number(n-1)
even_number(10)











