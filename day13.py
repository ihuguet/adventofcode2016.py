#!/usr/bin/env python3

import heapq

def calc_min_steps (pos, dest):
    if pos == dest:
        return 0

    active_routes = [(0, pos)]  # steps num, position
    visited_pos = {pos: 0}
    min_steps = None

    while active_routes:
        steps, pos = heapq.heappop(active_routes)
        if min_steps and steps + 1 >= min_steps:
            continue
        for adj_pos in get_adjacent_open_spaces(pos):
            if adj_pos not in visited_pos or visited_pos[adj_pos] > steps + 1:
                if adj_pos != dest:
                    heapq.heappush(active_routes, (steps + 1, adj_pos))
                    visited_pos[adj_pos] = steps + 1
                elif not min_steps or steps + 1 < min_steps:
                    min_steps = steps + 1
    
    return min_steps or 0

def calc_visited_spaces_in_range(pos, max_steps):
    if max_steps == 0:
        return 1
    
    active_routes = [(0, pos)]
    visited_pos = {pos: 0}

    while active_routes:
        steps, pos = active_routes.pop()
        if steps + 1 > max_steps:
            continue
        for adj_pos in get_adjacent_open_spaces(pos):
            if adj_pos not in visited_pos or visited_pos[adj_pos] > steps + 1:
                visited_pos[adj_pos] = steps + 1
                active_routes.append((steps + 1, adj_pos))

    return len(visited_pos)

def get_adjacent_open_spaces(pos):
    adjacents = []
    for x, y in [(pos[0]+mov[0], pos[1]+mov[1]) for mov in [(0,1), (0,-1), (1,0), (-1,0)]]:
        if x < 0 or y < 0:
            continue
        num_dec = x*x + 3*x + 2*x*y + y + y*y + puzzle_input
        ones = format(num_dec, 'b').count('1')
        if ones % 2 == 0: # is space, not wall
            adjacents.append((x,y))
    return adjacents

puzzle_input = 1358
print(f'Part 1: min steps = {calc_min_steps((1,1), (31,39))}')
print(f'Part 2: max visited in 50 steps = {calc_visited_spaces_in_range((1,1), 50)}')
