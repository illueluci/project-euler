import math


def brute_force_factor(n):
    for i in range(1, n):
        if n % i == 0:
            print(i)


x = 600851475143
# rootx = int(math.sqrt(x)) + 1
answer = []
#
# for i in range(1, rootx):
#     if x % i == 0:
#         answer.append((i,x//i))
#
# for a,b in answer:
#     print(f"{a},{b}")

i = 2
while i < x:
    if x % i == 0:
        answer.append(i)
        x //= i
        i = 2
    i += 1
else:
    answer.append(x)

print(answer)
brute_force_factor(answer[3])