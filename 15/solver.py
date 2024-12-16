import ipdb

class Simulation:
    def __init__(self, map = [], instructions = ''):
        self.MOVABLE_OBJECTS = {'@', 'O'}
        self.map = map
        self.instructions = instructions
    
    def print_map(self):
        print(f'{'Map':=^80}')
        for y in range(len(self.map)):
            for x in range(len(self.map[0])):
                print(self.map[y][x], end='')
            print()

    def initalize(self, inputFile):
        with open(inputFile, 'r') as file:
            inputText = file.read()
        # import ipdb; ipdb.set_trace()
        self.map, self.instructions = inputText.strip().split('\n\n')
        self.map = [list(line) for line in self.map.strip().split('\n')]
        self.instructions = [val for val in list(self.instructions) if val !='\n']

    def find_robot(self):
        for y in range(len(self.map)):
            for x in range(len(self.map[0])):
                if self.map[y][x] == '@':
                    return x, y

    def push_object(self, object, current_x, current_y, dir):
        if object not in self.MOVABLE_OBJECTS:
            return
        next_x = current_x + (-1 if dir == '<' else 1) * (0 if (dir == '^' or dir == 'v') else 1)
        next_y = current_y + (-1 if dir == '^' else 1) * (0 if (dir == '<' or dir == '>') else 1)
        if next_x < 0 or next_x >= len(self.map[0]):
            return
        if next_y < 0 or next_y >= len(self.map):
            return
        if self.map[next_y][next_x] == '.':
            self.map[current_y][current_x] = '.'
            self.map[next_y][next_x] = object
            return
        if self.map[next_y][next_x] == '#':
            return
        if self.map[next_y][next_x] == 'O':
            self.push_object('O', next_x, next_y, dir)
            if self.map[next_y][next_x] == '.':
                self.map[current_y][current_x] = '.'
                self.map[next_y][next_x] = object
            return

    def step(self):
        instruction = self.instructions.pop(0)
        robot_x, robot_y = self.find_robot()
        # ipdb.set_trace()
        self.push_object('@', robot_x, robot_y, instruction)
        # print(f'Updated map after {instruction}')
        # self.print_map()
        # print('-----------------------------')
    def sum_box_gps_coordinates(self):
        total = 0
        for y in range(len(self.map)):
            for x in range(len(self.map)):
                if self.map[y][x] == 'O':
                    total += 100*y + x
        return total

def solve_part_one(inputFile):
    sim = Simulation()
    sim.initalize(inputFile)
    while(len(sim.instructions) > 0):
        sim.step()
    print("final state:")
    sim.print_map()
    return sim.sum_box_gps_coordinates()

def solve_part_two():
    pass

def main():
    inputFile = 'input.txt'
    # inputFile = 'example.txt'

    print(solve_part_one(inputFile))

    solve_part_two()

if __name__ == '__main__':
    main()
