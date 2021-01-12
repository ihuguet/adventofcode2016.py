#!/usr/bin/env python3

disks = []
with open('day15_in.txt') as f:
    for line in f:
        words = line.split()
        disks.append((int(words[3]), int(words[-1][:-1])))

def calc_first_success_time(disks):
    time = 0
    inc = 1
    for disk_num in range(1, len(disks) + 1):
        disk_positions, disk_offset = disks[disk_num - 1]
        while (time + disk_offset + disk_num) % disk_positions != 0:
            time += inc
        inc = lcm(inc, disk_positions)
    return time
    
def gcd(a, b):
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

print(f'Part1: first success time = {calc_first_success_time(disks)}')
print(f'Part2: first success time = {calc_first_success_time(disks + [(11, 0)])}')

