import sys


def parse_input(puzzle_input):
    raw_warehouse, raw_moves = puzzle_input.split("\n\n")

    warehouse = {}
    for y, line in enumerate(raw_warehouse.splitlines()):
        for x, c in enumerate(line):
            warehouse[x, y] = c

    move_mapping = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}
    moves = [move_mapping[c] for line in raw_moves.splitlines() for c in line]

    return warehouse, moves


def part_one(warehouse, moves):
    warehouse = warehouse.copy()

    max_x, max_y = max(x for x, _ in warehouse), max(y for _, y in warehouse)
    (rx, ry), *_ = [k for k, v in warehouse.items() if v == "@"]

    for dx, dy in moves:
        x, y = rx, ry
        while 0 < x < max_x and 0 < y < max_y:
            x, y = x + dx, y + dy
            match warehouse[x, y]:
                case "#":
                    break
                case ".":
                    warehouse[x, y] = "O"
                    warehouse[rx, ry] = "."

                    rx, ry = rx + dx, ry + dy
                    warehouse[rx, ry] = "@"
                    break

    return sum(x + 100 * y for (x, y), c in warehouse.items() if c == "O")


def part_two(warehouse, moves):
    prev = warehouse.copy()

    warehouse = {}
    for (x, y), c in prev.items():
        match c:
            case "." | "#":
                warehouse[2 * x, y] = c
                warehouse[2 * x + 1, y] = c
            case "@":
                warehouse[2 * x, y] = c
                warehouse[2 * x + 1, y] = "."
            case "O":
                warehouse[2 * x, y] = "["
                warehouse[2 * x + 1, y] = "]"

    (rx, ry), *_ = [k for k, v in warehouse.items() if v == "@"]
    for dx, dy in moves:
        to_check, todo = [(rx, ry)], []
        while True:
            if any(warehouse[x, y] == "#" for x, y in to_check):
                break
            elif all(warehouse[x, y] == "." for x, y in to_check):
                while todo:
                    x, y = todo.pop()
                    warehouse[x + dx, y + dy] = warehouse[x, y]
                    warehouse[x, y] = "."

                warehouse[rx, ry] = "."

                rx, ry = rx + dx, ry + dy
                warehouse[rx, ry] = "@"
                break

            if dy == 0:
                assert len(to_check) == 1

                x, y = to_check.pop()

                todo.append((x, y))
                to_check.append((x + dx, y))

            else:
                nxt = set()
                while to_check:
                    x, y = to_check.pop()
                    cx, cy = x + dx, y + dy
                    if warehouse[cx, cy] == ".":
                        todo.append((x, y))
                        continue

                    if warehouse[cx, cy] == "[":
                        assert warehouse[cx + 1, cy] == "]"

                        todo.append((x, y))

                        nxt.add((cx, cy))
                        nxt.add((cx + 1, cy))

                    elif warehouse[cx, cy] == "]":
                        assert warehouse[cx - 1, cy] == "["

                        todo.append((x, y))

                        nxt.add((cx, cy))
                        nxt.add((cx - 1, cy))

                    elif warehouse[cx, cy] == "#":
                        nxt.add((cx, cy))

                to_check = list(nxt)

    return sum(x + 100 * y for (x, y), c in warehouse.items() if c == "[")


class Test:
    example1 = """\
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<
"""

    example2 = """\
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
"""

    example3 = """\
#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^
"""

    def test_one(self):
        assert part_one(*parse_input(self.example1)) == 2028
        assert part_one(*parse_input(self.example2)) == 10092

    def test_two(self):
        assert part_two(*parse_input(self.example2)) == 9021
        assert part_two(*parse_input(self.example3)) == 618


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    sys.exit(main())
