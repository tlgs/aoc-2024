import math
import sys
from collections import Counter
from functools import cache


def parse_input(puzzle_input):
    stones = [int(x) for x in puzzle_input.split()]
    return (stones,)


@cache
def nxt(stone):
    if stone == 0:
        return (1,)

    digits = int(math.log10(stone)) + 1
    q, odd = divmod(digits, 2)
    if not odd:
        return divmod(stone, 10**q)

    return (stone * 2024,)


def part_one(stones, blink=25):
    counts = Counter(stones)
    for _ in range(blink):
        tmp = Counter()
        for value, n in counts.items():
            for next_value in nxt(value):
                tmp[next_value] += n

        counts = tmp

    return counts.total()


def part_two(stones, blink=75):
    return part_one(stones, blink)


class Test:
    example = """\
125 17
"""

    def test_one(self):
        assert part_one(*parse_input(self.example), 6) == 22
        assert part_one(*parse_input(self.example), 25) == 55312


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    sys.exit(main())
