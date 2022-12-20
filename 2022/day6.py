# https://adventofcode.com/2022/day/6

f = open('day6.inputs.txt', 'r')

buff = f.readline().strip()

def detect(buffer, marker_size):
    window = {}
    lead = 0
    trail = 0

    while lead < marker_size - 1:
        curr = buffer[lead]
        if curr not in window:
            window[curr] = 0
        window[curr] += 1
        lead += 1

    while lead < len(buffer):
        # add lead to window
        if buffer[lead] not in window:
            window[buffer[lead]] = 1
        else:
            window[buffer[lead]] += 1

        # check window
        if len(window) == marker_size:
            break

        # remove trail
        if window[buffer[trail]] == 1:
            del window[buffer[trail]]
        else:
            window[buffer[trail]] -= 1
        
        lead += 1
        trail += 1
    
    return lead + 1

print('part1:', detect(buff, 4))
print('part2:', detect(buff, 14))