from collections import Counter
from pathlib import Path


def parse_input():
    puzzle_input = Path("2021/03/input.txt").read_text()
    puzzle_input = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""
    return puzzle_input


if __name__ == "__main__":
    puzzle_input = parse_input()
    rows = puzzle_input.split()
    bits = len(rows[0])

    gamma = ""
    epsilon = ""
    for idx in range(bits):
        columns = [i[idx] for i in rows]
        gamma, epsilon += Counter(columns).keys()
        print(gamma)
        print(epsilon)
