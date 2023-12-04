# AdventOfCode

## Introduction
Welcome to my Advent of Code solutions repository! :)
I'm going to try my best to tackle the daily coding challenges presented [here](https://adventofcode.com/), a series of fun, themed, and engaging programming puzzles. 
2023 is my first time trying it out, wish me luck!
I'm also using this time to learn good practices in Git Hub simultaneously.
As of making this, I'm unsure I can complete all of the challenges, but I will absolutely try!

## Project Structure
This repository is organized by day, with each day's challenge having its own folder.
Inside each day's folder, you'll find two files.
- `Day1/Star1.py`
- `Day1/Star2.py`
- `Day2/Star1.py`
- ...
- `Day25/Star1.py`
- `Day25/Star2.py`

## How to Use
To check out the solutions:
1. Navigate to the folder for the day you're interested in.
2. Open either the `Star1.py` or `Star2.py` to see my given solution for that part of the challenge.

## Progress
- [ ] Day1: In Progress
- [x] Day2: Completed
- [ ] Day3: In Progress
- [ ] Day4: N/A
- [ ] Day5: N/A
- [ ] Day6: N/A
- [ ] Day7: N/A
- [ ] Day8: N/A
- [ ] Day9: N/A
- [ ] Day10: N/A
- [ ] Day11: N/A
- [ ] Day12: N/A
- [ ] Day13: N/A
- [ ] Day14: N/A
- [ ] Day15: N/A
- [ ] Day16: N/A
- [ ] Day17: N/A
- [ ] Day18: N/A
- [ ] Day19: N/A
- [ ] Day20: N/A
- [ ] Day21: N/A
- [ ] Day22: N/A
- [ ] Day23: N/A
- [ ] Day24: N/A
- [ ] Day25: N/A

## Reflections and Learnings
After/during each challenge, I'll add some notes here about my approach and overall thoughts. This is mostly for me to fully digest my solutions, but anyone interested obviously can read :)

### Day1
- For Star 1, I used a two-pointer method to keep track of the first and last digits.
- An improvement I would like to implement in the future is having the first pointer increment from the start of the string as the last pointer decrements from the end.
- 

### Day2
- Unfortunately, shortly after starting Day1, Star2 I became sick, but as to not fall too far behind and lose hope, I've decided to continue trying from here, although it is Day 3 as of writing this.
- My approach to Star1 was pretty simple, I noticed that each line of my input represents a game, and each set in the game is divided by a semicolon, each color/number pair divided by a comma.
- Combining this knowledge, I used a series of .strip() and .split() to break each pair into their own values (num, and color).
- I then set up the valid pairs as a dictionary and compared the value of the key in the valid dictionary to the value num (which holds the number of cubes pulled from the respective color)
- Star2 was easy enough; I simply reused my program and changed some lines to, rather than compare numbers, multiply the largest value representing a color in a game and then add the new value to a total
- Very excited to have completed my first full advent of code day!

### Day3
-

### Day4
-

### Day5
-

### Day6
-

### Day7
-

### Day8
-

### Day9
-

### Day10
-

### Day11
-

### Day12
-

### Day13
-

### Day14
-

### Day15
-

### Day16
-

### Day17
-

### Day18
-

### Day19
-

### Day20
-

### Day21
-

### Day22
-

### Day23
-

### Day24
-

### Day25
-

## Contributing
Feedback and improvements for any reason are certainly welcome! This is entirely for my own learning and education, so anything I can improve on, I accept with open arms! 
Feel free to open an issue or even a pull request if you have any ideas on how to make any solutions better or more efficient.

## License
This project is open-sourced under the MIT License.
