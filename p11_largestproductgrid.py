grid_conv_to_list = []

with open("p11_question.txt") as grid:
    for line in grid.readlines():
        split_line_str = line.split()
        # print(split_line_str)
        split_line_int = [int(number) for number in split_line_str]
        # print(split_line_int)
        grid_conv_to_list.append(split_line_int)

print(grid_conv_to_list)

max_horizontal = 0
max_vertical = 0
max_diag_top_right = 0
max_diag_bott_right = 0

#horizontal
for row in range(0,20):
    for column in range(0,17):
        tempa = grid_conv_to_list[row][column]
        tempb = grid_conv_to_list[row][column+1]
        tempc = grid_conv_to_list[row][column+2]
        tempd = grid_conv_to_list[row][column+3]
        tempproduct = tempa * tempb * tempc * tempd
        if max_horizontal < tempproduct:
            max_horizontal = tempproduct
print(max_horizontal)

#vertical
for row in range(0,17):
    for column in range(0,20):
        tempa = grid_conv_to_list[row][column]
        tempb = grid_conv_to_list[row+1][column]
        tempc = grid_conv_to_list[row+2][column]
        tempd = grid_conv_to_list[row+3][column]
        tempproduct = tempa * tempb * tempc * tempd
        if max_vertical < tempproduct:
            max_vertical = tempproduct
print(max_vertical)

#diag_top_right
for row in range(3,20):
    for column in range(0,17):
        tempa = grid_conv_to_list[row][column]
        tempb = grid_conv_to_list[row-1][column+1]
        tempc = grid_conv_to_list[row-2][column+2]
        tempd = grid_conv_to_list[row-3][column+3]
        tempproduct = tempa * tempb * tempc * tempd
        if max_diag_top_right < tempproduct:
            max_diag_top_right = tempproduct
print(max_diag_top_right)

#diag_bottom_right
for row in range(0,17):
    for column in range(0,17):
        tempa = grid_conv_to_list[row][column]
        tempb = grid_conv_to_list[row+1][column+1]
        tempc = grid_conv_to_list[row+2][column+2]
        tempd = grid_conv_to_list[row+3][column+3]
        tempproduct = tempa * tempb * tempc * tempd
        if max_diag_bott_right < tempproduct:
            max_diag_bott_right = tempproduct
print(max_diag_bott_right)

print(max(max_vertical, max_horizontal, max_diag_top_right, max_vertical))