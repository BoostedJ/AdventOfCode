# This is how I made the process more streamlined, so I don't have to individually make each day and star
# Feel free to use and change the base_path to your desired path

import os

base_path = r'C:\School\Python Projects\AdventOfCode\AdventOfCode2023'

if not os.path.exists(base_path):
    os.makedirs(base_path)

for day in range(1, 26):
    day_folder = os.path.join(base_path, f'Day{day:02d}')
    os.makedirs(day_folder, exist_ok=True)

    for star in range(1, 3):
        file_path = os.path.join(day_folder, f'Star{star}.py')
        with open(file_path, 'w') as file:
            file.write("# Advent of Code 2023\n")
            file.write(f"# Day {day}, Star {star}\n\n")