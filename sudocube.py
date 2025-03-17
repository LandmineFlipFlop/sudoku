import sys, time, copy, random
sys.path.append("../useful_functions.py")
from useful_functions import *
startTime = time.time()

options = {}

sudocube = []
i = 0
while i < 8:
    i2 = 0
    while i2 < 8:
        sudocube.append([[0, 0, 0, 0, 0, 0, 0, 0]])
    i += 1

sudocube[random.randrange(0, 8)][random.randrange(0, 8)] = 1

changeable = []
priority = []

def filterlines(pos):
    if not (pos[0],pos[1]) in options:
        if sudocube[pos[0]][pos[1]] == 0:
            options[(pos[0],pos[1])] = [1,2,3,4,5,6,7,8]
    i = 0
    while i < 8:
        if sudocube[pos[0]][i] in options[(pos[0], pos[1])]:
            options[(pos[0], pos[1])].remove(sudocube[pos[0]][i])
        i += 1

    i = 0
    while i < 8:
        if sudocube[i][pos[1]] in options[(pos[0], pos[1])]:
            options[(pos[0], pos[1])].remove(sudocube[i][pos[1]])
        i += 1

def checklocation(row,col,pos):
    if sudocube[row][col] in options[(pos[0], pos[1])]:
        options[(pos[0], pos[1])].remove(sudocube[row][col])

def filterbox(pos):
    translation = [((pos[0]%2)*-2)+1,((pos[1]%2)*-2)+1]
    # print(pos, translation, [pos[0]+translation[0],pos[1]+translation[1]])
    checklocation(pos[0] + translation[0], pos[1], pos)
    checklocation(pos[0], pos[1] + translation[1], pos)
    checklocation(pos[0] + translation[0], pos[1] + translation[1], pos)

def scangrid():
    y = 0
    while y < 8:
        x = 0
        while x < 8:
            if sudocube[y][x] == 0:
                filterlines([y, x])
                filterbox([y, x])
                if len(options[(y, x)]) < 4:
                    if len(options[(y, x)]) == 1:
                        priority.append((y, x))
                    else:
                        changeable.append((y, x))
            x += 1
        y += 1

def additem(pos, num):
    options.pop((pos[0], pos[1]))
    sudocube[pos[0]][pos[1]] = num

i2 = 0
while i2 < 15:
    changeable.clear()
    priority.clear()
    scangrid()
    if len(priority) != 0:
        tochange = priority[random.randrange(0,len(priority))]
        additem(tochange, options[(tochange[0],tochange[1])][0])
    else:
        if len(changeable) != 0:
            tochange = changeable[random.randrange(0,len(changeable))]
            additem(tochange, options[(tochange[0],tochange[1])][0])
    i2 += 1

for layer in sudocube:
    printmap(greenmap(bluereplace(strmap(layer), '0')))
    print()

print(yellow(options))
print(purple(changeable))

# print(green("count: " + str(i)))
timerstop(startTime)