import requests


# yes it's sync. I don't care.
def get_day_input(day: int) -> str:
    r = requests.get(f"https://adventofcode.com/2023/day/{day}/input", cookies={"session": open("../../cookie.txt").read()})
    return r.text
