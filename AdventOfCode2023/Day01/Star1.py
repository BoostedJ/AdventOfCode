# Advent of Code 2023
# Day 1, Star 1

# star_1_input.txt is my specific puzzle inputs
f = open("star_1_input.txt", "r")
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
