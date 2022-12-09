# ======= Advent of Code ======= #

from typing import Any, Union, Dict
# from SantasHelpers import get_input
from collections import Counter

def get_input(input_file, day=0):
    x = []
    entry = []
    with open(input_file, 'r') as f:
        for line in f.readlines():
            line = line.strip().split()
            if not line:
                x.append(entry)
                entry = []
            else:
                entry.append(line)
    x.append(entry)



class Puzzle_class:
    def __init__(self, input=X) -> None:
        self.input_file = r'Data/DayX.in'
        self.input_file = r'Data/test.in'
        self.x = get_input(self.input_file, input)

    def run_day(self, part=0):
        answers = []
        a = [self.part_one(),
            self.part_two()]
        if part == 0:
            answers.append(a[0])
            answers.append(a[1])
        else:
            answers.append(a[part])
        for i in answers:
            yield i

    def part_one(self) -> int:  # Part 2
        return 

    def part_two(self) -> None:
        return

a = Puzzle_class()
print(a.part_one)
print(a.part_two)