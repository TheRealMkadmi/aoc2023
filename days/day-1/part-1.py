from typing import List
from input import get_day_input
from loguru import logger

puzzle_input = get_day_input(1)
logger.info("Fetched puzzle input")

nums: List[int] = []


def get_first_int(string: str) -> int:
    for char in string:
        if char.isdigit():
            return int(char)


for line in puzzle_input.splitlines():
    first_int = get_first_int(line)
    second_int = get_first_int(line[::-1])
    nums.append(int(str(first_int) + str(second_int)))

logger.success(f"Result is: {sum(nums)}")
