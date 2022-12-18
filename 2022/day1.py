# https://adventofcode.com/2022/day/1

f = open('day1.inputs.txt', 'r')

max = 0;
current = 0;

for rawline in f.readlines():
    calories = rawline.strip()
    if not calories:
        if current > max: max = current
        current = 0
    else:
        current += int(calories)

print(max)