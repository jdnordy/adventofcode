# https://adventofcode.com/2022/day/2

f = open('day2.inputs.txt', 'r')

part1 = 0
part2 = 0

decoder = {
    'X': 'A',
    'Y': 'B',
    'Z': 'C',
}

throws = ['A', 'B', 'C']

compare_table = {
    'A': {
        'A': 3,
        'B': 6,
        'C': 0,
    },
    'B': {
        'A': 0,
        'B': 3,
        'C': 6,
    },
    'C': {
        'A': 6,
        'B': 0,
        'C': 3,
    }
}

def getScore(other, self):
    return throws.index(self) + 1 + compare_table[other][self]

for line in f.readlines():
    [other, code] = line.strip().split(' ')
    # part 1
    part1 += getScore(other, decoder[code])
    # part 2
    self = '';
    if code == 'X':
        self = throws[(throws.index(other) + 2) % 3]
    elif code == 'Y':
        self = throws[throws.index(other)]
    elif code == 'Z':
        self = throws[(throws.index(other) + 1) % 3]
    part2 += getScore(other, self)

print('part1:', part1)
print('part2:', part2)