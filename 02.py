import itertools
import sys


def parse_input(puzzle_input):
    reports = []
    for line in puzzle_input.splitlines():
        levels = list(map(int, line.split()))
        reports.append(levels)

    return (reports,)


def is_safe(report):
    sign = 1 if report[1] > report[0] else -1
    for a, b in itertools.pairwise(report):
        if not (1 <= sign * (b - a) <= 3):
            return False
    return True


def part_one(reports):
    return sum(map(is_safe, reports))


def part_two(reports):
    safe = 0
    for report in reports:
        if is_safe(report):
            safe += 1
            continue

        for i, _ in enumerate(report):
            if is_safe(report[:i] + report[i + 1 :]):
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
