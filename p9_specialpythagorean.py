import math

for a in range(1,1000):
    for b in range(1,1000):
        c_squared = (a**2)+(b**2)
        c = math.sqrt(c_squared)
        if c.is_integer():
            c = int(c)
            # print(a,b,c)
            if a+b+c == 1000:
                print(a*b*c)
