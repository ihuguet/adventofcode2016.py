def parse_repetition(rep_text):
    return (int(val) for val in rep_text.split('x'))

def get_expanded_repetitions_length(text, repetitions, recursive):
    i = 0
    len_count = 0
    while i < len(text):
        if text[i] != '(':
            end = text.find('(', i)
            end = end if end != -1 else len(text)
            len_count += end - i
            i = end
        else:
            end = text.find(')', i)
            end = end if end != -1 else len(text)
            ch_count, rep_count = parse_repetition(text[i+1:end])
            i = end + 1
            if recursive:
                len_count += get_expanded_repetitions_length(text[i:i+ch_count], rep_count, True)
            else:
                len_count += ch_count * rep_count
            i += ch_count
    return len_count * repetitions

f = open('day9_in.txt')
compressed_text = f.read().strip()
f.close()
decompressed_text_v1_len = get_expanded_repetitions_length(compressed_text, 1, False)
decompressed_text_v2_len = get_expanded_repetitions_length(compressed_text, 1, True)

print(f'Part 1: decompressed text length (v1) = {decompressed_text_v1_len}')
print(f'Part 2: decompressed text length (v2) = {decompressed_text_v2_len}')