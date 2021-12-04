import re
from pathlib import Path
import pprint
from dataclasses import dataclass

BOARD_WIDTH = 5
BOARD_HEIGHT = 5

puzzle_input = Path("2021/04/input.txt").read_text()
# puzzle_input = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

# 22 13 17 11  0
#  8  2 23  4 24
# 21  9 14 16  7
#  6 10  3 18  5
#  1 12 20 15 19

#  3 15  0  2 22
#  9 18 13 17  5
# 19  8  7 25 23
# 20 11 10 24  4
# 14 21 16 12  6

# 14 21 17 24  4
# 10 16 15  9 19
# 18  8 23 26 20
# 22 11 13  6  5
#  2  0 12  3  7"""

numbers, *boards_str = puzzle_input.split("\n" * 2)

drawn_numbers = [int(number) for number in numbers.split(",")]


@dataclass
class Number:
    number: int
    marked: bool = False

    def __init__(self, number):
        self.number = int(number)

    def __repr__(self) -> str:
        return f"{self.number}{'*' if self.marked else ''}"


@dataclass
class Board:
    numbers: list[list[Number]]

    def __repr__(self):
        return pprint.pformat(self.numbers)

    def update(self, drawn: int):
        for row in self.numbers:
            for number in row:
                if number.number == drawn:
                    number.marked = True

    @property
    def is_winner(self) -> bool:
        for row in self.numbers:
            marked_row_count = 0
            for number in row:
                if number.marked:
                    marked_row_count += 1
            if marked_row_count == BOARD_WIDTH:
                return True

        for column in range(BOARD_WIDTH):
            marked_column_count = 0
            for row in self.numbers:
                if row[column].marked:
                    marked_column_count += 1
            if marked_column_count == BOARD_HEIGHT:
                return True

        return False

    @property
    def score(self) -> int:
        score = 0
        if self.is_winner:
            for row in self.numbers:
                for number in row:
                    if not number.marked:
                        score += number.number
        return score


boards = []

for board in boards_str:
    board_list = []
    for row in [i for i in board.split("\n") if i != ""]:
        row_items = []
        for column in [i for i in row.split(" ") if i != ""]:
            number = Number(column)
            row_items.append(number)

        board_list.append(row_items)
    boards.append(Board(board_list))


def part_1():
    for draw in drawn_numbers:
        for board in boards:
            board.update(draw)
            if board.is_winner:
                return board.score * draw


print(part_1())
