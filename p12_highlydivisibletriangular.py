import math

def triangular_number(n):
    summ = 0
    for i in range(1,n+1):
        summ += i
    return summ


number_list = [triangular_number(i) for i in range(12000,13000+1)]

for index in range(0,(13000+1-12000)):
    divisor_counter = 0
    for divisor in range(1, int(math.sqrt(number_list[index]))):
        if number_list[index] % divisor == 0:
            divisor_counter += 2
            # the number will be divisible by the divisor and the result of division
            # also, just check up to the square root of the number
    print(divisor_counter, number_list[index], index+12000)
    if divisor_counter > 500:
        print("*" * 20)
        print(divisor_counter, number_list[index], index+12000)
        break


# for i_tri in range(1000,10000 +1):
#     test = triangular_number(i_tri)
#     divisor_counter = 0
#     for divisor in range(1, test+1):
#         if test % divisor == 0:
#             divisor_counter += 1
#     print(divisor_counter, test, i_tri)
#     if divisor_counter > 500:
#         print("*" * 20)
#         print(i_tri, test, divisor_counter)
#         break
