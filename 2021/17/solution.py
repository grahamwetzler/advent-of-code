import itertools
import re
from pathlib import Path
from typing import Optional


def parse_input(puzzle_input: str) -> tuple[int]:
    x, y = re.findall("=([\d\.-]+)", puzzle_input)
    (x_min, x_max), (y_min, y_max) = x.split(".."), y.split("..")
    x_min, x_max, y_min, y_max = int(x_min), int(x_max), int(y_min), int(y_max)
    return x_min, x_max, y_min, y_max


def is_in_target_area(x: int, y: int) -> bool:
    if (x_min <= x <= x_max) and (y_min <= y <= y_max):
        return True
    return False


def launch_probe(x_velocity: int, y_velocity: int) -> Optional[int]:
    x, y = (0, 0)
    y_values = []
    while True:
        x += x_velocity
        if is_in_target_area(x, y):
            return max(y_values)

        y += y_velocity
        y_values.append(y)
        if is_in_target_area(x, y):
            return max(y_values)

        if x_velocity > 0:
            x_velocity -= 1
        elif x_velocity < 0:
            x_velocity += 1

        y_velocity -= 1

        if x > x_max or y < y_min:
            return None


def part_1() -> int:
    heighest_y = []
    for x_velocity, y_velocity in itertools.product(range(0, 250), range(-250, 250)):
        if y_values := launch_probe(x_velocity, y_velocity):
            heighest_y.append(y_values)

    return max(heighest_y)


def part_2():
    ...


if __name__ == "__main__":
    puzzle_input = Path("2021/17/input.txt").read_text()
    x_min, x_max, y_min, y_max = parse_input(puzzle_input)
    print("Part 1:", part_1())
