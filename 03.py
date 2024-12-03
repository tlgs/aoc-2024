import re
import sys


def parse_input(puzzle_input):
    pat = r"mul\([1-9][0-9]{,2},[1-9][0-9]{,2}\)|do\(\)|don't\(\)"
    instructions = re.findall(pat, puzzle_input)
    return (instructions,)


def part_one(instructions):
    total = 0
    for instruction in instructions:
        if not instruction.startswith("mul"):
            continue

        a, b = map(int, instruction[4:-1].split(","))
        total += a * b

    return total


def part_two(instructions):
    total, enabled = 0, True
    for instruction in instructions:
        match instruction[:3], enabled:
            case "do(", _:
                enabled = True
            case "don", _:
                enabled = False
            case "mul", True:
                a, b = map(int, instruction[4:-1].split(","))
                total += a * b

    return total


class Test:
    example1 = """\
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""
    example2 = """\
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
"""

    def test_one(self):
        assert part_one(*parse_input(self.example1)) == 161

    def test_two(self):
        assert part_two(*parse_input(self.example2)) == 48


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    sys.exit(main())
