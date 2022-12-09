ALL_FILES = []
TOTAL_SPACE = 70000000
REQUIRED_SPACE = 30000000

class Drive:
    @property
    def files(self):
        return [file for file in ALL_FILES if file.location == self]

class File:
    def __init__(self, name, location, content=None):
        self.name = name
        self.location = location
        self.content = content
        ALL_FILES.append(self)
    
    @property
    def size(self):
        return int(self.content)
    
    def __repr__(self):
        return f'{self.size} {self.name}'


class Dir(File):
    def __init__(self, name, location):
        super().__init__(name, location)
        self.content = None
    
    def __repr__(self):
        return f'dir {self.name}'
    
    @property
    def files(self):
        return [file for file in ALL_FILES if file.location == self]
    
    @property
    def size(self):
        return sum([file.size for file in self.files])


def solve(input_file):
    current_dir = Drive()
    root = Dir('/', current_dir)
    with open(input_file, 'r') as file:
        lines = file.readlines()
        while lines:
            line = lines.pop(0)
            if line.startswith('$'):
                if 'cd' in line:
                    print(line)
                    current_dir = get_current_dir(current_dir, line.rsplit(maxsplit=1)[-1])
                else:
                    create_local_files(lines, current_dir)
    # return sum(file.size for file in ALL_FILES if isinstance(file, Dir) and file.size < 100000)
    required_space = REQUIRED_SPACE - (TOTAL_SPACE - root.size)
    return min([file.size for file in ALL_FILES if isinstance(file, Dir) and file.size >= required_space])


def get_current_dir(current_dir, target):
    if target == '..':
        return current_dir.location
    return [file for file in current_dir.files if isinstance(file, Dir) and file.name == target][0]


def create_local_files(lines, current_dir):
    while lines and not lines[0].startswith('$'):
        prefix, filename = lines.pop(0).split(maxsplit=2)
        if prefix == 'dir':
            Dir(filename, current_dir)
        else:
            File(filename, current_dir, content=prefix)

# assert solve('advent_of_code_2022/day_7/test.txt') == 95437
print(solve('advent_of_code_2022/day_7/input.txt'))