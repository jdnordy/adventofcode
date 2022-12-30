# https://adventofcode.com/2022/day/10
from enum import Enum

f = open('day10.inputs.txt', 'r')

class Op(Enum):
    NOOP = 'noop'
    ADDX = 'addx'

class CPU:
    def __init__(self) -> None:
        self.__sum = 0
        self.__reg_x = 1
        self.__cycle = 0
        self.__crt = ''

    # def execute(self, op: Op):
    #     if op == Op.NOOP:
    #         pass
    #     elif op == Op.ADDX:
    #         pass

    def noop(self):
        self.cycle()

    def addx(self, value):
        self.cycle()
        self.cycle()
        self.__reg_x += value

    def cycle(self):
        self.__cycle += 1
        self.detect_signal()
        self.draw_crt()

    def detect_signal(self):
        mod_40 = self.__cycle % 40
        if mod_40 == 20:
            self.__sum += self.__cycle * self.__reg_x


    def draw_crt(self):
        mod_40 = self.__cycle % 40
        sprite_loc = {self.__reg_x, self.__reg_x - 1, self.__reg_x + 1}

        if mod_40 - 1 in sprite_loc:
            self.__crt += '#'
        else:
            self.__crt += '.'

        if mod_40 == 0:
            self.display_crt()

    def display_crt(self):
        print(self.__crt)
        self.__crt = ''

    def getSum(self):
        return self.__sum
    
    def getCycle(self):
        return self.__cycle

    def clear(self):
        self.__sum = 0
        self.__reg_x = 1
        self.__cycle = 0

cpu = CPU()

for line in f.readlines():
    instruct = line.strip().split()

    if len(instruct) == 1 and instruct[0] == Op.NOOP.value:
        cpu.noop()
    elif len(instruct) == 2 and instruct[0] == Op.ADDX.value:
        cpu.addx(int(instruct[1]))

print('part1:', cpu.getSum())