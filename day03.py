triangles_part1 = []
triangles_part2 = []

with open('day3_in.txt') as f:
    side = 0
    triangles_buff = [[0] * 3, [0] * 3, [0] * 3]
    for line in f:
        line_nums = [int(num) for num in line.split()]

        triangles_part1.append(line_nums)

        for num in range(0, len(line_nums)):
            triangles_buff[num][side] = line_nums[num]
        if side == 2:
            triangles_part2.extend(triangles_buff)
            triangles_buff = [[0] * 3, [0] * 3, [0] * 3]
            side = 0
        else:
            side += 1

def count_valid_triangles(triangles):
    valid_triangles_cnt = 0
    for a, b, c in triangles:
        if a < b + c and b < a + c and c < a + b:
            valid_triangles_cnt += 1
    return valid_triangles_cnt

print(f'Valid triangles part 1= {count_valid_triangles(triangles_part1)}')
print(f'Valid triangles part 2= {count_valid_triangles(triangles_part2)}')
        