#!/usr/bin/env python3

import re

def execute_program(instructions, regs):
    output = []
    instructions = instructions.copy()
    pc = 0
    while pc < len(instructions):
        operation, *operators = instructions[pc].split()
        pc_sum = 1
        if operation == 'cpy':
            if operators[1] in regs: # avoid invalid copy
                regs[operators[1]] = get_value(operators[0], regs)
        elif operation == 'inc':
            regs[operators[0]] += 1
        elif operation == 'dec':
            regs[operators[0]] -= 1
        elif operation == 'jnz':
            if get_value(operators[0], regs) != 0:
                pc_sum = get_value(operators[1], regs)
                if pc_sum < 0:
                    pc_sum = fast_loop(instructions, pc, regs)
        elif operation == 'tgl':
            pc_tgt = pc + get_value(operators[0], regs)
            if pc_tgt >= 0 and pc_tgt < len(instructions):
                instructions[pc_tgt] = toggle(instructions[pc_tgt])
        elif operation == 'out':
            output.append(get_value(operators[0], regs))
            if not check_valid_clk(output):
                return False
            if len(output) >= 1000:
                return True
        else:
            raise ValueError(f'Unknown instruction: {operation}')
        pc = pc + pc_sum

    return False

def get_value(operator, regs):
    if operator in regs:
        return regs[operator]
    return int(operator)

def toggle(instruction):
    operation, *operators = instruction.split()
    if len(operators) == 1:
        operation = 'dec' if operation == 'inc' else 'inc'
    else:
        operation = 'cpy' if operation == 'jnz' else 'jnz'
    return operation + ' ' + ' '.join(operators)

def fast_loop(instructions, pc, regs):
    jump_count = instructions[pc].split()[2]
    try:
        if jump_count == '-2':
            fast_loop_simple(instructions, pc, regs)
            return 1
        elif jump_count == '-5':
            fast_loop_double(instructions, pc, regs)
            return 1
    except Exception as e:
        print(e)

    return get_value(jump_count, regs)

def fast_loop_simple(instructions, pc, regs):
    loop_reg, mod_reg, mod_sum = calc_fast_loop_simple(instructions, pc, regs)
    regs[loop_reg] = 0
    regs[mod_reg] += mod_sum

def fast_loop_double(instructions, pc, regs):
    if (not is_cpy(instructions[pc-5]) or
        not are_incdec(instructions[pc-4:pc-2] + instructions[pc-1:pc])):
        raise Exception('Unsupported fast loop')

    _, reload_src, reload_dest = instructions[pc-5].split()
    loop_in_reg = instructions[pc-2].split()[1]
    loop_out_reg = instructions[pc].split()[1]
    loop_out_op, r = instructions[pc-1].split()
    if loop_in_reg != reload_dest or loop_in_reg == loop_out_reg or loop_out_reg != r:
        raise Exception('Unsupported fast loop')

    loops_count = get_value(loop_out_reg, regs)
    if is_inifinite_loop(loops_count, loop_out_op):
        raise Exception('Infinite loop')
    if loops_count < 0:
        loops_count = -loops_count

    if reload_dest in regs:
        regs[reload_dest] = get_value(reload_src, regs)
    _, mod_reg, mod_sum = calc_fast_loop_simple(instructions, pc-2, regs)

    regs[loop_in_reg] = 0
    regs[loop_out_reg] = 0
    regs[mod_reg] += mod_sum * loops_count

def calc_fast_loop_simple(instructions, pc, regs):
    if not are_incdec(instructions[pc-2:pc]):
        raise Exception('Unsupported fast loop')

    loop_reg = instructions[pc].split()[1]
    op1, arg1 = instructions[pc-2].split()
    op2, arg2 = instructions[pc-1].split()

    if loop_reg == arg1 and loop_reg != arg2:
        loop_op = op1
        mod_op, mod_reg = op2, arg2
    elif loop_reg == arg2 and loop_reg != arg1:
        loop_op = op2
        mod_op, mod_reg = op1, arg1
    else:
        raise Exception('Unsupported fast loop')

    loops_count = get_value(loop_reg, regs)
    if is_inifinite_loop(loops_count, loop_op):
        raise Exception('Infinite loop')
    if loops_count < 0:
        loops_count = -loops_count 

    mod_sum = loops_count if mod_op == 'inc' else -loops_count
    return (loop_reg, mod_reg, mod_sum)

def is_cpy(instruction):
    return re.match('^cpy ([0-9]+|[abcd]) [abcd]$', instruction)

def are_incdec(instructions):
    incdec_re = re.compile('^(inc|dec) [abcd]$')
    for instr in instructions:
        if not incdec_re.match(instr):
            return False
    return True

def is_inifinite_loop(loops_count, loop_operation):
    return (loops_count > 0 and loop_operation == 'inc') or (loops_count < 0 and loop_operation == 'dec')

def check_valid_clk(output):
    prev = output[0]
    if prev not in [0,1]:
        return False
    for val in output[1:]:
        if val not in [0,1] or val == prev:
            return False
        prev = val
    return True


with open('day25_in.txt') as f:
    instructions = [l.strip() for l in f]

regs = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
while not execute_program(instructions, regs.copy()):
    regs['a'] += 1
print(f'Part 1: value = {regs["a"]}')
# regs = execute_program(instructions, {'a': 12, 'b': 0, 'c': 1, 'd': 0})
# print(f'Part 2: value = {regs["a"]}')
