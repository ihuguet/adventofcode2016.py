class Bot:
    def __init__(self, high_to, low_to):
        self.high_to = high_to
        self.low_to  = low_to
        self.chips   = []

    def give_chips(self):
        give_chip(self.chips[0], self.high_to)
        give_chip(self.chips[1], self.low_to)
        self.chips.clear()

    def __repr__(self):
        return f'Bot(h/l={(self.high_to,self.low_to)}, chips={self.chips})'

def parse_bot_line(line):
    words = line.strip().split()
    high_to = (words[-2], int(words[-1]))
    low_to  = (words[5], int(words[6]))
    return (int(words[1]), Bot(high_to, low_to))

def parse_chip_line(line):
    words = line.strip().split()
    return (int(words[1]), int(words[-1]))

def give_chip(chip_num, dest):
    dest_type, dest_num = dest
    if dest_type == 'bot':
        bots[dest_num].chips.append(chip_num)
        bots[dest_num].chips.sort(reverse=True)
    else:
        outputs[dest_num] = chip_num

bots = {}
chips = {}
outputs = {}
with open('day10_in.txt') as f:
    line = f.readline()
    while line:
        if line.startswith('bot'):
            k, v = parse_bot_line(line)
            bots[k] = v
        elif line.startswith('value'):
            k, v = parse_chip_line(line)
            chips[k] = v
        line = f.readline()

for chip, bot in chips.items():
    give_chip(chip, ('bot', bot))
chips.clear()

bot_61_17 = None
while not bot_61_17 or 0 not in outputs or 1 not in outputs or 2 not in outputs:
    for bot_num, bot_data in bots.items():
        if bot_data.chips == [61, 17]:
            bot_61_17 = bot_num
        if len(bot_data.chips) == 2:
            bot_data.give_chips()

print(f'Part1: ID of bot that compares chips 61 and 17: {bot_61_17}')
print(f'Part2: mult of outputs 0, 1 and 2: {outputs[0]*outputs[1]*outputs[2]}')