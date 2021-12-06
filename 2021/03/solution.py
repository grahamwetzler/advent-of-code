from collections import Counter
from pathlib import Path


def parse_input():
    puzzle_input = Path("2021/03/input.txt").read_text()
    rows = puzzle_input.split()
    return rows


def bit_list_to_int(bits: list):
    return int("".join(bits), 2)


def count_bits(rows: list) -> list[Counter]:
    bits = len(rows[0])
    counts = []
    for idx in range(bits):
        columns = [i[idx] for i in rows]
        counter = Counter(columns)
        counts.append(counter)

    return counts


def part_1() -> int:
    rows = parse_input()
    counts = count_bits(rows)

    gamma = []
    epsilon = []
    for count in counts:
        (high, _), (low, _) = count.most_common()
        gamma.append(high)
        epsilon.append(low)

    return bit_list_to_int(gamma) * bit_list_to_int(epsilon)


if __name__ == "__main__":
    print("Part 1:", part_1())
