import math
import sys
from functools import cache


def parse_input(puzzle_input):
    stones = [int(x) for x in puzzle_input.split()]
    return (stones,)


@cache
def blink(v, n):
    if n == 0:
        return 1

    if v == 0:
        return blink(1, n - 1)

    digits = int(math.log10(v)) + 1
    q, odd = divmod(digits, 2)
    if not odd:
        left, right = divmod(v, 10**q)
        return blink(left, n - 1) + blink(right, n - 1)

    return blink(v * 2024, n - 1)


def part_one(stones, n=25):
    return sum(blink(stone, n) for stone in stones)


def part_two(stones, n=75):
    return sum(blink(stone, n) for stone in stones)


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
