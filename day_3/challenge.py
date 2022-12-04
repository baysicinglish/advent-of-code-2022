

def solve_challenge(filename):
    total = 0

    with open(filename, "r") as file:
        for line in file:
            midpoint = len(line)//2
            left, right = set(line[:midpoint]), set(line[midpoint:])
            shared_char = left.intersection(right).pop()

            total += char_to_value(shared_char)

        return total


def solve_challenge_part_2(filename):
    total = 0

    with open(filename, "r") as file:
        lines = file.readlines()
        for index in range(0, len(lines), 3):
            current_lines = [set(line.strip()) for line in lines[index:index + 3]]

            shared_letter = get_shared_value(current_lines)

            total += char_to_value(shared_letter)

    return total

def get_shared_value(list_of_sets):
    current = list_of_sets[0]
    for set_ in list_of_sets[1:]:
        current = current.intersection(set_)
    return current.pop()


def get_shared_value_rec(list_of_sets):

    if len(list_of_sets) == 1:
        return list_of_sets[0].pop()

    list_of_sets[0] = list_of_sets[0].intersection(list_of_sets.pop())
    return get_shared_value_rec(list_of_sets)



def char_to_value(letter):
    return ord(letter) - 96 if letter.islower() else ord(letter) - 38
            

assert solve_challenge_part_2("advent_of_code_2022/Day3/test.txt") == 70
