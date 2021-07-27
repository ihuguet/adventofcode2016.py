#!/usr/bin/env python

import heapq
import copy

nodes = dict()
x_max, y_max = 0, 0

with open('day22_in.txt') as f:
    lines = f.readlines()[2:]
    for line in lines:
        cols = line.split()
        coords = cols[0].split('-')[1:]
        x, y = int(coords[0][1:]), int(coords[1][1:])
        size, used = int(cols[1][:-1]), int(cols[2][:-1])
        if not x in nodes:
            nodes[x] = dict()
        nodes[x][y] = (size, used)
        if x + 1 > x_max:
            x_max = x + 1
        if y + 1 > y_max:
            y_max = y + 1

def is_viable_move(src, dst):
    free_in_dst = dst[0] - dst[1]
    return src[1] > 0 and free_in_dst >= src[1]

cnt_viable_movs = 0
viable_srcs = set()
for x1 in range(x_max):
    for y1 in range(y_max):
        y2 = y1 + 1
        for x2 in range(x1, x_max):
            while y2 < y_max:
                if is_viable_move(nodes[x1][y1], nodes[x2][y2]):
                    cnt_viable_movs += 1
                    viable_srcs.add((x1,y1))
                if is_viable_move(nodes[x2][y2], nodes[x1][y1]):
                    cnt_viable_movs += 1
                    viable_srcs.add((x2,y2))
                y2 += 1
            y2 = 0

print(f'Part 1: viable movs = {cnt_viable_movs}')
print('Part 2: this is the grid, must be solved by hand!')
print('        Seriously, by hand. I had to give up and find the solution in Reddit: do it by hand')
print('        G=goal, S=start, #=unusable nodes, _=empty node, .=movable nodes')
for y in range(y_max):
    for x in range(x_max):
        if (x,y) == (0,0):
            print('G', end='')
        elif (x,y) == (x_max-1,0):
            print('S', end='')
        elif nodes[x][y][1] == 0:
            print('_', end='')
        elif (x,y) in viable_srcs:
            print('.', end='')
        else:
            print('#', end='')
    print()
