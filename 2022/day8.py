# https://adventofcode.com/2022/day/8

f = open('day8.inputs.txt', 'r')

class Tree:
    def __init__(self, height) -> None:
        self.height = height
        self.north = 0
        self.east = 0
        self.south = 0
        self.west = 0

grid = []

for i, line in enumerate(f.readlines()):
    row = []
    for j, tree_height in enumerate(line.strip()):
        tree = Tree(int(tree_height))

        # North
        if i > 0:
            north_tree = grid[i - 1][j]
            tree.north = max(north_tree.north, north_tree.height)

        # West
        if j > 0:
            west_tree = row[j - 1]
            tree.west = max(west_tree.west, west_tree.height)

        row.append(tree)

    grid.append(row)

height = len(grid)
width = len(grid[0])

for i in reversed(range(height)):
    for j in reversed(range(width)):
        tree = grid[i][j]

        # South
        if i < height - 1:
            south_tree = grid[i + 1][j]
            tree.south = max(south_tree.south, south_tree.height)

        # East
        if j < width - 1:
            east_tree = grid[i][j + 1]
            tree.east = max(east_tree.east, east_tree.height)

def countVisible(grid):
    width = len(grid[0])
    height = len(grid)
    visible = height * 2 + width * 2 - 4

    for i in range(1, height - 1):
        for j in range(1, width - 1):
            tree = grid[i][j]
            if tree.north < tree.height or \
                tree.east < tree.height or \
                tree.south < tree.height or \
                tree.west < tree.height:

                visible += 1
            
    return visible

def findMaxVisibleTrees(grid):
    max_score = 0
    height = len(grid)
    width = len(grid[0])

    for i in range(height):
        for j in range(width):
            tree = grid[i][j]

            k = i
            l = j
            # North
            north = 0
            while k > 0:
                north += 1
                north_tree = grid[k - 1][l]
                if tree.height <= north_tree.height:
                    break
                k -= 1
            
            k = i
            l = j
            # East
            east = 0
            while l < width - 1:
                east += 1
                east_tree = grid[k][l + 1]
                if tree.height <= east_tree.height:
                    break
                l += 1

            k = i
            l = j
            # South
            south = 0
            while k < height - 1:
                south += 1
                south_tree = grid[k + 1][l]
                if tree.height <= south_tree.height:
                    break
                k += 1

            k = i
            l = j
            # West
            west = 0
            while l > 0:
                west += 1
                west_tree = grid[k][l - 1]
                if tree.height <= west_tree.height:
                    break
                l -= 1
            
            max_score = max(max_score, north * east * south * west)

    return max_score

print('part1:', countVisible(grid))
print('part2:', findMaxVisibleTrees(grid))