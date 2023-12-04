from input import get_day_input
from loguru import logger

puzzle_input = get_day_input(3)
logger.info("Fetched puzzle input")
lines = puzzle_input.splitlines()

n = len(lines)
m = len(lines[0])

goods = [[[] for _ in range(m)] for _ in range(n)]

def is_symbol(i, j, num):
    if not (0 <= i < n and 0 <= j < m):
        return False

    if lines[i][j] == "*":
        goods[i][j].append(num)
    return lines[i][j] != "." and not lines[i][j].isdigit()


part_sum = 0
for i, line in enumerate(lines):
    j = 0
    while j < m:
        start = j
        num = ""
        while j < m and line[j].isdigit():
            num += line[j]
            j += 1

        if num == "":
            j += 1
            continue

        num = int(num)

        # Number ended, look around
        if is_symbol(i, start - 1, num) or is_symbol(i, j, num):
            part_sum += num
        for k in range(start - 1, j + 1):
            if is_symbol(i - 1, k, num) or is_symbol(i + 1, k, num):
                part_sum += num
                break

logger.success(f"Sum of all part numbers: {part_sum}")

ans = 0
for i in range(n):
    for j in range(m):
        nums = goods[i][j]
        if lines[i][j] == "*" and len(nums) == 2:
            ans += nums[0] * nums[1]

print(ans)
logger.success(f"Gear Rat.: {ans}")
