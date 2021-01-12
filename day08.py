lines = None
with open('day8_in.txt') as f:
    lines = [l.strip() for l in f.readlines()]

PX_WIDTH = 50
PX_HEIGHT = 6
pixels = [[False]*PX_WIDTH for i in range(PX_HEIGHT)]


def fill_rect(pixels, w, h):
    for x in range(w):
        for y in range(h):
            pixels[y][x] = True
    
def rotate_row(pixels, row, positions):
    pixels[row] = pixels[row][-positions:] + pixels[row][:-positions]

def rotate_col(pixels, col, positions):
    col_pxs = [row[col] for row in pixels]
    col_pxs = col_pxs[-positions:] + col_pxs[:-positions]
    for i in range(len(col_pxs)):
        pixels[i][col] = col_pxs[i]

for line in lines:
    words = line.split()
    if words[0] == 'rect':
        rect_size = words[1].split('x')
        fill_rect(pixels, int(rect_size[0]), int(rect_size[1]))
    elif words[0] == 'rotate' and words[1] == 'row':
        row = int(words[2].split('=')[1])
        positions = int(words[-1])
        rotate_row(pixels, row, positions)
    elif words[0] == 'rotate' and words[1] == 'column':
        col = int(words[2].split('=')[1])
        positions = int(words[-1])
        rotate_col(pixels, col, positions)
    else:
        print(f'Invalid line: {line}')

px_on_count = 0
for row in pixels:
    px_on_count += row.count(True)

print(f"Part 1: {px_on_count} px ON")

print("Part 2:")
for row in pixels:
    row_text = ''
    for px in row:
        if px == True:
            row_text = row_text + '#'
        else:
            row_text = row_text + ' '
    print(row_text)