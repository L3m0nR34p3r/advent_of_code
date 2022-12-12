data = open('Day 8/input.txt', 'r',).read().splitlines()

# print (data)x

# I need to enter the line ahead and the line behind into memory,
# Then reference them in the checks to see if a tree is visable.
above = []


below = []
right = []
left = []

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
