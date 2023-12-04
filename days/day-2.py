from input import get_day_input
from loguru import logger

puzzle_input = get_day_input(2)
logger.info("Fetched puzzle input")

limits = {'red': 12, 'green': 13, 'blue': 14}


def parse_game_data(game_entry: str) -> tuple[int, list[tuple[int, ...]]]:
    game_id, game_data = game_entry.split(':')
    game_id = int(game_id.split(' ')[1])

    colors = {'red': 0, 'green': 1, 'blue': 2}
    subsets = [subset.strip() for subset in game_data.split(';')]
    indice_vec = []

    for subset in subsets:
        counts = [0, 0, 0]  # red, green, blue
        for color_info in subset.split(','):
            count, color = [x.strip() for x in color_info.split()]
            counts[colors[color]] += int(count)
        indice_vec.append(tuple(counts))

    return game_id, indice_vec


def is_game_possible(game):
    for subset in game[1]:
        if (subset[0] > limits['red'] or
                subset[1] > limits['green'] or
                subset[2] > limits['blue']):
            return False
    return True


def find_minimum_cubes(game):
    min_cubes = [0, 0, 0]  # red, green, blue
    for subset in game[1]:
        min_cubes = [max(min_cubes[i], subset[i]) for i in range(3)]
    return min_cubes


def calculate_power(cube_set):
    return cube_set[0] * cube_set[1] * cube_set[2]


games = [parse_game_data(game_entry) for game_entry in puzzle_input.splitlines()]

sum_of_ids = sum(game[0] for game in games if is_game_possible(game))
logger.success(sum_of_ids)

min_cubes_per_game = [find_minimum_cubes(game) for game in games]
powers = [calculate_power(cube_set) for cube_set in min_cubes_per_game]
total_power = sum(powers)
logger.success(total_power)
