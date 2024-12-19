import math
def is_power(n):
    if n & (n-1) == 0:
        return True
    return False

def iseven(n):
    return not n & 1

def fizzbuzz(n):
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif(i % 3 == 0):
            print("Fizz")
        elif(i % 5 == 0):
            print("Buzz")
        else:
            print(i)


def gcf(i1,i2):
    gcf = None
    if i1 > i2:
        smaller = i2
    else:
        smaller = i1
    for i in range(1,smaller+1):
        if i1 % i==0 and i2 % i==0:
            gcf = i

    return gcf

def gcf_euclid(x,y):
    if y==0:
        x,y=y,x
    while y!=0:
        x,y = y,x % y
    return x

def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False

    return True

def is_prime_improved(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False

    return True