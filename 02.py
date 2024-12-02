import sys
from itertools import chain, combinations, pairwise


def parse_input(puzzle_input):
    reports = []
    for line in puzzle_input.splitlines():
        levels = list(map(int, line.split()))
        reports.append(levels)

    return (reports,)


def is_safe(report):
    diffs = [b - a for a, b in pairwise(report)]
    return (all(v > 0 for v in diffs) or all(v < 0 for v in diffs)) and all(
        1 <= abs(v) <= 3 for v in diffs
    )


def part_one(reports):
    return sum(map(is_safe, reports))


def part_two(reports):
    safe = 0
    for report in reports:
        n = len(report)
        for attempt in chain([report], combinations(report, n - 1)):
            if is_safe(attempt):
                safe += 1
                break

    return safe


class Test:
    example = """\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

    def test_one(self):
        assert part_one(*parse_input(self.example)) == 2

    def test_two(self):
        assert part_two(*parse_input(self.example)) == 4


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    sys.exit(main())
