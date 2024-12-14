import itertools
import math
import sys
from enum import Enum


class Operator(Enum):
    ADD = 1
    MULTIPLY = 2
    CONCATENATE = 3


def parse_input(puzzle_input):
    equations = []
    for line in puzzle_input.splitlines():
        raw_target, rest = line.split(":", maxsplit=1)
        values = list(map(int, rest.split()))

        equations.append((int(raw_target), values))

    return (equations,)


def calculate(values, operators):
    result, *remaining = values
    for value, operator in zip(remaining, operators):
        match operator:
            case Operator.ADD:
                result += value
            case Operator.MULTIPLY:
                result *= value
            case Operator.CONCATENATE:
                n = int(math.log10(value)) + 1
                result = result * 10**n + value

    return result


def run_calibration(equations, valid_operators):
    total = 0
    for target, values in equations:
        for operators in itertools.product(valid_operators, repeat=len(values) - 1):
            if target == calculate(values, operators):
                total += target
                break

    return total


def part_one(equations):
    return run_calibration(equations, [Operator.ADD, Operator.MULTIPLY])


def part_two(equations):
    return run_calibration(equations, list(Operator))


class Test:
    example = """\
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""

    def test_one(self):
        assert part_one(*parse_input(self.example)) == 3749

    def test_two(self):
        assert part_two(*parse_input(self.example)) == 11387


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    sys.exit(main())
