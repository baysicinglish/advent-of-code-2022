
def solve(input_file):
    visible_trees = 0
    tree_matrix = generate_tree_matrix(input_file)
    for row_index, row in enumerate(tree_matrix):
        for column_index, tree_height in enumerate(row):
            if is_visible(tree_height, {'x': column_index, 'y': row_index}, tree_matrix):
                visible_trees += 1
    return visible_trees

def generate_tree_matrix(input_file):
    tree_matrix = []
    with open(input_file, 'r') as file:
        for line in file:
            tree_matrix.append([int(char) for char in line.strip('\n')])
    return tree_matrix

def is_visible(this_tree_height, coordinates, tree_matrix):
    tree_row = tree_matrix[coordinates['y']]
    trees_to_left, trees_to_right = tree_row[:coordinates['x']], tree_row[coordinates['x'] + 1:]
    tree_column = [row[coordinates['x']] for row in tree_matrix]
    trees_above, trees_below = tree_column[:coordinates['y']], tree_column[coordinates['y'] + 1:]
    
    for direction in (trees_to_left, trees_to_right, trees_above, trees_below):
        if all([tree_height < this_tree_height for tree_height in direction]):
            return True
    return False

def solve_part_2(input_file):
    highscore = 0
    tree_matrix = generate_tree_matrix(input_file)
    for row_index, row in enumerate(tree_matrix):
        for column_index, tree_height in enumerate(row):
            score = get_scenic_score(tree_height, {'x': column_index, 'y': row_index}, tree_matrix)
            highscore = score if score > highscore else highscore
    return highscore

def get_scenic_score(this_tree_height, coordinates, tree_matrix):
    tree_row = tree_matrix[coordinates['y']]
    trees_to_left, trees_to_right = reversed(tree_row[:coordinates['x']]), tree_row[coordinates['x'] + 1:]
    tree_column = [row[coordinates['x']] for row in tree_matrix]
    trees_above, trees_below = reversed(tree_column[:coordinates['y']]), tree_column[coordinates['y'] + 1:]

    directions = (trees_to_left, trees_to_right, trees_above, trees_below)
    scores = [calculate_score(trees, this_tree_height) for trees in directions]

    return prod(scores)

def calculate_score(trees, this_tree_height):
    score = 0
    for tree_height in trees:
        score += 1
        if tree_height >= this_tree_height:
            break
    return score

def prod(nums):
    total = 1
    for num in nums:
        total *= num
    return total
   
assert solve('advent_of_code_2022/day_8/test.txt') == 21
assert solve_part_2('advent_of_code_2022/day_8/test.txt') == 8
print(solve('advent_of_code_2022/day_8/input.txt'))
print(solve_part_2('advent_of_code_2022/day_8/input.txt'))
