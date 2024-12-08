import collections
import itertools
import sys


def parse_input(puzzle_input):
    antennas = collections.defaultdict(list)
    for y, line in enumerate(puzzle_input.splitlines()):
        for x, c in enumerate(line):
            if c == ".":
                continue

            antennas[c].append(complex(x, y))

    return (x + 1, y + 1), antennas


def part_one(dims, antennas):
    antinodes = set()
    for paired_antennas in antennas.values():
        for a, b in itertools.combinations(paired_antennas, 2):
            diff = b - a
            antinodes |= {
                node
                for node in [a - diff, b + diff]
                if node.real in range(dims[0]) and node.imag in range(dims[1])
            }

    return len(antinodes)


def part_two(dims, antennas):
    antinodes = set()
    for paired_antennas in antennas.values():
        for a, b in itertools.combinations(paired_antennas, 2):
            antinodes |= {a, b}

            diff = b - a
            for i in itertools.count(1):
                nxt = b + i * diff
                if nxt.real not in range(dims[0]) or nxt.imag not in range(dims[1]):
                    break
                antinodes.add(nxt)

            for i in itertools.count(1):
                nxt = a - i * diff
                if nxt.real not in range(dims[0]) or nxt.imag not in range(dims[1]):
                    break
                antinodes.add(nxt)

    return len(antinodes)


class Test:
    example = """\
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""

    def test_one(self):
        assert part_one(*parse_input(self.example)) == 14

    def test_two(self):
        assert part_two(*parse_input(self.example)) == 34


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    sys.exit(main())
