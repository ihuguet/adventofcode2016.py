#!/usr/bin/env python3

import heapq


def get_adjacents(pos):
    adjs = []
    for x_sum, y_sum in [(0,1), (0,-1), (1,0), (-1,0)]:
        x = pos[0] + x_sum
        y = pos[1] + y_sum
        if y < 0 or y >= y_len or x < 0 or x >= x_len:
            continue
        if circuit[y][x] != '#':
            adjs.append((x,y))
    return adjs


with open('day24_in.txt') as f:
    circuit = []
    targets = []
    for y,l in enumerate(f):
        circuit.append(l.strip())
        for x,ch in enumerate(l.strip()):
            if ch == '0':
                start = (x,y)
            elif ch in '123456789':
                targets.append(ch)
    targets.sort()
    y_len = len(circuit)
    x_len = len(circuit[0])


# (tgts_left_cnt, steps, pos, tgts_left)
routes = [(len(targets), 0, start, targets)]

# (tgts_left, pos): steps
seen_states = {}

min_steps1 = None
min_steps2 = None

while routes:
    _, steps, pos, tgts = heapq.heappop(routes)

    if min_steps2 and steps >= min_steps2:
        continue
    
    pos_val = circuit[pos[1]][pos[0]]
    if pos_val in '123456789' and pos_val in tgts:  # target found
        tgts.remove(pos_val)
        if not tgts and (not min_steps1 or steps < min_steps1):
            min_steps1 = steps
    if not tgts and pos_val == '0':   # all targets found and returned to beginning
        min_steps2 = steps
        continue

    state = (tuple(tgts), pos)
    if state not in seen_states or steps < seen_states[state]:
        seen_states[state] = steps
        for next_pos in get_adjacents(pos):
            heapq.heappush(routes, (len(tgts), steps+1, next_pos, tgts.copy()))

print(f'Part 1: min. steps = {min_steps1}')
print(f'Part 2: min. steps = {min_steps2}')
