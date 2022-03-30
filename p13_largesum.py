summ = 0
with open("p13_question.txt") as question:
    for line in question.readlines():
        summ += int(line)
        print(summ)