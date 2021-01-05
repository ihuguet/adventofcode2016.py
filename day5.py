import hashlib

door_id = 'ojvtpuvg'

index = 0
pwd = '********'
print('Part 1:')
for i in range(0, 8):
    hash = ''
    while hash[:5] != '00000':
        string = door_id + str(index)
        hash = hashlib.md5(string.encode('utf-8')).hexdigest()
        index += 1
    pwd = pwd[:i] + hash[5] + pwd[i+1:]
    print(f'{hash} -> ch={hash[5]} -> pwd = {pwd}')
pwd1 = pwd

index = 0
pwd = '********'
print('\nPart 2:')
while pwd.count('*') > 0:
    hash = ''
    while hash[:5] != '00000':
        string = door_id + str(index)
        hash = hashlib.md5(string.encode('utf-8')).hexdigest()
        index += 1
    pos = int(hash[5], 16)
    if pos < len(pwd) and pwd[pos] == '*':
        pwd = pwd[:pos] + hash[6] + pwd[pos+1:]
    print(f'{hash} -> pos={hash[5]} ch={hash[6]} -> pwd = {pwd}')

print(f'\nPart 1: pwd = {pwd1}')
print(f'Part 2: pwd = {pwd}')
