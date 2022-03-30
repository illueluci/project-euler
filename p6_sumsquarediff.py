sum_of_squares = 0
squares_of_sum = 0
for i in range(1,101):
    sum_of_squares += i**2
    squares_of_sum += i

squares_of_sum = squares_of_sum**2

print(sum_of_squares, squares_of_sum, sum_of_squares-squares_of_sum)