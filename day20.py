#!/usr/bin/env python3

import heapq

IP_MAX = 4294967295

def merge_ranges(ranges_ips):
    ranges_ips = ranges_ips.copy()
    ranges_merged = []
    low, high = heapq.heappop(ranges_ips)
    while ranges_ips:
        low2, high2 = heapq.heappop(ranges_ips)
        if low2 <= high + 1:
            high = high2 if high2 > high else high
        else:
            ranges_merged.append((low, high))
            low, high = low2, high2
    ranges_merged.append((low, high))
    return ranges_merged
        
def get_min_allowed_ip(blocked_ips):
    blocked_ips = blocked_ips.copy()
    range_ips = heapq.heappop(blocked_ips)
    if range_ips[0] > 0:
        return 0
    while blocked_ips:
        range_ips_next = heapq.heappop(blocked_ips)
        if range_ips_next[0] > range_ips[1] + 1:
            return range_ips[1] + 1
        range_ips = range_ips_next
    if range_ips[1] < IP_MAX:
        return range_ips[1] + 1
    return None

def get_allowed_ips_count(blocked_ips):
    blocked_ips = blocked_ips.copy()
    range_ips = heapq.heappop(blocked_ips)
    allowed_count = range_ips[0]
    while blocked_ips:
        range_ips_next = heapq.heappop(blocked_ips)
        if range_ips_next[0] > range_ips[1]:
            allowed_count += range_ips_next[0] - range_ips[1] - 1
        range_ips = range_ips_next
    if range_ips[1] < IP_MAX:
        allowed_count += IP_MAX - range_ips[1]
    return allowed_count


blocked_ips = []
with open("day20_in.txt") as f:
    for line in f:
        heapq.heappush(blocked_ips, tuple(int(ip) for ip in line.strip().split('-')))
blocked_ips = merge_ranges(blocked_ips)

print(f'Part 1: lowest allowed IP = {get_min_allowed_ip(blocked_ips)}')
print(f'Part 2: allowed IPs count = {get_allowed_ips_count(blocked_ips)}')
