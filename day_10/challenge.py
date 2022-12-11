
def cycle(num_cycles):
    def cycle_wrapper(func):
        def execute(self, *args, **kwargs):
            for _ in range(num_cycles):
                self.cycles += 1
                self.register_values.append(self.register)
                self.signal_strengths.append(self.cycles * self.register)
            return func(self, *args, **kwargs)
        return execute
    return cycle_wrapper


class CPU:
    def __init__(self):
        self.register = 1
        self.cycles = 0
        self.signal_strengths = [1]
        self.register_values = [self.register]
    
    @cycle(1)
    def noop(self):
        pass
    
    @cycle(2)
    def addx(self, value):
        self.register += value


class CRT:
    def __init__(self):
        self.pixels = [['.'] * 40 for _ in range(6)]
    
    @property
    def display(self):
        return '\n'.join(''.join(row) for row in self.pixels)
    
    def draw(self, register_stream):
        for cycle, register_value in enumerate(register_stream[1:]):
            if cycle % 40 in range(register_value - 1, register_value + 2):
                print(cycle, register_value, True)
                self.pixels[cycle // 40][cycle % 40] = '#'
            else:
                print(cycle, register_value, False)


def solve(input_file):
    cpu = CPU()

    with open(input_file) as file:
        command = file.readline()
        while command:
            args = command.split()
            getattr(cpu, args[0])(*[int(arg) for arg in args[1:]])
            command = file.readline()
        
        crt = CRT()
        crt.draw(cpu.register_values)
        print(crt.display)
        # return sum(cpu.signal_strengths[index] for index in range(20, cpu.cycles, 40))
        return sum(cpu.register_values[cycle] * cycle for cycle in range(20, cpu.cycles, 40))

print(solve('advent_of_code_2022/day_10/input.txt'))
# assert solve('advent_of_code_2022/day_10/test.txt') == 13140

