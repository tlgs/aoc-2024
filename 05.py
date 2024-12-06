import sys


def parse_input(puzzle_input):
    fst, snd = puzzle_input.split("\n\n")

    rules = []
    for line in fst.splitlines():
        rule = tuple([int(v) for v in line.split("|")])
        rules.append(rule)

    updates = []
    for line in snd.splitlines():
        update = tuple([int(v) for v in line.split(",")])
        updates.append(update)

    return rules, updates


def part_one(rules, updates):
    total = 0
    for update in updates:
        for left, right in rules:
            try:
                if update.index(left) > update.index(right):
                    break
            except ValueError:
                pass

        else:
            total += update[len(update) // 2]

    return total


def part_two(rules, updates):
    to_fix = []
    for update in updates:
        flag, relevant = False, []
        for left, right in rules:
            try:
                if update.index(left) > update.index(right):
                    flag = True

                relevant.append((left, right))
            except ValueError:
                pass

        if flag:
            to_fix.append((list(update), relevant))

    total = 0
    for update, update_rules in to_fix:
        while True:
            done = True
            for left, right in update_rules:
                a, b = update.index(left), update.index(right)
                if a > b:
                    update[a], update[b] = right, left
                    done = False

            if done:
                break

        total += update[len(update) // 2]

    return total


class Test:
    example = """\
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

    def test_one(self):
        assert part_one(*parse_input(self.example)) == 143

    def test_two(self):
        assert part_two(*parse_input(self.example)) == 123


def main():
    puzzle = parse_input(sys.stdin.read())

    print("part 1:", part_one(*puzzle))
    print("part 2:", part_two(*puzzle))


if __name__ == "__main__":
    sys.exit(main())
