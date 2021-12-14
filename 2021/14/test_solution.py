from solution import day_14

test_input_1 = """
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
""".strip()


def test_part_1():
    assert day_14(test_input_1, 10) == 1588


def test_part_2():
    assert day_14(test_input_1, 40) == 2188189693529
