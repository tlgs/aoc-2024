import itertools
import sys


def parse_input(puzzle_input):
    blocks = []
    curr, file = 0, True
    for n in map(int, puzzle_input.strip()):
        if file:
            blocks.append((curr, n))

        curr, file = curr + n, not file

    return (blocks,)


def part_one(blocks):
    blocks = blocks[:]

    slots = []
    for a, b in itertools.pairwise(blocks):
        start, end = sum(a), b[0]
        slots.append((start, end))

    i, j, s = 0, len(blocks) - 1, 0
    rearranged = {blocks[i]: i}
    while i < j:
        start, end = slots[s]
        while (free := end - start) > 0:
            sz = blocks[j][1]
            d = free - sz
            if d >= 0:
                rearranged[start, start + sz] = j
                j -= 1
                start += sz
            else:
                rearranged[start, start + free] = j
                start += free
                blocks[j] = (blocks[j][0], -d)

        s += 1
        i += 1
        rearranged[blocks[i][0], sum(blocks[i])] = i

    total = 0
    for (a, b), id_ in rearranged.items():
        total += id_ * sum(range(a, b))

    return total


def part_two(blocks):
    slots = []
    for a, b in itertools.pairwise(blocks):
        start, end = sum(a), b[0]
        slots.append((start, end))

    rearranged = {(block[0], sum(block)): i for i, block in enumerate(blocks)}
    for i in range(len(blocks) - 1, -1, -1):
        x, sz = blocks[i]
        s = 0
        while s < len(slots):
            start, end = slots[s]
            if start > x:
                break
            d = (end - start) - sz
            if d >= 0:
                rearranged[start, start + sz] = i
                slots[s] = (start + sz, end)

                del rearranged[blocks[i][0], sum(blocks[i])]
                break

            s += 1

    total = 0
    for (a, b), id_ in rearranged.items():
        total += id_ * sum(range(a, b))

    return total


class Test:
    example = """\
2333133121414131402
"""

    def test_one(self):
        assert part_one(*parse_input(self.example)) == 1928

    def test_two(self):
        assert part_two(*parse_input(self.example)) == 2858


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))

    # 8509897721111 high


if __name__ == "__main__":
    sys.exit(main())
