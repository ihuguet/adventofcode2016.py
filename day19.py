#!/usr/bin/env python3

class Node:
    def __init__ (self, elf_id):
        self.elf_id = elf_id
        self.next = None
        self.prev = None

    def pop (self):
        if self.prev: self.prev.next = self.next
        if self.next: self.next.prev = self.prev

def get_game_winner_p1 (elfs_num):
    first_elf = 1
    gap = 2
    while elfs_num > 1:
        if elfs_num % 2 != 0:
            first_elf += gap
        elfs_num //= 2
        gap *= 2
    return first_elf

def get_game_winner_p2 (elfs_num):
    next_to_play, next_to_del = create_circle(elfs_num)
    while not next_to_play.next is next_to_play:
        if elfs_num % 2 == 0:
            next_next_to_del = next_to_del.next
        else:
            next_next_to_del = next_to_del.next.next
        next_to_del.pop()
        next_to_del = next_next_to_del
        next_to_play = next_to_play.next
        elfs_num -= 1
    return next_to_play.elf_id

def create_circle (elfs_num):
    mid_id = 1 + elfs_num // 2
    first = Node(1)
    elf = first
    for i in range(2, elfs_num+1):
        elf.next = Node(i)
        elf.next.prev = elf
        elf = elf.next
        if i == mid_id:
            mid = elf
    elf.next = first # circular
    first.prev = elf

    return (first, mid)


elfs_num = 3017957 # puzzle input
print(f'Part 1: winner elf = {get_game_winner_p1(elfs_num)}')
print(f'Part 2: winner elf = {get_game_winner_p2(elfs_num)}')
