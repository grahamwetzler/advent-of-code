import pprint
from dataclasses import dataclass
from pathlib import Path

BOARD_WIDTH = 5
BOARD_HEIGHT = 5


@dataclass
class Number:
    number: int
    marked: bool = False

    def __init__(self, number: str):
        self.number = int(number)

    def __repr__(self) -> str:
        return f"{self.number}{'*' if self.marked else ''}"


@dataclass
class Board:
    numbers: list[list[Number]]

    def __repr__(self) -> str:
        return pprint.pformat(self.numbers)

    def update(self, drawn: int) -> None:
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


def parse_input() -> tuple:
    puzzle_input = Path("2021/04/input.txt").read_text()
    numbers, *boards_str = puzzle_input.split("\n" * 2)
    drawn_numbers = [int(number) for number in numbers.split(",")]

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

    return drawn_numbers, boards


def part_1() -> int:
    drawn_numbers, boards = parse_input()
    for draw in drawn_numbers:
        for board in boards:
            board.update(draw)
            if board.is_winner:
                return board.score * draw


def part_2() -> int:
    drawn_numbers, boards = parse_input()
    board_scores = []
    for draw in drawn_numbers:
        for board in boards:
            if not board.is_winner:
                board.update(draw)
                if board.is_winner:
                    board_scores.append(board.score * draw)

    return board_scores[-1]


if __name__ == "__main__":
    print("Part 1:", part_1())
    print("Part 2:", part_2())
