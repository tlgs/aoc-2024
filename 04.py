import sys


def parse_input(puzzle_input):
    grid = {}
    for y, line in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(line):
            grid[x + y * 1j] = c

    return (grid,)


def part_one(grid):
    target = tuple("XMAS")
    deltas = [-1 - 1j, -1j, 1 - 1j, -1, 1, -1 + 1j, 1j, 1 + 1j]

    candidates = [
        tuple(grid.get(v + d * i) for i in range(4)) for v in grid for d in deltas
    ]
    return candidates.count(target)


def part_two(grid):
    targets = {tuple("SAM"), tuple("MAS")}
    deltas = [-1 - 1j, 0, 1 + 1j]

    total = 0
    for v in grid:
        back = tuple(grid.get(v + d) for d in deltas)
        fwd = tuple(grid.get(v + d.conjugate()) for d in deltas)
        total += {back, fwd} <= targets

    return total


class Test:
    example = """\
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

    def test_one(self):
        assert part_one(*parse_input(self.example)) == 18

    def test_two(self):
        assert part_two(*parse_input(self.example)) == 9


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    sys.exit(main())
