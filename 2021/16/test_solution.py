from solution import BITS, part_1, part_2, hex_to_bin, bin_to_int

test_input_1 = "D2FE28"


def test_hex_to_bin():
    assert hex_to_bin("D2FE28") == "110100101111111000101000"
    assert (
        hex_to_bin("38006F45291200")
        == "00111000000000000110111101000101001010010001001000000000"
    )


def test_bin_to_int():
    assert bin_to_int("001") == 1
    assert bin_to_int("00000000011") == 3
    assert bin_to_int("000000000011011") == 27


def test_literal_value_packet():
    bits = BITS("D2FE28")
    assert bits.version == 6
    assert bits.type == 4
    assert bits.value == 2021


def test_operator_packet():
    bits = BITS("38006F45291200")
    assert bits.version == 1
    assert bits.type == 6
    assert bits.length_type_id == 0
    assert bits.total_length == 27
    # assert bits.


# def test_part_1():
#     assert part_1()


# def test_part_2():
#     assert part_2()
