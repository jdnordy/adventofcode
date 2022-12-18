# https://adventofcode.com/2022/day/3

f = open('day3.inputs.txt', 'r')

# part1
answer = 0;

# part2
answer2 = 0
count = 0
sack0 = set()
sack01 = set()

def convert(item):
    value = ord(item)
    # ASCII A to Z = 65 to 91
    if (value < 91):
        value -= 38
    # ASCII a to z = 97 to 123
    else:
        value -= 96
    return value

for line in f.readlines():
    # part1
    sack = line.strip()
    numItems = len(sack)
    sack1 = set()

    sharedItem = ''
    i = 0
    while i < numItems / 2:
        sack1.add(sack[i])
        i += 1

    while i < numItems:
        if sack[i] in sack1:
            sharedItem = sack[i]
            break
        i += 1

    answer += convert(sharedItem)

    # part2
    sack = line.strip()
    if count == 3:
        count = 0
        sack0 = set()
        sack01 = set()
    for item in sack:
        if count == 0:
            sack0.add(item)
        elif count == 1:
            if item in sack0:
                sack01.add(item)
        else:
            if item in sack01:
                answer2 += convert(item)
                break
    count += 1

print('part1: ', answer)
print('part2: ', answer2)