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


#sum of n natural number
def sumN(n):
    if n == 1:
        return 1
    else:
        s =  n + sumN(n-1)
        return s   
num = sumN(5)
print(num)


#sum of n odd number
def sumNodd(n):
    if n == 1:
        return 1
    else:
        s =  (2*n-1) + sumNodd(n-1)
        return s   
num = sumNodd(5)
print(num)

#sum of n even number
def sumNeven(n):
    if n == 0:
        return 0
    else:
        s =  (2*n) + sumNeven(n-1)
        return s   
num = sumNeven(5)
print(num)

#factorial of n number 
def fac(n):
    if n==1:
        return 1
    else:
        s = n * fac(n-1)
        return s
print(fac(5))

# sum of squares of n natural number
def sum_square(n):
    if n==1:
        return n
    else:
        s = n*n + (sum_square(n-1))
        return s
print(sum_square(5))












