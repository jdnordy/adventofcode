# https://adventofcode.com/2022/day/1

f = open('day1.inputs.txt', 'r')

max = 0
current = 0

elfs = []

for rawline in f.readlines():
    calories = rawline.strip()
    if not calories:
        if current > max: max = current

        elfs.append(current)
        
        current = 0
    else:
        current += int(calories)

print(max)
elfs.sort(reverse=True)
print(elfs[0] + elfs[1] + elfs[2])