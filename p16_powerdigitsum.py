a = 2**1000
a_str = str(a)
summ = 0
for char in a_str:
    summ += int(char)

print(summ)