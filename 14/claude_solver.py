from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional, Tuple
import re
from enum import Enum

# Constants
GRID_WIDTH = 101
GRID_HEIGHT = 103
SIMULATION_TIME = 100

@dataclass
class Position:
    x: int
    y: int

    def __add__(self, other: 'Position') -> 'Position':
        return Position(self.x + other.x, self.y + other.y)

@dataclass
class Robot:
    position: Position
    velocity: Position

    def move(self, width: int, height: int) -> None:
        """Move the robot one time step, wrapping around grid boundaries."""
        new_pos = self.position + self.velocity
        self.position.x = new_pos.x % width
        self.position.y = new_pos.y % height

class Grid:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.cells = [[0 for _ in range(width)] for _ in range(height)]

    def place_robots(self, robots: List[Robot]) -> None:
        """Reset grid and place all robots in their current positions."""
        self.cells = [[0 for _ in range(self.width)] for _ in range(self.height)]
        for robot in robots:
            self.cells[robot.position.y][robot.position.x] += 1

    def __str__(self) -> str:
        """Convert grid to string representation."""
        return '\n'.join(
            ''.join(str(cell) if cell > 0 else '.' for cell in row)
            for row in self.cells
        )

class Quadrant(Enum):
    TOP_LEFT = 0
    TOP_RIGHT = 1
    BOTTOM_LEFT = 2
    BOTTOM_RIGHT = 3

class Simulation:
    def __init__(self, width: int = GRID_WIDTH, height: int = GRID_HEIGHT):
        self.width = width
        self.height = height
        self.grid = Grid(width, height)
        self.robots: List[Robot] = []

    @staticmethod
    def parse_input(file_path: str) -> List[Robot]:
        """Parse robot definitions from input file."""
        ROBOT_PATTERN = r"""
            p=(?P<pos_x>\d{1,3}),(?P<pos_y>\d{1,3})\s+
            v=(?P<vel_x>-?\d{1,3}),(?P<vel_y>-?\d{1,3})
        """
        pattern = re.compile(ROBOT_PATTERN.strip(), re.VERBOSE)
        robots = []

        path = Path(file_path)
        with path.open() as f:
            for line in f:
                if match := pattern.search(line):
                    robots.append(Robot(
                        position=Position(
                            int(match.group('pos_x')),
                            int(match.group('pos_y'))
                        ),
                        velocity=Position(
                            int(match.group('vel_x')),
                            int(match.group('vel_y'))
                        )
                    ))
        return robots

    def load_robots(self, file_path: str) -> None:
        """Load robots from input file."""
        self.robots = self.parse_input(file_path)

    def step(self) -> None:
        """Advance simulation by one time step."""
        for robot in self.robots:
            robot.move(self.width, self.height)

    def get_quadrant_counts(self) -> List[int]:
        """Count robots in each quadrant, excluding center lines."""
        counts = [0] * 4
        mid_x = (self.width - 1) // 2
        mid_y = (self.height - 1) // 2

        for robot in self.robots:
            x, y = robot.position.x, robot.position.y
            if x == mid_x or y == mid_y:
                continue
            if x < mid_x and y < mid_y:
                counts[Quadrant.TOP_LEFT.value] += 1
            elif x > mid_x and y < mid_y:
                counts[Quadrant.TOP_RIGHT.value] += 1
            elif x < mid_x and y > mid_y:
                counts[Quadrant.BOTTOM_LEFT.value] += 1
            elif x > mid_x and y > mid_y:
                counts[Quadrant.BOTTOM_RIGHT.value] += 1
        return counts

    def calculate_safety_factor(self) -> int:
        """Calculate safety factor as product of quadrant counts."""
        counts = self.get_quadrant_counts()
        result = 1
        for count in counts:
            result *= count
        return result

    def detect_tree_pattern(self) -> bool:
        """Check if current robot positions form a Christmas tree pattern."""
        self.grid.place_robots(self.robots)
        return self._check_tree_pattern()

    def _check_tree_pattern(self) -> bool:
        """
        Check for a line of robots either horizontally or vertically.
        Returns True if a line of at least 10 robots is found.
        """
        # Check horizontal lines
        for y in range(self.height):
            consecutive = 0
            for x in range(self.width):
                if self.grid.cells[y][x] > 0:
                    consecutive += 1
                    if consecutive >= 10:
                        return True
                else:
                    consecutive = 0
        
        # Check vertical lines
        for x in range(self.width):
            consecutive = 0
            for y in range(self.height):
                if self.grid.cells[y][x] > 0:
                    consecutive += 1
                    if consecutive >= 10:
                        return True
                else:
                    consecutive = 0
                    
        return False

def solve_part_one(input_file: str) -> int:
    """
    Solve part one: Calculate safety factor after 100 seconds.
    
    Args:
        input_file: Path to input file containing robot definitions
        
    Returns:
        Safety factor (product of robots in each quadrant)
    """
    sim = Simulation()
    sim.load_robots(input_file)
    
    for _ in range(SIMULATION_TIME):
        sim.step()
    
    return sim.calculate_safety_factor()

def solve_part_two(input_file: str, max_time: int = 10000) -> Optional[int]:
    """
    Solve part two: Find first occurrence of Christmas tree pattern.
    Print the pattern when found.
    
    Args:
        input_file: Path to input file containing robot definitions
        max_time: Maximum number of seconds to simulate
        
    Returns:
        Number of seconds elapsed when tree pattern first appears,
        or None if pattern is not found
    """
    sim = Simulation()
    sim.load_robots(input_file)
    
    for t in range(max_time):
        sim.grid.place_robots(sim.robots)  # Update grid with current positions
        if sim.detect_tree_pattern():
            print(f"\nTree pattern found at time {t}:")
            print(f"{'Grid Map':=^80}")
            print(str(sim.grid))  # This will use our Grid.__str__ method
            print("="*80)
            return t
        sim.step()
    
    return None

def main():
    input_file = "input.txt"
    
    # Solve part one
    safety_factor = solve_part_one(input_file)
    print(f"Part One - Safety Factor: {safety_factor}")
    
    # Solve part two with visualization
    tree_time = solve_part_two(input_file)
    if tree_time is not None:
        print(f"\nPart Two - Tree appears after {tree_time} seconds")
    else:
        print("\nPart Two - No tree pattern found")

if __name__ == "__main__":
    main()
