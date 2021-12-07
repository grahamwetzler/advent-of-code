from pathlib import Path

class School:
    def __init__(self, days: int):
        self.days = days
        self.ages = self.parse_input()
        self.timers = {k: 0 for k in range(9)}
        for age in self.ages:
            self.timers[age] += 1
        self.step(self.days)

    def parse_input(self) -> list:
        puzzle_input = Path("2021/06/input.txt").read_text()
        split = puzzle_input.split(",")
        return [int(n) for n in split]
    
    def step(self, days):
        for _ in range(days):
            new_fish = 0
            for timer, timer_value in self.timers.items():
                if timer == 0:
                    new_fish += timer_value
                else:
                    self.timers[timer-1] = timer_value

            self.timers[8] = new_fish
            self.timers[6] += new_fish

        return self

    @property
    def size(self) -> int:
        return sum(self.timers.values())


if __name__ == "__main__":
    print("Part 1:", School(18).size)
    print("Part 2:", School(256).size)
