#!/usr/bin/env python3

import hashlib
import re

def generate_keys(key_stretching_hash_times = 1):
    index = 0
    key_candidates = []
    keys = []

    five_regex  = re.compile(r'(.)\1{4}')
    three_regex = re.compile(r'(.)\1{2}')

    while len(keys) < 64 or key_candidates:
        hash = salt + str(index)
        for i in range(key_stretching_hash_times):
            hash = hashlib.md5(hash.encode()).hexdigest()

        while key_candidates and key_candidates[0][0] < index - 1000:
            key_candidates.pop(0)

        if key_candidates:
            for letter in five_regex.findall(hash):
                for key_cand in filter(lambda kc: kc[1] == letter*3, key_candidates):
                    keys.append(key_cand)
                    keys.sort()
                key_candidates = list(filter(lambda kc: kc[1] != letter*3, key_candidates))

        if len(keys) < 64:
            re_match = three_regex.search(hash)
            if re_match:
                key_candidates.append((index, re_match.group(), hash))

        index += 1

    return keys

salt = "jlmsuwbz"
print(f'Part 1: 64th key = {generate_keys(1)[63]}')
print(f'Part 2: 64th key = {generate_keys(2017)[63]}')
