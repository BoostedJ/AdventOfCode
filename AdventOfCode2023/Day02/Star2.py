# Advent of Code 2023
# Day 2, Star 2

"""
problem in my words:

now with those cubes
    1. find the minimum amount of colored cubes required to make a game possible
        - for example, a game with sets with red 20, 6, and 10 will need a minimum of 20 red cubes
            - this can be done by finding altering my previous program to find the max, rather than if it's legitimate
    2. get the power of the game by multiplying the maximum numbers together
    3. sum the powers of each game, this is the result
"""

with open("game_input.txt", "r") as f:
    lines = f.readlines()


def parse_game(game: str) -> dict:
    fewest_cubes = {"red": 0, "green": 0, "blue": 0}
    game = game.split(":")[1].split(";")
    for set in game:
        set = set.split(",")
        for pair in set:
            num, color = pair.strip().split(" ")
            if int(fewest_cubes[color]) < int(num):
                fewest_cubes[color] = int(num)
    return fewest_cubes


total = 0
for line in lines:
    set_power = 1
    cubes = parse_game(line)
    for cube in cubes:
        set_power *= cubes[cube]
    total += set_power

print(total)
