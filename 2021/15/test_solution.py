from solution import part_1, part_2

test_input_1 = """
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
""".strip()


def test_part_1():
    assert part_1(test_input_1) == 40


def test_part_2():
    assert part_2(test_input_1) == 315
