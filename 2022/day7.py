# https://adventofcode.com/2022/day/7

f = open('day7.inputs.txt', 'r')

FILE = 'FILE'
DIR = 'DIR'

class File:
    def __init__(self, name, size: int) -> None:
        self.type = FILE
        self.name = name
        self.__size = size

    def getSize(self):
        return self.__size

class Dir:
    def __init__(self, name) -> None:
        self.type = DIR
        self.name = name
        self.__size = 0
        self.__contents = {
            '.': self,
            '..': self,
        }
    
    def addDir(self, contentName, content):
        content.add('..', self)
        self.__contents[contentName] = content

    def add(self, contentName, content):
        self.__contents[contentName] = content

    def get(self, contentName):
        return self.__contents[contentName]

    def getContents(self):
        return self.__contents

    def getSize(self):
        if self.__size == 0:
            for name, content in self.__contents.items():
                if name != '.' and name != '..':
                    self.__size += content.getSize()

        return self.__size

    def getTotalSizeDirsSub100K(self, acc = { 'total': 0 }):
        for name, content in self.__contents.items():
            if content.type == DIR and name != '.' and name != '..':
                content.getTotalSizeDirsSub100K(acc)
        
        if self.getSize() <= 100000:
            acc['total'] += self.getSize()

        return acc['total']

    def findSmallestDirOver(self, over, acc = { 'over': 70000000 }):
        # search sub directories
        for name, content in self.__contents.items():
            if content.type == DIR and name != '.' and name != '..':
                    content.findSmallestDirOver(over, acc)
            
        if self.getSize() >= over and self.getSize() < acc['over']: 
            acc['over'] = self.getSize()
        
        return acc['over']

root = None
cur = None

lines = f.readlines()
def getLine(num, lines_array):
    return lines_array[num].strip().split(' ')

for i in range(len(lines)):
    line = getLine(i, lines)

    # handle cd command
    if line[0] == '$' and line[1] == 'cd':
        if not cur:
            root = Dir('/')
            cur = root
        else:
            cur = cur.get(line[2])
    
    # handle ls command
    elif line[0] == '$' and line[1] == 'ls':
        ls_dir = cur

        # check if list current dir or sub dir
        if len(line) == 3:
            ls_dir = cur.get(line[2])

        # process ls command
        while i + 1 < len(lines) and getLine(i + 1, lines)[0] != '$':
            i += 1
            line = getLine(i, lines)
            if line[0] == 'dir':
                ls_dir.addDir(line[1], Dir(line[1]))
            else:
                ls_dir.add(line[1], File(line[1], int(line[0])))

print('part1:', root.getTotalSizeDirsSub100K())

def getMinAmountToDelete(used, min = 30000000, max = 70000000):
    amount = used + min - max

    if amount < 0:
        return 0
    
    return amount

print('part2:', root.findSmallestDirOver(getMinAmountToDelete(root.getSize())))
