messages = None
with open('day6_in.txt') as f:
    messages = [l.strip() for l in f.readlines()]

good_message1 = ''
good_message2 = ''
for i in range(0, len(messages[0])):
    letters_count = {}
    for msg in messages:
        letter = msg[i]
        if letter not in letters_count:
            letters_count[letter] = 0
        else:
            letters_count[letter] += 1
    
    higher_count = ('', 0)
    lower_count  = ('', len(messages) + 1)
    for letter, count in letters_count.items():
        if count > higher_count[1]:
            higher_count = (letter, count)
        if count < lower_count[1]:
            lower_count = (letter, count)
    
    good_message1 = good_message1 + higher_count[0]
    good_message2 = good_message2 + lower_count[0]

print(f'Part1: message: {good_message1}')
print(f'Part2: message: {good_message2}')
