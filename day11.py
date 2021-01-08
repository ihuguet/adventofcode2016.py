#!/usr/bin/env python3

import heapq

pwrs_mapping = {}
types_mapping = {'microchip': -1, 'generator': 1}
pwrs_next_mapping = 1
def parse_line(line):
    global pwrs_mapping
    global types_mapping
    global pwrs_next_mapping

    line = line.strip().partition('contains')[2]
    if (line == ' nothing relevant.'):
        return []

    objs = []
    line = line[:-1].replace(', and', ' and').replace(' and', ',') # some lines finish with ', and' and some only with ' and'
    for token_str in line.split(','):
        token_words = token_str.strip().split()
        objs.append((token_words[1].split('-')[0], token_words[2]))
    
    result = []
    for pwr_type, obj_type in objs:
        if pwr_type not in pwrs_mapping:
            pwrs_mapping[pwr_type] = pwrs_next_mapping
            pwrs_next_mapping += 1
        result.append(types_mapping[obj_type] * pwrs_mapping[pwr_type]) # -num for microchip, num for generator
    
    return sorted(result)

floors = {}    
with open('day11_in.txt') as f:
    floors[0] = parse_line(f.readline())
    floors[1] = parse_line(f.readline())
    floors[2] = parse_line(f.readline())
    floors[3] = parse_line(f.readline())


def is_generator(obj_id):
    return obj_id > 0

def is_microchip(obj_id):
    return obj_id < 0

def is_valid_combination(objs):
    generators = list(filter(is_generator, objs))
    for mc in filter(is_microchip, objs):
        if len(generators) > 0 and -mc not in generators:
            return False
    return True

def copy_without_objs(objs, objs_rm):
    objs = list(objs)
    for obj in objs_rm:
        objs.remove(obj)
    return objs

def is_valid_move(floor_orig, floor_dest, objs_move):
    floor_orig_new = copy_without_objs(floor_orig, objs_move)
    floor_dest_new = floor_dest + objs_move
    return is_valid_combination(objs_move) and is_valid_combination(floor_orig_new) and is_valid_combination(floor_dest_new)
    
def get_valid_movements_combinations(floor_orig, floor_dest):
    combinations = []
    for obj1_id in floor_orig:
        comb = [obj1_id]
        if comb not in combinations and is_valid_move(floor_orig, floor_dest, comb):
            combinations.append(comb)
        
        for obj2_id in filter(lambda x: x != obj1_id, floor_orig):
            comb = [obj1_id, obj2_id]
            comb.sort()
            if comb not in combinations and is_valid_move(floor_orig, floor_dest, comb):
                combinations.append(comb)
    return combinations

class Node:
    def __init__(self, parent, floors, floor_num, steps):
        self.parent = parent
        self.floors = floors
        self.floor_num = floor_num
        self.steps = steps
        self.cost = steps - len(floors[3])     # A* algorithm, cost estimation
        for i in range(3):
            self.cost += len(floors[i]) * (3 - i)    # invented, estimate at least 2 steps per object and floor

    def __lt__(self, other):
        return self.cost < other.cost

    def create_all_valid_children_nodes(self):
        children = []
        for floor_num_new in [self.floor_num + 1, self.floor_num - 1]:
            if floor_num_new < 0 or floor_num_new > 3:
                continue
            combs = get_valid_movements_combinations(self.floors[self.floor_num], self.floors[floor_num_new])
            for objs in combs:
                floors_new = self.floors.copy()
                floors_new[self.floor_num] = copy_without_objs(floors_new[self.floor_num], objs)
                floors_new[floor_num_new] = sorted(floors_new[floor_num_new] + objs)
                children.append(Node(self, floors_new, floor_num_new, self.steps+1))
        return children


def get_equivalent_state(node):
    mappings = {}
    next_mapping = 100  # start with 100 to avoid confusion with real objects ids
    floors_new = []
    for floor_num, floor in node.floors.items():
        floor_new = []
        for obj_id in floor:
            obj_id_abs = abs(obj_id)
            obj_id_sign = obj_id_abs / obj_id
            if not obj_id_abs in mappings:
                mappings[obj_id_abs] = next_mapping
                next_mapping += 1
            floor_new.append(obj_id_sign * mappings[obj_id_abs])
        floors_new.append(tuple(sorted(floor_new)))
    return (node.floor_num, tuple(floors_new))

def calc_min_steps(floors):
    seen_states = {}
    queue = [Node(None, floors, 0, 0)]
    cnt_checks = 0
    min_steps = None
    while queue:
        node = heapq.heappop(queue)
        cnt_checks += 1

        if min_steps and node.steps >= min_steps:
            continue
        if not node.floors[0] and not node.floors[1] and not node.floors[2]:
            if not min_steps or node.steps < min_steps:
                min_steps = node.steps
                break

        for child in node.create_all_valid_children_nodes():
            eq_state = get_equivalent_state(child)
            if eq_state not in seen_states or child.steps < seen_states[eq_state]:
                seen_states[eq_state] = child.steps
                heapq.heappush(queue, child)
    #print(f'Combinations checked = {cnt_checks}')
    return min_steps


# print(get_equivalent_state(Node(None, floors, 0, 0)))
# floors = {0: [-3, -1, -2, 1, 2, 3, 4, 5], 1: [-4, -5], 2: [], 3: []}
# print(get_equivalent_state(Node(None, floors, 3, 0)))
# quit()

min_steps = calc_min_steps(floors.copy())
print(f'Part 1 steps = {min_steps}')

floors[0].extend([pwrs_next_mapping, -pwrs_next_mapping, pwrs_next_mapping+1, -pwrs_next_mapping-1])
floors[0].sort()
min_steps = calc_min_steps(floors.copy())
print(f'Part 2 steps = {min_steps}')
