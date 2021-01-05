lines = None
with open('day7_in.txt') as f:
    lines = [l.strip() for l in f.readlines()]


# PART 1
valid_tls_count = 0
for line in lines:
    within_brackets = False
    abba_invalid = False
    abba_found = False
    for i in range(0, len(line) - 3):
        a, b, c, d = line[i:i+4]
        if a == '[':
            within_brackets = True
        elif a == ']':
            within_brackets = False
        elif within_brackets and a != b and b == c and a == d:
            abba_invalid = True
        elif a != b and b == c and a == d:
            abba_found = True

    if abba_found and not abba_invalid:
        valid_tls_count += 1


# PART 2
valid_ssl_count = 0
for line in lines:
    within_brackets = False
    aba_outside_brackets = []
    aba_within_brackets = []
    for i in range(0, len(line) - 2):
        a, b, c = line[i:i+3]
        if not b.isalpha() or not c.isalpha():
            continue
        elif a == '[':
            within_brackets = True
        elif a == ']':
            within_brackets = False
        elif within_brackets and a != b and a == c:
            aba_within_brackets.append(a+b+c)
        elif a != b and a == c:
            aba_outside_brackets.append(a+b+c)

    for a, b, c in aba_outside_brackets:
        if b+a+b in aba_within_brackets:
            valid_ssl_count += 1
            break


print(f"Part 1: {valid_tls_count} valid TLS addresses")
print(f"Part 2: {valid_ssl_count} valid SSL addresses")
