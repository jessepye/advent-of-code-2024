import re
from pathlib import Path

def parse_mul_instructions(text: str, handle_conditionals: bool = False) -> int:
    total = 0
    enabled = True
    
    # Find all valid mul instructions and control statements
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\)'
    matches = re.finditer(pattern, text)
    
    for match in matches:
        instruction = match.group(0)
        
        if handle_conditionals:
            if instruction == "do()":
                enabled = True
                continue
            elif instruction == "don't()":
                enabled = False
                continue
        
        if instruction.startswith("mul") and (enabled or not handle_conditionals):
            x, y = map(int, match.groups())
            total += x * y
            
    return total

def solve_parts(input_path: str = "input.txt") -> tuple[int, int]:
    text = Path(input_path).read_text()
    return (
        parse_mul_instructions(text),
        parse_mul_instructions(text, handle_conditionals=True)
    )

if __name__ == "__main__":
    part1, part2 = solve_parts()
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
