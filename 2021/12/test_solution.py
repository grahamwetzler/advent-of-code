from solution import part_1, part_2

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
kj-dc"""

test_input_3 = """
fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
"""


def test_part_1():
    assert part_1(test_input_1) == 10
    assert part_1(test_input_2) == 19


def test_part_2():
    assert part_2(test_input_2) == 103
    assert part_2(test_input_3) == 3509
