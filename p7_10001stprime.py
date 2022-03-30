import math

def is_prime(n):
    rootn = int(math.sqrt(n)) + 1
    for i in range(2,rootn):
        if n % i == 0:
            return False
    return True

counter = 1
for i in range(2,200000):
    if is_prime(i):
        print(counter, i)
        counter += 1
    if counter == 10002:
        break

