import sys, time, copy, random
sys.path.append("../useful_functions.py")
from useful_functions import *
startTime = time.time()

sudoku = []
i = 0
while i < 4:
    sudoku.append([0,0,0,0])
    i += 1

sudoku[random.randrange(0,4)][random.randrange(0,4)] = 1

printmap(greenmap(bluereplace(strmap(sudoku),'0')))

# print(green("count: " + str(i)))
timerstop(startTime)