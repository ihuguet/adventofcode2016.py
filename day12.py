#!/usr/bin/env python3

def execute_program(instructions, regs):
    pc = 0
    while pc < len(instructions):
        operation, *operators = instructions[pc].strip().split()
        pc_sum = 1
        if operation == 'cpy':
            regs[operators[1]] = get_value(operators[0], regs)
        elif operation == 'inc':
            regs[operators[0]] += 1
        elif operation == 'dec':
            regs[operators[0]] -= 1
        elif operation == 'jnz':
            if get_value(operators[0], regs) != 0:
                pc_sum = get_value(operators[1], regs)
        else:
            raise ValueError(f'Unknown instruction: {operation}')
        pc = pc + pc_sum

    return regs

def get_value(operator, regs):
    if operator in regs:
        return regs[operator]
    return int(operator)

with open('day12_in.txt') as f:
    instructions = f.readlines()

regs = execute_program(instructions, {'a': 0, 'b': 0, 'c': 0, 'd': 0})
print(f'Part 1: pwd = {regs["a"]}')

regs = execute_program(instructions, {'a': 0, 'b': 0, 'c': 1, 'd': 0})
print(f'Part 2: pwd = {regs["a"]}')
