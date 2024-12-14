import itertools
import math
import re
import sys


def parse_input(puzzle_input):
    robots = []

    pat = re.compile(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)")
    for line in puzzle_input.splitlines():
        match = pat.fullmatch(line)
        px, py, vx, vy = map(int, match.groups())

        robots.append((px, py, vx, vy))

    return (robots,)


def part_one(robots, dims=(101, 103)):
    mx, my = dims[0] // 2, dims[1] // 2

    quadrants = [0] * 4
    idx = {(True, False): 0, (True, True): 1, (False, True): 2, (False, False): 3}
    for robot in robots:
        px, py, vx, vy = robot
        x = (px + 100 * vx) % dims[0]
        y = (py + 100 * vy) % dims[1]

        if x == mx or y == my:
            continue

        quadrants[idx[x > mx, y > mx]] += 1

    return math.prod(quadrants)


def part_two(robots, dims=(101, 103)):
    for seconds in itertools.count(start=1):
        grid = {}
        for i, robot in enumerate(robots):
            px, py = (robot[0] + robot[2]) % dims[0], (robot[1] + robot[3]) % dims[1]
            robots[i] = (px, py, robot[2], robot[3])

            grid[px, py] = "#"

        slope = 0
        for px, py, _, _ in robots:
            slope += {(px - 1, py - 1), (px + 1, py + 1)} <= grid.keys() or {
                (px + 1, py - 1),
                (px - 1, py + 1),
            } <= grid.keys()

        if slope > len(robots) / 4:
            return seconds


class Test:
    example = """\
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
"""

    def test_one(self):
        assert part_one(*parse_input(self.example), (11, 7)) == 12


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    sys.exit(main())
