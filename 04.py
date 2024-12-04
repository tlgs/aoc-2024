import itertools
import sys


def parse_input(puzzle_input):
    grid = {}
    for y, line in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(line):
            grid[complex(x, y)] = c

    return (grid,)


def part_one(grid):
    transitions = dict(itertools.pairwise("XMAS"))
    deltas = [-1 - 1j, -1j, 1 - 1j, -1, 1, -1 + 1j, 1j, 1 + 1j]

    total = 0
    todo = [(t, d) for t, c in grid.items() for d in deltas if c == "X"]
    while todo:
        t, d = todo.pop()

        v = grid[t]
        if v == "S":
            total += 1
        elif grid.get(t + d) == transitions[v]:
            todo.append((t + d, d))

    return total


def part_two(grid):
    deltas = [-1 - 1j, 1 - 1j, -1 + 1j, 1 + 1j]

    total = 0
    for t in [t for t, c in grid.items() if c == "A"]:
        a, b, c, d = [grid.get(t + d) for d in deltas]
        if any(v is None or v == "X" for v in (a, b, c, d)):
            continue

        fst = (a == "M" and d == "S") or (a == "S" and d == "M")
        snd = (b == "M" and c == "S") or (b == "S" and c == "M")
        total += fst and snd

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
