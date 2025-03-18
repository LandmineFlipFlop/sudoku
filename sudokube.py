import sys, time, copy, random
sys.path.append("../useful_functions.py")
from useful_functions import *
startTime = time.time()

options = {}

sudokube = [[],[],[],[],[],[],[],[]]
i = 0
while i < 8:
    i2 = 0
    while i2 < 8:
        sudokube[i].append([0,0,0,0,0,0,0,0])
        i2 += 1
    i += 1

sudokube[random.randrange(0, 8)][random.randrange(0, 8)][random.randrange(0, 8)] = 1

changeable = []
priority = []

def filterlines(pos):
    if not (pos[0],pos[1],pos[2]) in options:
        if sudokube[pos[0]][pos[1]][pos[2]] == 0:
            options[(pos[0],pos[1],pos[2])] = [1,2,3,4,5,6,7,8]
    i = 0
    while i < 8:
        if sudokube[pos[0]][pos[1]][i] in options[(pos[0], pos[1], pos[2])]:
            options[(pos[0], pos[1], pos[2])].remove(sudokube[pos[0]][pos[1]][i])
        i += 1
    i = 0
    while i < 8:
        if sudokube[pos[0]][i][pos[2]] in options[(pos[0], pos[1], pos[2])]:
            options[(pos[0], pos[1], pos[2])].remove(sudokube[pos[0]][i][pos[2]])
        i += 1
    i = 0
    while i < 8:
        if sudokube[i][pos[1]][pos[2]] in options[(pos[0], pos[1], pos[2])]:
            options[(pos[0], pos[1], pos[2])].remove(sudokube[i][pos[1]][pos[2]])
        i += 1

def checklocation(row,col,layer,pos):
    if sudokube[row][col][layer] in options[(pos[0], pos[1], pos[2])]:
        options[(pos[0], pos[1], pos[2])].remove(sudokube[row][col][layer])

def filterbox(pos):
    translation = [((pos[0]%2)*-2)+1, ((pos[1]%2)*-2)+1, ((pos[2]%2)*-2)+1]
    checklocation(pos[0] + translation[0], pos[1], pos[2], pos)
    checklocation(pos[0], pos[1] + translation[1], pos[2], pos)
    checklocation(pos[0] + translation[0], pos[1] + translation[1], pos[2], pos)

    checklocation(pos[0], pos[1], pos[2] + translation[2], pos)
    checklocation(pos[0] + translation[0], pos[1], pos[2] + translation[2], pos)
    checklocation(pos[0], pos[1] + translation[1], pos[2] + translation[2], pos)
    checklocation(pos[0] + translation[0], pos[1] + translation[1], pos[2] + translation[2], pos)


def scangrid():
    y = 0
    while y < 8:
        x = 0
        while x < 8:
            z = 0
            while z < 8:
                if sudokube[y][x][z] == 0:
                    filterlines([y, x, z])
                    filterbox([y, x, z])
                    if len(options[(y, x, z)]) < 8:
                        if len(options[(y, x, z)]) == 1:
                            priority.append((y, x, z))
                        else:
                            changeable.append((y, x, z))
                z += 1
            x += 1
        y += 1


def additem(pos, num):
    options.pop((pos[0], pos[1], pos[2]))
    sudokube[pos[0]][pos[1]][pos[2]] = num


def findshortest():
    i = 0
    shortest = 8
    while i < len(changeable) - 1:
        if len(options[changeable[i]]) < shortest:
            if len(options[changeable[i]]) != 0:
                shortest = len(options[changeable[i]])
        i += 1

    for item in changeable:
        if len(options[item]) == shortest:
            priority.append(item)

i2 = 0
while i2 < 511:
    changeable.clear()
    priority.clear()
    scangrid()
    findshortest()
    # print(changeable)
    if len(priority) != 0:
        tochange = priority[random.randrange(0,len(priority))]
        additem(tochange, options[(tochange[0],tochange[1],tochange[2])][0])
    else:
        if len(changeable) != 0:
            tochange = changeable[random.randrange(0,len(changeable) )]
            # tochange = findshortest()
            additem(tochange, options[ (tochange[0],tochange[1],tochange[2]) ][0])
    i2 += 1

    for layer in sudokube:
        printmap(greenmap(redreplace(strmap(layer), '0')))
        print()
    print(yellow(round(((i2 + 2)/512)*100))+'%')
    print(blue('----------------------------------------'))



for layer in sudokube:
    printmap(greenmap(bluereplace(strmap(layer), '0')))
    print()

print(yellow(options))
print(purple(changeable))

timerstop(startTime)