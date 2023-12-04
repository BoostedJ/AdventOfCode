# Advent of Code 2023
# Day 2, Star 1

"""
problem in my words:

the game being played is a simple colored cubes game, where cubes are randomly drawn from a bag
the bag has exactly 12 red cubes, 13 green cubes, and 14 blue cubes
each game has a unique id, the first game is game 1, second game 2, etc.
each game also has a ";" divider, signifying the end of a set

given a file with 100 games played:
    1. find if the game played is a legitimate game
        - a game is considered legitimate if there are 12 or less red cubes played, etc. in a set
        - at the end of a set, the cubes are put back into the bag, so I only care about the total in a set
    2. if a game is legitimate, add the game's id to a total
    3. print that total, this is the answer
"""

with open("game_input.txt", "r") as f:
    lines = f.readlines()

valid_nums = {"red": 12, "green": 13, "blue": 14}


def parse_game(game: str) -> bool:
    game = game.split(":")[1].split(";")
    for set in game:
        set = set.split(",")
        for pair in set:
            num, color = pair.strip().split(" ")
            if valid_nums[color] < int(num):
                return False
    return True


total_ids = 0
for i in range(len(lines)):
    game_id = i+1
    if parse_game(lines[i]):
        total_ids += game_id

print(total_ids)