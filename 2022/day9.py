# https://adventofcode.com/2022/day/9
from enum import Enum

f = open('day9.inputs.txt', 'r')

class Direction(Enum):
    UP = 'U'
    RIGHT = 'R'
    DOWN = 'D'
    LEFT = 'L'

class Grid:
    def __init__(self) -> None:
        self.__grid = [['s']]

    def mark(self, row_index, col_index, mark = '#'):
        if self.height() > row_index and \
           self.width() > col_index and \
           self.__grid[row_index][col_index] == '.':

            self.__grid[row_index][col_index] = mark

    def countMarks(self):
        count = 0
        for row in self.__grid:
            for space in row:
                if space != '.':
                    count += 1

        return count

    def height(self):
        return len(self.__grid)

    def width(self):
        return len(self.__grid[0])

    def expandUp(self):
        row = []
        for i in range(self.width()):
            row.append('.')
        self.__grid.insert(0, row)

    def expandRight(self):
        for row in self.__grid:
            row.append('.')

    def expandDown(self):
        row = []
        for i in range(self.width()):
            row.append('.')
        self.__grid.append(row)

    def expandLeft(self):
        for row in self.__grid:
            row.insert(0, '.')

    def print(self):
        for row in self.__grid:
            print(''.join(row))

class Node():
    def __init__(self, row = 0, col = 0, prev = None, next = None, name = '') -> None:
        self.row = row
        self.col = col
        self.prev = prev
        self.next = next
        self.name = name

    def move(self):
        # need to move up
        if self.row - self.prev.row > 1:
            self.row -= 1

            diff = self.col - self.prev.col
            if diff > 0:
                self.col -= 1
            elif diff < 0:
                self.col += 1
        # need to move right
        elif self.prev.col - self.col > 1:
            self.col += 1

            diff = self.row - self.prev.row
            if diff > 0:
                self.row -= 1
            elif diff < 0:
                self.row += 1
        # need to move down
        elif self.prev.row - self.row > 1:
            self.row  += 1

            diff = self.col - self.prev.col
            if diff > 0:
                self.col -= 1
            elif diff < 0:
                self.col += 1

        # need to move left
        elif self.col - self.prev.col > 1:
            self.col -= 1

            diff = self.row - self.prev.row
            if diff > 0:
                self.row -= 1
            elif diff < 0:
                self.row += 1

        if self.next:
            self.next.move()

    def moveHead(self, direction: Direction):
        if direction == Direction.UP:
            self.row -= 1
        elif direction == Direction.RIGHT:
            self.col += 1
        elif direction == Direction.DOWN:
            self.row += 1
        elif direction == Direction.LEFT:
            self.col -= 1
                
        if self.next:
            self.next.move()
    
    def moveSame(self, direction: Direction):
        if direction == Direction.UP:
            self.row -= 1
        elif direction == Direction.RIGHT:
            self.col += 1
        elif direction == Direction.DOWN:
            self.row += 1
        elif direction == Direction.LEFT:
            self.col -= 1
        
        if self.next:
            self.next.moveSame(direction)

    def length(self):
        if not self.next:
            return 1

        return 1 + self.next.length()

def buildRope(head, length):
    tail = None
    curr = head
    for i in range(length):
        curr.next = Node(0, 0, curr, name=str(i + 1))
        curr = curr.next
        tail = curr

    return tail

### PART 1 ###
grid = Grid()
head = Node(name='head')
tail = buildRope(head, 1)

grid2 = Grid()
head2 = Node(name='head')
tail2 = buildRope(head2, 9)

for line in f.readlines():
    # movement instructions
    m = line.strip().split()
    direction = Direction(m[0])
    n = int(m[1])

    for i in range(n):
        # MOVE UP
        if direction == Direction.UP:
            if head.row == 0:
                grid.expandUp()
                head.moveSame(Direction.DOWN)

            head.moveHead(Direction.UP)

            if head2.row == 0:
                grid2.expandUp()
                head2.moveSame(Direction.DOWN)

            head2.moveHead(Direction.UP)

        # MOVE RIGHT
        if direction == Direction.RIGHT:
            if head.col == grid.width() - 1:
                grid.expandRight()

            head.moveHead(Direction.RIGHT)

            if head2.col == grid2.width() - 1:
                grid2.expandRight()

            head2.moveHead(Direction.RIGHT)

        # MOVE DOWN
        if direction == Direction.DOWN:
            if head.row == grid.height() - 1:
                grid.expandDown()

            head.moveHead(Direction.DOWN)

            if head2.row == grid2.height() - 1:
                grid2.expandDown()

            head2.moveHead(Direction.DOWN)

        # MOVE LEFT
        if direction == Direction.LEFT:
            if head.col == 0:
                grid.expandLeft()
                head.moveSame(Direction.RIGHT)

            head.moveHead(Direction.LEFT)

            if head2.col == 0:
                grid2.expandLeft()
                head2.moveSame(Direction.RIGHT)

            head2.moveHead(Direction.LEFT)

        grid.mark(tail.row, tail.col)
        grid2.mark(tail2.row, tail2.col)

print('part1:', grid.countMarks())
print('print2:', grid2.countMarks())