from pathlib import Path


def hex_to_bin(hex: str) -> str:
    return "".join([format(int(h, 16), "b").zfill(4) for h in hex])


def bin_to_int(bin: str) -> int:
    return int(bin, 2)


def decode_value(body) -> int:
    value = ""
    for group in range(0, len(body) + 1, 5):
        bits = body[group : group + 5]
        control = bits[0]
        value += bits[1:]
        if control == "0":
            return bin_to_int(value)


class BITS:
    def __init__(self, transmission: str) -> None:
        self.version_sum = 0
        self._parse(hex_to_bin(transmission))

    def _parse(self, packet: str) -> None:
        version = bin_to_int(packet[:3])
        self.version_sum += version
        packet_type = bin_to_int(packet[3:6])
        if packet_type == 4:
            body = packet[6:]
        else:
            length_type_id = bin_to_int(packet[6])
            if length_type_id == 0:
                total_length = bin_to_int(packet[7:22])
                body = packet[22 : 22 + total_length]
                bits = 0
                while bits < total_length:
                    ...
            else:
                number_sub_packets = bin_to_int(packet[7:18])
                body = packet[19:]


def part_1(puzzle_input: str) -> int:
    ...


def part_2(puzzle_input: str) -> int:
    ...


if __name__ == "__main__":
    puzzle_input = Path("2021/16/input.txt").read_text().strip()
    bits = BITS(puzzle_input)
    print(bits.body)
