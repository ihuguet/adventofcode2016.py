#!/usr/bin/env python3

def get_data_to_fill_disk(data, disk_size):
    while len(data) < disk_size:
        data2 = ''.join(map(lambda ch: '0' if ch=='1' else '1', data[::-1]))
        data  = data + '0' + data2
    return data[:disk_size]

def calc_checksum(data):
    while len(data) % 2 == 0:
        checksum = ''.join(map(lambda i: '1' if data[i] == data[i+1] else '0', range(0, len(data), 2)))
        data = checksum
    return checksum

input_data = "10001110011110000"
data = get_data_to_fill_disk(input_data, 272)
print(f'Part1: checksum = {calc_checksum(data)}')
data = get_data_to_fill_disk(input_data, 35651584)
print(f'Part2: checksum = {calc_checksum(data)}')

