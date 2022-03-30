import math


def is_prime(n):
    rootn = int(math.sqrt(n)) + 1
    for i in range(2,rootn):
        if n % i == 0:
            return False
    return True


def fibonacci(n):
    a = 1
    b = 2
    if n == 1:
        return a
    elif n == 2:
        return b
    else:
        for i in range(2,n):
            temp = a+b
            a = b
            b = temp
        return b


def generate_prime_list(n):
    prime_list = [i for i in range(2,n) if is_prime(i)]
    return prime_list


def triangular_number(n):
    summ = 0
    for i in range(1,n+1):
        summ += i
    return summ

