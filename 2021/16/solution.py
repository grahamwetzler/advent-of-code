from dataclasses import dataclass
from math import prod
from pathlib import Path


@dataclass
class Packet:
    version: int
    type_id: int
    value: int
    sub_packets: list


def hex_to_bin(hex: str) -> str:
    return "".join([format(int(h, 16), "b").zfill(4) for h in hex])


def bin_to_int(bin: str) -> int:
    return int(bin, 2)


def decode_literal_value(packet: str, index: int) -> tuple[int, int]:
    value = ""
    while True:
        control = packet[index] == "0"
        value += packet[index + 1 : index + 5]
        index += 5
        if control:
            return bin_to_int(value), index


def decode_packets_by_length(packet: str, index: int) -> tuple[list, int]:
    sub_packets = []
    length_of_sub_packets = bin_to_int(packet[index : index + 15])
    index += 15
    bits = 0
    while bits < length_of_sub_packets:
        sub_packet, new_index = parse(packet, index)
        sub_packets.append(sub_packet)
        bits += new_index - index
        index = new_index

    return sub_packets, index


def decode_packets_by_number(packet: str, index: int) -> tuple[list, int]:
    sub_packets = []
    number_sub_packets = bin_to_int(packet[index : index + 11])
    index += 11
    for _ in range(number_sub_packets):
        sub_packet, index = parse(packet, index)
        sub_packets.append(sub_packet)

    return sub_packets, index


def parse(packet: Packet, index: int = 0) -> tuple[Packet, int]:
    version = bin_to_int(packet[index : index + 3])
    type_id = bin_to_int(packet[index + 3 : index + 6])
    index += 6
    if type_id == 4:
        value, index = decode_literal_value(packet, index)
        return Packet(version, type_id, value, []), index

    length_type_id = bin_to_int(packet[index])
    index += 1

    if length_type_id == 0:
        sub_packets, index = decode_packets_by_length(packet, index)
    else:
        sub_packets, index = decode_packets_by_number(packet, index)

    value = calculate_packet_value(type_id, sub_packets)

    return Packet(version, type_id, value, sub_packets), index


def sum_versions(packet: Packet) -> int:
    total = packet.version
    for sub_packet in packet.sub_packets:
        total += sum_versions(sub_packet)

    return total


def calculate_packet_value(type_id: int, sub_packets: list) -> int:
    values = [packet.value for packet in sub_packets]
    if type_id in [0, 1, 2, 3]:
        if type_id == 0:
            value = sum(values)
        elif type_id == 1:
            value = prod(values)
        elif type_id == 2:
            value = min(values)
        elif type_id == 3:
            value = max(values)
    else:
        first, second = values
        if type_id == 5:
            value = 1 if first > second else 0
        elif type_id == 6:
            value = 1 if first < second else 0
        else:
            value = 1 if first == second else 0

    return value


def part_1(packet: str) -> int:
    packet_as_binary = hex_to_bin(packet)
    outer_packet, _ = parse(packet_as_binary)

    return sum_versions(outer_packet)


def part_2(packet: str) -> int:
    packet_as_binary = hex_to_bin(packet)
    outer_packet, _ = parse(packet_as_binary)

    return outer_packet.value


if __name__ == "__main__":
    puzzle_input = Path("2021/16/input.txt").read_text().strip()
    print("Part 1:", part_1(puzzle_input))
    print("Part 2:", part_2(puzzle_input))
