# https://adventofcode.com/2022/day/11

class Monkey:

    def __init__(self,
        number: int,
        true_monkey: int,
        false_monkey: int,
        items: list = [],
        operation = lambda n: n,
        divisible_by:int = 1) -> None:

        self.number = number
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.items = items
        self.operation = operation
        self.divisible_by = divisible_by
        self.items_inspected = 0

    def take_turn(self, monkey_list):
        self.inspect_items()
        self.throw_items(monkey_list)

    def take_turn_part2(self, monkey_list):
        self.inspect_items(useRelief=False)
        self.throw_items(monkey_list)

    def inspect_item(self, item):
        self.items_inspected += 1
        return self.operation(item)//3
    
    def inspect_item_no_relief(self, item):
        self.items_inspected += 1
        return self.operation(item) % (13*2*7*17*5*11*3*19)

    def inspect_items(self, useRelief = True):
        for i in range(len(self.items)):
            if useRelief:
                self.items[i] = self.inspect_item(self.items[i])
            else:
                self.items[i] = self.inspect_item_no_relief(self.items[i])

    def throw_item(self, item):
        if item % self.divisible_by == 0:
            return self.true_monkey
        
        return self.false_monkey

    def throw_items(self, monkey_list):
        for item in self.items:
            pass_to_monkey = self.throw_item(item)
            monkey_list[pass_to_monkey].items.append(item)

        self.items = []

    def toString(self):
        str = "Monkey{}<items: {}, items_inspected: {}>"
        return str.format(self.number, self.items, self.items_inspected)

monkeys1 = [
    Monkey(0, 1, 7, [84,72,58,51], lambda old: old*3, 13),
    Monkey(1, 7, 5, [88,58,58], lambda old: old+8, 2),
    Monkey(2, 3, 4, [93,82,71,77,83,53,71,89], lambda old: old*old, 7),
    Monkey(3, 4, 6, [81,68,65,81,73,77,96], lambda old: old+2, 17),
    Monkey(4, 6, 0, [75,80,50,73,88], lambda old: old+3, 5),
    Monkey(5, 2, 3, [59,72,99,87,91,81], lambda old: old*17, 11),
    Monkey(6, 1, 0, [86,69], lambda old: old+6, 3),
    Monkey(7, 2, 5, [91], lambda old: old+1, 19)
]

monkeys2 = [
    Monkey(0, 1, 7, [84,72,58,51], lambda old: old*3, 13),
    Monkey(1, 7, 5, [88,58,58], lambda old: old+8, 2),
    Monkey(2, 3, 4, [93,82,71,77,83,53,71,89], lambda old: old*old, 7),
    Monkey(3, 4, 6, [81,68,65,81,73,77,96], lambda old: old+2, 17),
    Monkey(4, 6, 0, [75,80,50,73,88], lambda old: old+3, 5),
    Monkey(5, 2, 3, [59,72,99,87,91,81], lambda old: old*17, 11),
    Monkey(6, 1, 0, [86,69], lambda old: old+6, 3),
    Monkey(7, 2, 5, [91], lambda old: old+1, 19)
]

def getAnswer(monkeys, rounds, part = 1):
    for i in range(rounds):
        for monkey in monkeys:
            if part == 1:
                monkey.take_turn(monkeys)
            elif part == 2:
                monkey.take_turn_part2(monkeys)

    monkeys.sort(key=lambda m: m.items_inspected, reverse=True)

    return monkeys[0].items_inspected * monkeys[1].items_inspected

print('part1:', getAnswer(monkeys1, 20, part=1))
print('part2:', getAnswer(monkeys2, 10000, part=2))