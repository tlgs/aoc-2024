import sys


def parse_input(puzzle_input):
    fst, snd = puzzle_input.split("\n\n")

    rules = []
    for line in fst.splitlines():
        rule = [int(v) for v in line.split("|")]
        rules.append(rule)

    correct, incorrect = [], []
    for line in snd.splitlines():
        update = [int(v) for v in line.split(",")]
        for left, right in rules:
            if {left, right} <= set(update) and (
                update.index(left) > update.index(right)
            ):
                incorrect.append(update)
                break
        else:
            correct.append(update)

    return rules, correct, incorrect


def part_one(rules, correct, incorrect):
    return sum(update[len(update) // 2] for update in correct)


def part_two(rules, correct, incorrect):
    total = 0
    for update in incorrect:
        relevant_rules = list(filter(lambda t: set(t) <= set(update), rules))
        while True:
            done = True
            for left, right in relevant_rules:
                a, b = update.index(left), update.index(right)
                if a > b:
                    update[a], update[b] = update[b], update[a]
                    done = False

            if done:
                total += update[len(update) // 2]
                break

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
