data = open('Day 8/input.txt', 'r',).read().splitlines()

# I need to enter the line ahead and the line behind into memory,
# Then reference them in the checks to see if a tree is visable.

def fistline():
    for line in data:
        line.strip
        break
    return line

def is_visible(tree):
    for line in data:
        line.strip
        prev_line = line
        for x, tree in enumerate(line):
            print("I don't like where this is going.....")


grid = [list(map(int, line)) for line in data]
t = 0

for r in range(len(grid)):
    for c in range(len(grid[r])):
        k = grid[r][c]
        if all(grid[r][x] < k for x in range(c)) or all(grid[r][x] < k for x in range(c+1, len(grid[r]))) or all(grid[x][c]<k for x in range(r)) or all (grid[x][c]<k for x in range(r +1, len(grid))):
            t +=1
print (t)