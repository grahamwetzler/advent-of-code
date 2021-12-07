from collections import Counter
from pathlib import Path


class Submarine:
    def __init__(self):
        self.binary_input = Path("2021/03/input.txt").read_text().split()

    def bit_list_to_int(self, bits: list):
        return int("".join(bits), 2)

    def count_bits(self, rows: list) -> list[Counter]:
        bits = len(rows[0])
        counts = []
        for idx in range(bits):
            columns = [i[idx] for i in rows]
            counter = Counter(columns)
            counts.append(counter)

        return counts

    @property
    def power_consuption(self) -> int:
        counts = self.count_bits(self.binary_input)

        gamma = []
        epsilon = []
        for count in counts:
            (most_common, _), (least_common, _) = count.most_common()
            gamma.append(most_common)
            epsilon.append(least_common)

        return self.bit_list_to_int(gamma) * self.bit_list_to_int(epsilon)

    def calculate_life_support(self, type: str) -> int:
        readings = self.binary_input

        idx = 0
        while len(readings) > 1:
            counts = self.count_bits(readings)
            count = counts[idx]
            (most_common, high_count), (least_common, low_count) = count.most_common()
            if type == "oxygen":
                if high_count == low_count:
                    most_common = "1"
                readings = list(filter(lambda x: x[idx] == most_common, readings))
            elif type == "co2":
                if high_count == low_count:
                    least_common = "0"
                readings = list(filter(lambda x: x[idx] == least_common, readings))
            idx += 1

        return self.bit_list_to_int(readings)

    @property
    def oxygen_generator_rating(self) -> int:
        return self.calculate_life_support(type="oxygen")

    @property
    def co2_scrubber_rating(self) -> int:
        return self.calculate_life_support(type="co2")

    @property
    def life_support_rating(self):
        return self.oxygen_generator_rating * self.co2_scrubber_rating


if __name__ == "__main__":
    print("Part 1:", Submarine().power_consuption)
    print("Part 2:", Submarine().life_support_rating)
