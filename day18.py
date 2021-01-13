#!/usr/bin/env python3

def count_safe_tiles(first_row, total_rows_count):
    safe_count = sum(1 for ch in first_row if ch == '.')
    row = "." + first_row + "." # fake tiles on both ends
    for i in range(total_rows_count - 1):
        row_new = '.'
        for i in range(1, len(row)-1):
            upper_3_tiles = row[i-1:i+2]
            if upper_3_tiles in ['^^.', '.^^', '^..', '..^']:
                row_new += '^'
            else:
                row_new += '.'
                safe_count += 1
        row = row_new + '.'
    return safe_count

row = "......^.^^.....^^^^^^^^^...^.^..^^.^^^..^.^..^.^^^.^^^^..^^.^.^.....^^^^^..^..^^^..^^.^.^..^^..^^^.."
print(f'Part 1: safe tiles = {count_safe_tiles(row, 40)}')
print(f'Part 2: safe tiles = {count_safe_tiles(row, 400_000)}')
