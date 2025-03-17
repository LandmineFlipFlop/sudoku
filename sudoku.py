import sys, time, copy, random
sys.path.append("../useful_functions.py")
from useful_functions import *
startTime = time.time()

options = {}

sudoku = []
i = 0
while i < 4:
    sudoku.append([0,0,0,0])
    i += 1

sudoku[random.randrange(0,4)][random.randrange(0,4)] = 1

changeable = []

def filterlines(pos):
    if not (pos[0],pos[1]) in options:
        if sudoku[pos[0]][pos[1]] == 0:
            options[(pos[0],pos[1])] = [1,2,3,4]
    i = 0
    while i < 4:
        if sudoku[pos[0]][i] in options[(pos[0],pos[1])]:
            options[(pos[0], pos[1])].remove(sudoku[pos[0]][i])
        i += 1

    i = 0
    while i < 4:
        if sudoku[i][pos[1]] in options[(pos[0], pos[1])]:
            options[(pos[0], pos[1])].remove(sudoku[i][pos[1]])
        i += 1

def scangrid():
    row = 0
    while row < 4:
        col = 0
        while col < 4:
            if sudoku[row][col] == 0:
                filterlines([row,col])
            col += 1
        row += 1

def additem(pos, num):
    options.pop((pos[0], pos[1]))
    sudoku[pos[0]][pos[1]] = num


scangrid()



printmap(greenmap(bluereplace(strmap(sudoku),'0')))
print(yellow(options))

# print(green("count: " + str(i)))
timerstop(startTime)