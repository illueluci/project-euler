answer_list = []

for i in range(999,800, -1):
    for j in range(999,800, -1):
        temp = str(i*j)
        if temp == temp[::-1]:
            answer_list.append(int(temp))
            # print(temp)

print(sorted(answer_list))