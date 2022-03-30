dict_of_numbers = {"1": "one",
                   "2": "two",
                   "3": "three",
                   "4": "four",
                   "5": "five",
                   "6": "six",
                   "7": "seven",
                   "8": "eight",
                   "9": "nine",
                   "10": "ten",
                   "11": "eleven",
                   "12": "twelve",
                   "13": "thirteen",
                   "14": "fourteen",
                   "15": "fifteen",
                   "16": "sixteen",
                   "17": "seventeen",
                   "18": "eighteen",
                   "19": "nineteen",
                   "20": "twenty",
                   "30": "thirty",
                   "40": "forty",
                   "50": "fifty",
                   "60": "sixty",
                   "70": "seventy",
                   "80": "eighty",
                   "90": "ninety",
                   }

all_letters_to_99 = ""

# first 99
for i in range(1,99+1):
    j = str(i)
    print(i)
    if j in dict_of_numbers:
        print(dict_of_numbers[j])
        all_letters_to_99 += dict_of_numbers[j]
        # print(all_letters_to_99)
    else:
        temp_ten = dict_of_numbers[j[0] + "0"]
        temp_ones = dict_of_numbers[j[1]]
        print(temp_ten + temp_ones)
        all_letters_to_99 += (temp_ten + temp_ones)
        # print(all_letters_to_99)

print(all_letters_to_99)
# number_of_letter_to_99 = len(all_letters_to_99)
# print(number_of_letter_to_99)
#
# # 1-9 happens to be three 3-letter words, three 4-letter words, and three 5-letter words
#
# calculating1 = number_of_letter_to_99 * 10
# calculating2 = 10*3 + 11*3 + 12*3   # hundreds ending with 00
# calculating3 = ((10*3 + 11*3 + 12*3) * 99) + (3*99)      # hundreds not ending with 00, (3*99) because "and"
# calculating4 = 11  #onethousand
# print(calculating1, calculating2, calculating3, calculating4)
# print(calculating1+calculating2+calculating3+calculating4)

# 100-999
all_letters_100_to_999 = ""

for i in range(100,999+1):
    j = str(i)
    print(i)
    if i % 100 == 0:
        print(dict_of_numbers[j[0]] + "hundred")
        all_letters_100_to_999 += (dict_of_numbers[j[0]] + "hundred")
    else:
        h,t,o = j[0], j[1], j[2]
        if t == "0":
            print(dict_of_numbers[h] + "hundred" + "and" + dict_of_numbers[o])
            all_letters_100_to_999 += dict_of_numbers[h] + "hundred" + "and" + dict_of_numbers[o]
        elif t+o in dict_of_numbers:
            print(dict_of_numbers[h] + "hundred" + "and" + dict_of_numbers[t+o])
            all_letters_100_to_999 += dict_of_numbers[h] + "hundred" + "and" + dict_of_numbers[t+o]
        else:
            print(dict_of_numbers[h] + "hundred" + "and" + dict_of_numbers[t+"0"] + dict_of_numbers[o])
            all_letters_100_to_999 += dict_of_numbers[h] + "hundred" + "and" + dict_of_numbers[t+"0"] + dict_of_numbers[o]

print(all_letters_100_to_999)

print(len(all_letters_to_99), len(all_letters_100_to_999), len("onethousand"))
print(len(all_letters_to_99) + len(all_letters_100_to_999) + len("onethousand"))  #onethousand




