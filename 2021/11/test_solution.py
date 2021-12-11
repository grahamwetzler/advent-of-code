from solution import part_1, part_2

test_input = """
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
"""


def test_part_1():
    assert part_1(test_input) == 1656


def test_part_2():
    assert part_2(test_input) == 195
