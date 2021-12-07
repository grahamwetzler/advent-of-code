from pathlib import Path
from statistics import median


class Crabs:
  def __init__(self, part: int):
    puzzle = Path("2021/07/input.txt").read_text().split(",")
    self.part = part
    self.positions = [int(i) for i in puzzle]
    match part:
      case 1:
        self.fuel_cost = self.part_1()
      case 2:
        self.fuel_cost = self.part_2()

  def __repr__(self) -> str:
    return f"Part {self.part}: {self.fuel_cost}"

  def part_1(self) -> int:
    optimal_position = int(median(self.positions))
    return sum([abs(p - optimal_position) for p in self.positions])

  def part_2(self) -> int:
    fuel_costs = []
    for position in range(len(self.positions)):
      fuel_costs.append(
        sum([sum(range(abs(p - position) + 1)) for p in self.positions])
        )
    
    return min(fuel_costs)

if __name__ == "__main__":
  print(Crabs(part=1))
  print(Crabs(part=2))
