import collections
import functools
import math
import sys


def parse_input(puzzle_input):
    stones = [int(x) for x in puzzle_input.split()]
    return (stones,)


@functools.cache
def nxt(stone):
    if stone == 0:
        return (1,)

    digits = int(math.log10(stone)) + 1
    if digits % 2 == 0:
        return divmod(stone, 10 ** (digits / 2))

    return (stone * 2024,)


def part_one(stones, blink=25):
    counts = collections.Counter(stones)
    for _ in range(blink):
        new = collections.Counter()
        for k, v in counts.items():
            for w in nxt(k):
                new[w] += v

        counts = new

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
