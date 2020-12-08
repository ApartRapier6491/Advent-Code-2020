from typing import Dict, Set

FILENAME = "input.txt"

class Instruction:
    def __init__(self, line_num, operation, argument = 0):
        self.line_num = line_num
        self.opr = operation
        self.arg = argument

    def __iter__(self):
        return iter((self.line_num, self.opr, self.arg))

    def __str__(self):
        return f"{self.opr} {self.arg}"

    def __repr__(self):
        return f"Instruction({self.line_num}, {self.opr}, {self.arg})"

    def change_operation(self, new_operation: str):
        self.opr = new_operation

class InfiniteLoopError(Exception):
    def __init__(self, value = 0):
        self.val = value

    def get_value(self):
        return self.val

def get_input() -> Dict[int, Instruction]:
    instructions = dict()

    with open(FILENAME) as f:
        for line_num, instruction in enumerate(f.readlines(), start=1):
            instruction = instruction.strip().split()

            op, arg = instruction
            instructions[line_num] = Instruction(line_num, op.strip(), int(arg))

    return instructions

def simulate(
        instructions: Dict[int, Instruction],
        line_num: int = 1,
        acc: int = 0,
        visited: Set[int] = None
    ) -> int:

    if visited is None:
        visited = set()

    last_line_num = max(instructions.keys())

    while line_num != last_line_num+1:
        if line_num in visited:
            raise InfiniteLoopError(acc)

        if not 1 <= line_num <= last_line_num:
            raise IndexError("Jumped out of range!")

        visited.add(line_num)

        _, opr, arg = instructions[line_num]

        if opr == "acc":
            acc += arg

        elif opr == "jmp":
            line_num += arg-1

        line_num += 1

    return acc

def part_1():
    instructions = get_input()

    try:
        acc = simulate(instructions)

    except InfiniteLoopError as e:
        acc = e.get_value()

    print("Immediately before the program would run an instruction a second time, "
        f"the value in the accumulator is {acc}.")

def part_2():
    instructions = get_input()

    acc = 0
    line_num = 1
    visited = set()

    while True:

        if line_num in visited:
            raise InfiniteLoopError

        _, opr, arg = instructions[line_num]

        if opr == "acc":
            acc += arg
            visited.add(line_num)

        elif opr == "jmp":
            try:
                instructions[line_num].change_operation("nop")
                acc = simulate(instructions, line_num, acc, visited.copy())
                break

            except (InfiniteLoopError, IndexError):
                instructions[line_num].change_operation("jmp")
                visited.add(line_num)
                line_num += arg-1

        else:
            try:
                instructions[line_num].change_operation("jmp")
                acc = simulate(instructions, line_num, acc, visited.copy())
                break

            except (InfiniteLoopError, IndexError):
                instructions[line_num].change_operation("nop")
                visited.add(line_num)

        line_num += 1

    print(f"the value of the accumulator after the program terminates is {acc}.")

if __name__ == "__main__":
    # part_1()
    # part_2()
    pass
