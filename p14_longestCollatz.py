def make_collatz_list(n):
    c_list = [n,]
    while c_list[-1] != 1:
        if c_list[-1] % 2 == 0:
            next = c_list[-1] // 2
        else:
            next = (c_list[-1] * 3) + 1
        c_list.append(next)
    return c_list


max_length = 0
for i in range(1,1000000):
    temp = make_collatz_list(i)
    if max_length < len(temp):
        max_length = len(temp)
        print(max_length, i)


