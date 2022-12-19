# https://adventofcode.com/2022/day/4

f = open('day4.inputs.txt', 'r')

def process(input: str):
    pair = []
    for assignment in input.split(','):
        section = []
        for num in assignment.split('-'):
            section.append(int(num))
        pair.append(section)
    return pair

answer1 = 0
answer2 = 0
for line in f.readlines():
    [first, second] = process(line.strip())
    if (first[0] >= second[0] and first[1] <= second[1]) or \
       (second[0] >= first[0] and second[1] <= first[1]):
        answer1 += 1
    if (first[0] >= second[0] and first[0] <= second[1]) or \
       (first[1] >= second[0] and first[1] <= second[1]) or \
       (second[0] >= first[0] and second[0] <= first[1]) or \
       (second[1] >= first[0] and second[1] <= first[1]):
       answer2 += 1

print('part1:', answer1)
print('part2:', answer2)