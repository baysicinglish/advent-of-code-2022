import re
import math

class Barrel:
    monkeys = []
    lowest_common_multiple = 0

    def __new__(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Barrel, cls).__new__(cls)
        return cls._instance
    
    @classmethod
    def set_lowest_common_multiple(cls):
        cls.lowest_common_multiple = math.lcm(*[monkey.yeet_params[0] for monkey in cls.monkeys])


class Monkey:
    def __init__(self, interest_calculation, yeet_params, *starting_items):
        self.items = list(starting_items)
        self.inspection_count = 0
        self.interest_calculation = interest_calculation
        self.yeet_params = yeet_params

        self.barrel = Barrel()
        self.barrel.monkeys.append(self)

    def take_turn(self):
        for item in self.items:
            self.inspect(item)
        self.items.clear()
    
    def yeet(self, item):
        divisor, on_true, on_false = self.yeet_params
        target = on_true if not item % divisor else on_false
        self.barrel.monkeys[target].items.append(item)

    def inspect(self, item):
        self.inspection_count += 1
        shiny_interest_level = self._calculate_interest_level(self.interest_calculation, item)
        # item = shiny_interest_level // 3
        item = shiny_interest_level % self.barrel.lowest_common_multiple
        self.yeet(item)
        return item
    
    def _calculate_interest_level(self, equation, item):
        operations = {'+': sum, '*': math.prod}
        num1, operator, num2 = equation.split()
        num1 = int(num1) if num1.isdigit() else item
        num2 = int(num2) if num2.isdigit() else item
        return operations[operator]((num1, num2))


def solve(input_file):
    with open(input_file, 'r') as file:
        input_data = file.readlines()
    
    monkey_blueprints = [input_data[split - 7: split] for split in range(7, len(input_data) + 2, 7)]
    
    for monkey_blueprint in monkey_blueprints:
        starting_items = [int(item) for item in re.findall(r'\d+', monkey_blueprint[1])]
        interest_operation = re.match(r'\s+Operation: new = (.+)\n', monkey_blueprint[2]).groups()[0]
        interest_operation = interest_operation.replace('old', '{item}')
        yeet_params = [int(re.match(r'\D+(\d+)\D*', line).groups()[0]) for line in monkey_blueprint[3:6]]

        Monkey(interest_operation, yeet_params, *starting_items)

    barrel = Barrel()
    barrel.set_lowest_common_multiple()

    for _ in range(10000):
        for monkey in barrel.monkeys:
            monkey.take_turn()

    inspection_counts = [monkey.inspection_count for monkey in barrel.monkeys]
    inspection_counts.sort(reverse=True)
    return inspection_counts[0] * inspection_counts[1]


# print(solve('advent_of_code_2022/day_11/test.txt'))
print(solve('advent_of_code_2022/day_11/input.txt'))