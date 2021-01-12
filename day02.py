keypad1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

keypad2 = [
    [' ', ' ', '1', ' ', ' '],
    [' ', '2', '3', '4', ' '],
    ['5', '6', '7', '8', '9'],
    [' ', 'A', 'B', 'C', ' '],
    [' ', ' ', 'D', ' ', ' ']
]


def key_exists(keypad, coords):
    x, y = coords
    if y < 0 or y >= len(keypad):
        return False
    if x < 0 or x >= len(keypad[y]):
        return False
    if keypad[y][x] == ' ':
        return False
    return True

def solve(keypad, coords_ini, indications):
    x, y = coords_ini
    code = ''

    for line in indications:
        for direction in line:
            x_new, y_new = x, y

            if direction == 'U':
                y_new -= 1
            elif direction == 'D':
                y_new += 1
            elif direction == 'R':
                x_new += 1
            elif direction == 'L':
                x_new -= 1
            else:
                print(f'Wrong direction: {direction}')
            
            if key_exists(keypad, (x_new, y_new)):
                x, y = x_new, y_new
        
        code = code + str(keypad[y][x])
    
    return code

fin = open('day2_in.txt')
indications = [line.strip() for line in fin.readlines()]
fin.close()
print(f'Code part 1 = {solve(keypad1, (1, 1), indications)}')
print(f'Code part 2 = {solve(keypad2, (2, 0), indications)}')
        