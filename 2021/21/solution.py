from pathlib import Path


class DeterministicDie:
    def __init__(self) -> None:
        self.state = 0
        self.times_rolled = 0

    def roll3(self):
        values = []
        for _ in range(3):
            values.append(self._roll())

        return sum(values)

    def _roll(self):
        self.state += 1
        self.times_rolled += 1

        if self.state > 100:
            self.state = 1

        return self.state


def move(start, roll):
    _, remainder = divmod(start + roll, 10)

    if remainder == 0:
        return 10

    return remainder


def part_1(starting_positions):
    die = DeterministicDie()
    p1, p2 = starting_positions

    p1 = move(p1, die.roll3())
    p2 = move(p2, die.roll3())

    scores = [p1, p2]

    while True:

        p1 = move(p1, die.roll3())
        scores[0] += p1
        if scores[0] >= 1000:
            break

        p2 = move(p2, die.roll3())
        scores[1] += p2
        if scores[1] >= 1000:
            break

    return min(scores) * die.times_rolled


def part_2():
    ...


if __name__ == "__main__":
    puzzle_input = Path("2021/21/input.txt").read_text().splitlines()
    starting_positions = [int(p[-1]) for p in puzzle_input]
    print("Part 1:", part_1(starting_positions))
