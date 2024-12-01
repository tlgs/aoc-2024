import sys
from collections import Counter


def parse_input(puzzle_input):
    left, right = [], []
    for line in puzzle_input.splitlines():
        fst, snd = map(int, line.split())
        left.append(fst)
        right.append(snd)

    return left, right


def part_one(left, right):
    return sum(abs(a - b) for a, b in zip(sorted(left), sorted(right)))


def part_two(left, right):
    counts = Counter(right)
    return sum(v * counts[v] for v in left)


class Test:
    example = """\
3   4
4   3
2   5
1   3
3   9
3   3
"""

    def test_one(self):
        assert part_one(*parse_input(self.example)) == 11

    def test_two(self):
        assert part_two(*parse_input(self.example)) == 31


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    sys.exit(main())
