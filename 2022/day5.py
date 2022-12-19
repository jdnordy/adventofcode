# https://adventofcode.com/2022/day/5
import copy

"""
[P]     [C]         [M]            
[D]     [P] [B]     [V] [S]        
[Q] [V] [R] [V]     [G] [B]        
[R] [W] [G] [J]     [T] [M]     [V]
[V] [Q] [Q] [F] [C] [N] [V]     [W]
[B] [Z] [Z] [H] [L] [P] [L] [J] [N]
[H] [D] [L] [D] [W] [R] [R] [P] [C]
[F] [L] [H] [R] [Z] [J] [J] [D] [D]
 1   2   3   4   5   6   7   8   9 
"""

ro_stacks = [
    [],
    ['F', 'H', 'B', 'V', 'R', 'Q', 'D', 'P'],
    ['L', 'D', 'Z', 'Q', 'W', 'V'],
    ['H', 'L', 'Z', 'Q', 'G', 'R', 'P', 'C'],
    ['R', 'D', 'H', 'F', 'J', 'V', 'B'],
    ['Z', 'W', 'L', 'C'],
    ['J', 'R', 'P', 'N', 'T', 'G', 'V', 'M'],
    ['J' ,'R', 'L', 'V', 'M', 'B', 'S'],
    ['D', 'P', 'J'],
    ['D', 'C', 'N', 'W', 'V']
]
stacks1 = copy.deepcopy(ro_stacks)
stacks2 = copy.deepcopy(ro_stacks)

f = open('day5.inputs.txt', 'r')

def process(raw_instruct: str):
    parts = raw_instruct.split()
    return {
        'move': int(parts[1]),
        'from': int(parts[3]),
        'to':   int(parts[5])
    }

for raw_instuct in f.readlines():
    instruct = process(raw_instuct.strip())

    # part1
    for i in range(instruct['move']):
        stacks1[instruct['to']].append(stacks1[instruct['from']].pop())

    # part 2
    group = []
    for i in range(instruct['move']):
        group.append(stacks2[instruct['from']].pop())

    group.reverse()
    
    for box in group:
        stacks2[instruct['to']].append(box)
          
def get_answer(stack_list):
    answer = ''
    for stack in stack_list:
        last_index = len(stack) - 1
        if last_index >= 0:
            answer += stack[len(stack) - 1]
    return answer

print('part1:', get_answer(stacks1))
print('part2:', get_answer(stacks2))
