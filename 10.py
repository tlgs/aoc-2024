import sys


def parse_input(puzzle_input):
    grid, starts = {}, []
    for y, line in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(map(int, line)):
            if c == 0:
                starts.append((x, y))

            grid[x, y] = c

    return grid, starts


def neighbors(x, y):
    yield x, y - 1
    yield x - 1, y
    yield x + 1, y
    yield x, y + 1


def part_one(grid, starts):
    total = 0
    for start in starts:
        todo, seen = [start], set()
        while todo:
            pos = todo.pop()
            seen.add(pos)

            if (v := grid[pos]) == 9:
                total += 1
                continue

            for nxt in neighbors(*pos):
                if nxt not in seen and grid.get(nxt) == v + 1:
                    todo.append(nxt)

    return total


def part_two(grid, starts):
    total = 0
    for start in starts:
        todo = [start]
        while todo:
            pos = todo.pop()
            if (v := grid[pos]) == 9:
                total += 1
                continue

            for nxt in neighbors(*pos):
                if grid.get(nxt) == v + 1:
                    todo.append(nxt)

    return total


class Test:
    example = """\
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""

    def test_one(self):
        assert part_one(*parse_input(self.example)) == 36

    def test_two(self):
        assert part_two(*parse_input(self.example)) == 81


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    sys.exit(main())
