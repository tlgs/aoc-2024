import itertools
import sys


def parse_input(puzzle_input):
    lines = puzzle_input.splitlines()
    dims = len(lines[0]), len(lines)

    obstacles, guard = set(), None
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            match c:
                case ".":
                    pass
                case "#":
                    obstacles.add((x, y))
                case "^":
                    guard = (x, y)

    return dims, obstacles, guard


def part_one(dims, obstacles, guard):
    xmax, ymax = dims
    directions = itertools.cycle([(0, -1), (1, 0), (0, 1), (-1, 0)])

    seen = set()
    (x, y), curr = guard, next(directions)
    while -1 < x < xmax and -1 < y < ymax:
        seen.add((x, y))

        nxt = (x + curr[0], y + curr[1])
        if nxt in obstacles:
            curr = next(directions)
        else:
            x, y = nxt

    return len(seen)


def part_two(dims, obstacles, guard):
    xmax, ymax = dims
    directions = itertools.cycle([(0, -1), (1, 0), (0, 1), (-1, 0)])

    candidates = set()
    (x, y), curr = guard, next(directions)
    while -1 < x < xmax and -1 < y < ymax:
        candidates.add((x, y))

        nxt = (x + curr[0], y + curr[1])
        if nxt in obstacles:
            curr = next(directions)
        else:
            x, y = nxt

    total = 0
    for candidate in candidates - {guard}:
        x, y = guard
        while curr != (0, -1):
            curr = next(directions)

        obstacles.add(candidate)

        seen = set()
        while -1 < x < xmax and -1 < y < ymax:
            if (x, y, *curr) in seen:
                total += 1
                break

            seen.add((x, y, *curr))

            nxt = (x + curr[0], y + curr[1])
            if nxt in obstacles:
                curr = next(directions)
            else:
                x, y = nxt

        obstacles.remove(candidate)

    return total


class Test:
    example = """\
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

    def test_one(self):
        assert part_one(*parse_input(self.example)) == 41

    def test_two(self):
        assert part_two(*parse_input(self.example)) == 6


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    sys.exit(main())
