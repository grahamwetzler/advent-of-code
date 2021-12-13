from solution import part_1

test_input_1 = """
start-A
start-b
A-c
A-b
b-d
A-end
b-end
"""

test_input_2 = """
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
"""


def test_part_1():
    assert part_1(test_input_1) == 10
    assert part_1(test_input_2) == 19
