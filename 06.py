import sys


def parse_input(puzzle_input):
    obstacles, guard = set(), None
    for y, line in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(line):
            match c:
                case ".":
                    pass
                case "#":
                    obstacles.add(complex(x, y))
                case "^":
                    guard = complex(x, y)

    return (x + 1, y + 1), obstacles, guard


def part_one(dims, obstacles, guard):
    pos, d, seen = guard, -1j, set()
    while -1 < pos.real < dims[0] and -1 < pos.imag < dims[1]:
        seen.add(pos)

        if (nxt := pos + d) in obstacles:
            d *= 1j
        else:
            pos = nxt

    return len(seen)


def part_two(dims, obstacles, guard):
    pos, d, candidates = guard, -1j, {}
    while -1 < pos.real < dims[0] and -1 < pos.imag < dims[1]:
        if pos not in candidates:
            candidates[pos] = (pos - d, d)

        if (nxt := pos + d) in obstacles:
            d *= 1j
        else:
            pos = nxt

    candidates.pop(guard)

    total = 0
    for tmp, (pos, d) in candidates.items():
        obstacles.add(tmp)

        seen = set()
        while -1 < pos.real < dims[0] and -1 < pos.imag < dims[1]:
            seen.add((pos, d))

            nxt = pos + d
            if (nxt, d) in seen:
                total += 1
                break
            elif nxt in obstacles:
                d *= 1j
            else:
                pos = nxt

        obstacles.remove(tmp)

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
