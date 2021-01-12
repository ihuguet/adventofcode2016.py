num_letters_in_alphabet = ord('z') - ord('a') + 1

def get_sorted_letters_counts(text):
    letters_counts = {}
    for letter in text:
        if letter not in letters_counts:
            letters_counts[letter] = 0
        else:
            letters_counts[letter] += 1
    letters_counts = list(letters_counts.items())
    letters_counts.sort(key=lambda x: (-x[1], x[0]))
    return letters_counts

def calc_checksum(text):
    csum = ''
    letters_counts = get_sorted_letters_counts(text.replace('-', ''))
    for letter,_ in letters_counts[:5]:
        csum = csum + letter
    return csum

def rotate_letter(letter, rotate_count):
    offset = rotate_count % num_letters_in_alphabet
    new_letter_ord = ord(letter) + offset
    if new_letter_ord > ord('z'):
        new_letter_ord -= num_letters_in_alphabet
    return chr(new_letter_ord)

def decrypt_text(text, rotate_count):
    decr_text = ''
    for letter in text:
        if letter == '-':
            decr_text = decr_text + ' '
        else:
            decr_text = decr_text + rotate_letter(letter, rotate_count)
    return decr_text


valid_sectors_sum = 0
valid_sectors = []
with open('day4_in.txt') as f:
    for line in f:
        line = line.strip()
        split_pos = line.rfind('-')
        crypt_name = line[:split_pos]
        sector_id  = int(line[split_pos+1:-7])
        checksum   = line[-6:-1]

        if (calc_checksum(crypt_name) == checksum):
            valid_sectors_sum += sector_id
            valid_sectors.append((crypt_name, sector_id))

print(f'Part 1: Valid sectors sum = {valid_sectors_sum}')
  
for crypt_name, sector_id in valid_sectors:
    decrypt_name = decrypt_text(crypt_name, sector_id)
    if decrypt_name == 'northpole object storage':
        print(f'Part 2: {sector_id} - {decrypt_name}')
        break


        