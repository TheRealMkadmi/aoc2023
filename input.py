import os

import requests


# yes it's sync. I don't care.
def get_day_input(day: int) -> str:
    script_dir = os.path.dirname(os.path.realpath(__file__))
    cookie_path = os.path.join(script_dir, 'cookie.txt')

    with open(cookie_path, 'r') as file:
        cookie = file.read().strip()

    r = requests.get(f"https://adventofcode.com/2023/day/{day}/input", cookies={"session": cookie})
    return r.text
