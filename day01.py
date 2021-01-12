indications = open('day1_in.txt').read().split(', ')

def rotate(direction, angle):
    direction += angle
    while direction >= 360:
        direction -= 360
    while direction < 0:
        direction += 360
    return direction

def move_coords(coords, direction, distance):
    x,y = coords
    if direction == 0:
        y += distance
    elif direction == 90:
        x += distance
    elif direction == 180:
        y -= distance
    elif direction == 270:
        x -= distance
    else:
        print(f'Invalid direction (must be multiple of 90): {direction}')
    return (x, y)

def part1 ():
    current_direction = 0
    current_coords = (0, 0)

    for indication in indications:
        direction = indication[0]
        distance = int(indication[1:])
        
        if direction == 'R':
            current_direction = rotate(current_direction, 90)
        elif direction == 'L':
            current_direction = rotate(current_direction, -90)
        else:
            print(f'Error: unknown direction "{direction}"')
        
        current_coords = move_coords(current_coords, current_direction, distance)

    return current_coords

def part2():
    current_direction = 0
    current_coords = (0, 0)
    visited_coords = []

    for indication in indications:
        direction = indication[0]
        distance = int(indication[1:])
        
        if direction == 'R':
            current_direction = rotate(current_direction, 90)
        elif direction == 'L':
            current_direction = rotate(current_direction, -90)
        else:
            print(f'Error: unknown direction "{direction}"')
        
        while distance > 0:
            current_coords = move_coords(current_coords, current_direction, 1)
            if visited_coords.count(current_coords) > 0:
                return current_coords
            else:
                visited_coords.append(current_coords)
            distance -= 1
        
    print('No coords were visited twice')
    return None

coords_p1 = part1()
print('Part 1')
print(f'Final coords {coords_p1}')
print(f'Distance = {coords_p1[0] + coords_p1[1]}')

print()

coords_p2 = part2()
print('Part 2')
print(f'Final coords {coords_p2}')
print(f'Distance = {coords_p2[0] + coords_p2[1]}')


