

def factorial(n):
    the_product = 1
    while n > 0:
        the_product *= n
        n = n - 1

    return the_product

def fac_recursive(n):
    if(n==0):
        return 1
    return n*fac_recursive(n-1)

def print_numbers(n):
    if (n == 1):
        return 1
    print(n)
    return print_numbers(n-1)

print(print_numbers(10))
