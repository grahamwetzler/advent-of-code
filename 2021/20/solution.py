import itertools
from pathlib import Path

import numpy as np


class Image:
    def __init__(self, image: np.ndarray) -> None:
        self.image = image

    def __getitem__(self, coordinates: tuple[int]) -> str:
        y, x = coordinates
        n_rows, n_cols = self.image.shape

        # Middle
        if 0 < y < n_rows - 1 and 0 < x < n_cols - 1:
            array = self.image[y - 1 : y + 2, x - 1 : x + 2]
            return self._grid_to_bin(array)

        # Corners

        # Top Left
        elif y == 0 and x == 0:
            array = self.image[0:2, 0:2]
            array = np.row_stack([np.zeros(2, dtype="int8"), array])
            array = np.column_stack([np.zeros(3, dtype="int8"), array])
            self._expand_image("top")
            self._expand_image("left")
            return self._grid_to_bin(array)

        # Top Right
        elif y == 0 and x == n_cols - 1:
            array = self.image[: n_cols - 3, n_cols - 2 :]
            array = np.row_stack([np.zeros(2, dtype="int8"), array])
            array = np.column_stack([array, np.zeros(3, dtype="int8")])
            self._expand_image("top")
            self._expand_image("right")
            return self._grid_to_bin(array)

        # Bottom Left
        elif y == 0 and x == n_cols - 4:
            ...

        # Bottom Right
        elif y == n_rows - 1 and x == n_cols - 1:
            ...

        # Edges

        # Top
        elif y == 0:
            array = self.image[y : y + 2, x - 1 : x + 2]
            array = np.row_stack([np.zeros(3, dtype="int8"), array])
            self._expand_image("top")
            return self._grid_to_bin(array)

        # Bottom
        elif y == n_rows - 1:
            ...

        # Left
        elif x == 0:
            ...

        elif x - n_cols - 1:
            ...

    def _grid_to_bin(self, array: np.ndarray) -> str:
        return "".join([str(row) for col in array.tolist() for row in col])

    def _expand_image(self, side: str) -> None:
        n_rows, n_cols = self.image.shape
        new_col = np.zeros((n_rows, 1), dtype="int8")
        new_row = np.zeros(n_cols, dtype="int8")

        if side == "left":
            self.image = np.hstack([new_col, self.image])
        elif side == "right":
            self.image = np.hstack([self.image, new_col])
        elif side == "bottom":
            self.image = np.vstack([self.image, new_row])
        elif side == "top":
            self.image = np.vstack([new_row, self.image])


def parse(puzzle_input: str) -> tuple[str, Image]:
    algorithm, image = puzzle_input.split("\n\n")
    algorithm = "".join(["1" if i == "#" else "0" for i in list(algorithm)])
    image = Image(
        np.array(
            [
                [1 if pixel == "#" else 0 for pixel in list(row)]
                for row in image.splitlines()
            ],
            dtype="int8",
        )
    )
    return algorithm, image


def get_surrounding(image: np.ndarray, x: int, y: int) -> str:
    pixels = []
    for x, y in itertools.product([1, 0, -1], [1, 0, -1]):
        pixels.append(image[x, y])
    print(pixels)


def part_1():
    ...


def part_2():
    ...


if __name__ == "__main__":
    puzzle_input = Path("2021/20/input.txt").read_text()
    algorithm, image = parse(puzzle_input)
    print(image.image)
    print(image[0, 4])
    print(image.image)
    # get_surrounding(image, 2, 2)
