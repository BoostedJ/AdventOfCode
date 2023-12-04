# Advent of Code 2023
# Day 1, Star 1

"""
problem in my words:

given a file of 1000 lines of "random" text and numbers,
    1. find the first and last digit in the line
        - if the digit is the only in the line, it counts as both
    2. concatenate the first and last digit (e.g. first = 1, last = 2, the number is 12)
    3. combine the resulting number in a total
    4. print the total, this is the answer
"""

# calibration_input.txt is my specific puzzle inputs
f = open("calibration_input.txt", "r")
lines = f.readlines()

total = 0
for line in lines:
    first = None
    last = None
    for char in line:
        if char.isdigit():
            if first:
                last = char
            else:
                first = char
                last = char
    total += int(str(first + last))

print(total)
