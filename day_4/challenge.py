
def solve(input_file):
    inclusive_sets = 0
    with open(input_file) as file:
        for line in file:
            sections1, sections2 = [get_sections(section_range) for section_range in line.split(',')]
            if has_partial_overlap(sections1, sections2):
                inclusive_sets += 1
    return inclusive_sets


def get_sections(section_range):
    lower_section, upper_section = [int(section_bound) for section_bound in section_range.split('-')]
    return {section for section in range(lower_section, upper_section + 1)}


def has_complete_overlap(set1, set2):
    return not (set1.difference(set2) and set2.difference(set1))


def has_partial_overlap(set1, set2):
    return bool(set1.intersection(set2))


assert solve("advent_of_code_2022/Day4/test.txt") == 4
print(solve("advent_of_code_2022/Day4/input.txt"))
