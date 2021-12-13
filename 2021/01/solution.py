from pathlib import Path


def part_1(puzzle_input):
    increased = 0
    for idx, number in enumerate(puzzle_input):
        if number > puzzle_input[idx - 1]:
            increased += 1

    return increased


def part_2(puzzle_input):
    increased = 0
    for idx in range(1, len(puzzle_input)):
        if sum(puzzle_input[idx : idx + 3]) > sum(puzzle_input[idx - 1 : idx + 2]):
            increased += 1

    return increased


if __name__ == "__main__":
    puzzle_input = [
        int(i) for i in Path("2021/01/input.txt").read_text().split("\n") if i
    ]
    print("Part 1:", part_1(puzzle_input))
    print("Part 2:", part_2(puzzle_input))
