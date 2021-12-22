from dataclasses import dataclass
from functools import lru_cache
from itertools import cycle, product
from pathlib import Path


@dataclass
class Player:
    score: int = 0
    wins: int = 0

    def __init__(self, id: int, position: int) -> None:
        self.id = id
        self.position = position
        self.starting_postition = position

    def reset(self):
        self.position = self.starting_postition
        self.score = 0


def move(position: int, score: int, roll: int) -> tuple[int]:
    position = (position + roll - 1) % 10 + 1
    return position, score + position


def part_1(starting_positions):
    die = cycle(range(1, 101))
    rolls = 0
    players = [Player(player, position) for player, position in starting_positions]

    while True:
        for player in players:
            roll = next(die) + next(die) + next(die)
            rolls += 3
            player.position, player.score = move(player.position, player.score, roll)
            if player.score >= 1000:
                return min(player.score for player in players) * rolls


def part_2(p1, p2):
    @lru_cache(maxsize=None)
    def count_wins(p1, p2):
        p1_wins = p2_wins = 0
        for a, b, c in product(range(1, 4), repeat=3):
            _, score = roll_p1 = move(*p1, a + b + c)
            if score >= 21:
                p1_wins += 1
            else:
                roll_p2_wins, roll_p1_wins = count_wins(p2, roll_p1)
                p1_wins += roll_p1_wins
                p2_wins += roll_p2_wins

        return p1_wins, p2_wins

    return max(count_wins((p1, 0), (p2, 0)))


if __name__ == "__main__":
    puzzle_input = Path("2021/21/input.txt").read_text().splitlines()
    starting_positions = [(idx, int(p[-1])) for idx, p in enumerate(puzzle_input, 1)]
    print("Part 1:", part_1(starting_positions))
    print("Part 2:", part_2(7, 5))
