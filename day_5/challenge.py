
def solve(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
        index = lines.index('\n')
        stack_info, instructions = lines[:index], lines[index + 1:]
        stacks = get_stacks(stack_info)
        stacks = apply_instructions(stacks, instructions)
        return ''.join([column.pop() for column in stacks])


def get_stacks(stack_info):
    stack_info.reverse()
    column_numbers = stack_info.pop(0).split()
    columns = [[] for _ in column_numbers]
    for row in stack_info:
        crates = [None if crate.isspace() else crate[1] for crate in row_to_columns(row)]
        for index, crate in enumerate(crates):
            if crate:
                columns[index].append(crate)
    return columns


def row_to_columns(row):
    while row:
        crate, row = row[:3], row[4:]
        yield crate


def apply_instructions(stacks, instructions):
    for instruction in instructions:
        count, from_, to = [int(word) for word in instruction.split() if word.isdigit()]
        # for _ in range(count):
            # stacks[to - 1].append(stacks[from_ - 1].pop())
        stacks[from_ - 1], selected_crates =  stacks[from_ - 1][:-count], stacks[from_ - 1][-count:]
        stacks[to - 1] += selected_crates
    return stacks


# assert solve('advent_of_code_2022/day_5/test.txt') == 'CMZ'
assert solve('advent_of_code_2022/day_5/test.txt') == 'MCD'
print(solve('advent_of_code_2022/day_5/input.txt'))