from typing import List
from input import get_day_input
from loguru import logger
import re

nums: List[int] = []

puzzle_input = get_day_input(1)
logger.info("Fetched puzzle input")


def first_last(string: str) -> int:
    replacements = {
        "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8",
        "nine": "9",
    }
    needles = re.findall(r'(?=(\d|zero|one|two|three|four|five|six|seven|eight|nine))', string)
    needles = [(replacements[t] if not t.isnumeric() else t) for t in needles]

    return needles[0] + needles[-1]


logger.success(f"Result is: {sum([int(first_last(line)) for line in puzzle_input.splitlines()])}")
