#!/usr/bin/env python3

import heapq
import hashlib

def calc_shortest_and_longest_routes (pos, dest, passcode):
    if pos == dest:
        return ''

    active_routes = [(0, pos, '')]  # steps num, position, route
    shortest_route, min_steps = None, None
    longest_route, max_steps = None, 0

    while active_routes:
        steps, pos, route = heapq.heappop(active_routes)
        for open_dir, adj_pos in get_open_dirs_and_pos(pos, route, passcode):
            if adj_pos != dest:
                heapq.heappush(active_routes, (steps + 1, adj_pos, route + open_dir))
            else:
                if not shortest_route or steps + 1 < min_steps:
                    shortest_route, min_steps = route + open_dir, steps + 1
                if steps + 1 > max_steps:
                    longest_route, max_steps = route + open_dir, steps + 1
            
    return (shortest_route, longest_route)

def get_open_dirs_and_pos(pos, route, passcode):
    x, y = pos
    hash = hashlib.md5((passcode + route).encode()).hexdigest()
    spaces = []
    if y > 0 and hash[0] in 'bcdef':
        spaces.append(('U', (x, y - 1)))
    if y < 3 and hash[1] in 'bcdef':
        spaces.append(('D', (x, y + 1)))
    if x > 0 and hash[2] in 'bcdef':
        spaces.append(('L', (x - 1, y)))
    if x < 3 and hash[3] in 'bcdef':
        spaces.append(('R', (x + 1, y)))
    return spaces

def get_pos(pos, dir):
    pos_sums = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}
    pos_sum = pos_sums[dir]
    return (pos[0] + pos_sum[0], pos[1] + pos_sum[1])

passcode = "qzthpkfp"
shortest, longest = calc_shortest_and_longest_routes((0,0), (3,3), passcode)
print(f'Part 1: shortest route = {shortest}')
print(f'Part 2: longest route length = {len(longest)}')
