#!/usr/bin/env python3

def scramble(ops_list, pwd):
    for line in ops_list:
        words = line.split()
        optr = f'{words[0]} {words[1]}'
        if optr == 'swap position':
            pwd = swap_pos(pwd, int(words[2]), int(words[5]))
        elif optr == 'swap letter':
            pwd = swap_letters(pwd, words[2], words[5])
        elif optr == 'rotate left':
            pwd = rotate(pwd, -int(words[2]))
        elif optr == 'rotate right':
            pwd = rotate(pwd, int(words[2]))
        elif optr == 'rotate based':
            pwd = rotate_based(pwd, words[-1])
        elif optr == 'reverse positions':
            pwd = reverse_between(pwd, int(words[2]), int(words[4]))
        elif optr == 'move position':
            pwd = move_pos(pwd, int(words[2]), int(words[5]))
        else:
            raise Exception(f'Unknown operation: {line.strip()}')
    return pwd

def unscramble(ops_list, pwd):
    for line in reversed(ops_list):
        words = line.split()
        optr = f'{words[0]} {words[1]}'
        if optr == 'swap position':
            pwd = swap_pos(pwd, int(words[5]), int(words[2]))
        elif optr == 'swap letter':
            pwd = swap_letters(pwd, words[5], words[2])
        elif optr == 'rotate left':
            pwd = rotate(pwd, int(words[2]))
        elif optr == 'rotate right':
            pwd = rotate(pwd, -int(words[2]))
        elif optr == 'rotate based':
            pwd = rotate_based_undo(pwd, words[-1])
        elif optr == 'reverse positions':
            pwd = reverse_between(pwd, int(words[2]), int(words[4]))
        elif optr == 'move position':
            pwd = move_pos(pwd, int(words[5]), int(words[2]))
        else:
            raise Exception(f'Unknown operation: {line.strip()}')
    return pwd

def swap_pos(txt, idx1, idx2):
    if idx1 > idx2:
        idx1, idx2 = idx2, idx1
    return txt[:idx1] + txt[idx2] + txt[idx1+1:idx2] + txt[idx1] + txt[idx2+1:]

def swap_letters(txt, letter1, letter2):
    return swap_pos(txt, txt.index(letter1), txt.index(letter2))

def rotate(txt, rotation):
    rotation = rotation % len(txt) # avoid full rotations
    return txt[-rotation:] + txt[:-rotation]

def rotate_based(txt, letter):
    idx = txt.index(letter)
    rotation = 1 + idx + (1 if idx >= 4 else 0)
    return rotate(txt, rotation)

def rotate_based_undo(txt, letter):
    idx = txt.index(letter)
    for i in range(len(txt)):
        txt_new = rotate(txt, -i)
        if txt == rotate_based(txt_new, letter):
            return txt_new
    raise Exception(f'Cannot undo rotate_based(\'{txt}\', \'{letter}\')')

def reverse_between(txt, idx1, idx2):
    if idx1 > idx2:
        idx1, idx2 = idx2, idx1
    reversed_substr = ''.join(reversed(txt[idx1:idx2+1]))
    return txt[:idx1] + reversed_substr + txt[idx2+1:]

def move_pos(txt, idx_src, idx_dst):
    if idx_src < idx_dst:
        return txt[:idx_src] + txt[idx_src+1:idx_dst+1] + txt[idx_src] + txt[idx_dst+1:]
    else:
        return txt[:idx_dst] + txt[idx_src] + txt[idx_dst:idx_src] + txt[idx_src+1:]


with open('day21_in.txt') as f:
    ops_list = [line.strip() for line in f]
print(f'Part 1: pwd = {scramble(ops_list, "abcdefgh")}')
print(f'Part 2: pwd = {unscramble(ops_list, "fbgdceah")}')
