import re

class MonkeyFactory:
    def __init__(self):
        self.provisioned_monkeys = []

    def provision_monkey(self, interest_function, yeet_params, *starting_items):
        monkey = Monkey(*starting_items)
        monkey.inspect = self.generate_inspect_function(interest_function).__get__(monkey)
        monkey.yeet = self.generate_yeet_function(*yeet_params).__get__(monkey)
        self.provisioned_monkeys.append(monkey)
    
    def generate_inspect_function(factory, operation):
        def inspect(self, item):
            self.inspection_count += 1
            shiny_interest_level = eval(operation.format(item=item))
            # item = shiny_interest_level // 3
            item = shiny_interest_level
            self.yeet(item)
            return item
        return inspect
    
    def generate_yeet_function(factory, divisor, on_true, on_false):
        def yeet(self, item):
            target = on_true if not item % divisor else on_false
            factory.provisioned_monkeys[target].items.append(item)
        return yeet
                

class Monkey:
    def __init__(self, *starting_items):
        self.items = list(starting_items)
        self.inspection_count = 0

    def take_turn(self):
        for item in self.items:
            self.inspect(item)
        self.items.clear()
    
    def yeet(self, item):
        pass

    def inspect(self, item):
        raise NotImplementedError('Monkey object should have inspect method added by builder')


def solve(input_file):
    with open(input_file, 'r') as file:
        input_data = file.readlines()
    
    monkey_blueprints = [input_data[split - 7: split] for split in range(7, len(input_data) + 2, 7)]
    monkey_factory = MonkeyFactory()
    
    for monkey_blueprint in monkey_blueprints:
        starting_items = [int(item) for item in re.findall(r'\d+', monkey_blueprint[1])]
        interest_operation = re.match(r'\s+Operation: new = (.+)\n', monkey_blueprint[2]).groups()[0]
        interest_operation = interest_operation.replace('old', '{item}')
        yeet_params = [int(re.match(r'\D+(\d+)\D*', line).groups()[0]) for line in monkey_blueprint[3:6]]

        monkey_factory.provision_monkey(interest_operation, yeet_params, *starting_items)

    for _ in range(10000):
        if not _ % 100:
            print(_)
        for monkey in monkey_factory.provisioned_monkeys:
            monkey.take_turn()
        # print(f'ROUND {_}')
        # for monkey_num, monkey in enumerate(monkey_factory.provisioned_monkeys):
        #     print(monkey_num, monkey.items)
    inspection_counts = [monkey.inspection_count for monkey in monkey_factory.provisioned_monkeys]
    inspection_counts.sort(reverse=True)
    return inspection_counts[0] * inspection_counts[1]


print(solve('advent_of_code_2022/day_11/test.txt'))
print(solve('advent_of_code_2022/day_11/input.txt'))