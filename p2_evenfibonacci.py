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

n = 1
summ = 0
while True:
    if fibonacci(n) > 4000000:
        break
    if fibonacci(n) % 2 == 0:
        summ += fibonacci(n)
    n += 1

print(summ)


