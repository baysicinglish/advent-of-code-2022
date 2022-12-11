
class Direction:
    UP = 'U'
    DOWN = 'D'
    LEFT = 'L'
    RIGHT = 'R'
    VERTICAL = (UP, DOWN)
    HORIZONTAL = (LEFT, RIGHT)
    NEGATIVE = (LEFT, DOWN)

    def __init__(self, direction):
        self.direction = direction
    
    def __repr__(self):
        return self.direction

    def apply(self, coordinate, distance):
        index = 0 if self.direction in self.__class__.HORIZONTAL else 1
        offset = distance if self.direction not in self.__class__.NEGATIVE else distance * -1
        coordinate[index] += offset
    
    @classmethod
    def get_directions_of_offset(cls, offset):
        offset_directions = []
        horizontal, vertical = offset
        if horizontal:
            offset_directions.append(cls.LEFT if horizontal < 0 else cls.RIGHT)
        if vertical:
            offset_directions.append(cls.DOWN if vertical < 0 else cls.UP)
        return [Direction(direction) for direction in offset_directions]

class Knot:
    def __init__(self):
        self.location = [0, 0]
        self.linked_knot = None
        self.visited_locations = set()
        self.visited_locations.add((0, 0))
    
    def _apply_movement(self, direction):
        direction.apply(self.location, 1)
    
    def move(self, direction, amount):
        for _ in range(amount):
            self._apply_movement(direction)
            if self.linked_knot:
                self.linked_knot.follow(self)
                
    def follow(self, knot):
        offset = knot.get_offset(self)
        if 2 in offset or -2 in offset:
            follow_directions = Direction.get_directions_of_offset(offset)
            for follow_direction in follow_directions:
                self._apply_movement(follow_direction)
            if self.linked_knot:
                self.linked_knot.follow(self)
            self.visited_locations.add(tuple(self.location))

    def link(self, knot):
        self.linked_knot = knot
    
    def get_offset(self, knot):
        return self.location[0] - knot.location[0], self.location[1] - knot.location[1]


def solve(input_file):
    # head, tail = Knot(), Knot()
    # head.link(tail)
    # knots = [head, tail]

    knots = [Knot() for _ in range(10)]
    head = knots[0]
    previous = head
    for knot in knots[1:]:
        previous.link(knot)
        previous = knot
    tail = knots[-1]

    with open(input_file, 'r') as file:
        for line in file:
            direction, amount = line.split()
            direction = Direction(direction)
            head.move(direction, int(amount))
    print(len(tail.visited_locations))
            
# solve("advent_of_code_2022/day_9/test.txt")
solve("advent_of_code_2022/day_9/input.txt")
