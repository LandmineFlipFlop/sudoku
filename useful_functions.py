import sys, time, math
sys.path.append("/useful_functions.py")
# from useful_functions import *


def clamp(value, minimum, maximum):
    return max(minimum, min(value, maximum))


def checkletter(letter, startx, starty, array):

    maxX = len(array[starty]) - 1
    maxY = len(array) - 1

    #compares x value to itself clamped between the min and max
    if not clamp(startx , 0, maxX) == startx:
        return False

    # compares y value to itself clamped between the min and max
    if not clamp(starty, 0, maxY) == starty:
        return False

    #checks if the charecter matches the one that's actually there
    if not array[starty][startx] == letter:
        return False

    return True


class Colors:
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    DARKCYAN = "\033[36m"
    GREEN = '\033[92m'
    PURPLE = "\033[35m"
    MAGENTA = '\033[95m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    WHITE = "\033[37m"
    GREY = "\033[30m"
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    def blue(text):
        return Colors.BLUE + text + Colors.ENDC
    def cyan(text):
        return Colors.CYAN + text + Colors.ENDC
    def green(text):
        return Colors.GREEN + text + Colors.ENDC
    def purple(text):
        return Colors.PURPLE + text + Colors.ENDC
    def red(text):
        return Colors.RED + text + Colors.ENDC
    def yellow(text):
        return Colors.YELLOW + text + Colors.ENDC
    def darkcyan(text):
        return Colors.DARKCYAN + text + Colors.ENDC
    def magenta(text):
        return Colors.MAGENTA + text + Colors.ENDC
    def black(text):
        return Colors.BLACK + text + Colors.ENDC
    def grey(text):
        return Colors.GREY + text + Colors.ENDC
    def bold(text):
        return Colors.BOLD + text + Colors.ENDC
    def underline(text):
        return Colors.UNDERLINE + text + Colors.ENDC


def blue(text):
    return Colors.blue(str(text))
def red(text):
    return Colors.red(str(text))
def green(text):
    return Colors.green(str(text))
def cyan(text):
    return Colors.cyan(str(text))
def darkcyan(text):
    return Colors.darkcyan(str(text))
def purple(text):
    return Colors.purple(str(text))
def yellow(text):
    return Colors.yellow(str(text))
def magenta(text):
    return Colors.magenta(str(text))
def black(text):
    return Colors.black(str(text))
def grey(text):
    return Colors.grey(str(text))
def bold(text):
    return Colors.bold(str(text))
def underline(text):
    return Colors.underline(str(text))


def timerstop(start_time):
    end_time = time.time()

    execution_time_sec = (end_time - start_time)
    execution_time_ms = execution_time_sec * 1_000
    execution_time_us = execution_time_sec * 1_000_000

    print()
    print(darkcyan("Execution time:"))
    print(f"  - {execution_time_sec:.3f} sec")
    print(f"  - {execution_time_ms:.2f} ms")
    print(f"  - {math.ceil(execution_time_us)} µs")


def outofbounds(pos, max):
    if pos[0] > max[0] or pos[1] > max[1] or pos[0] < 0 or pos[1] < 0:
        return True
    return False


def iseven(num):
    return num % 2 == 0


def printmap(map):
    for row in map:
        print("".join(row))

def strmap(map):
    revised = []
    for row in map:
        revised.append([])
        for col in row:
            revised[len(revised) - 1].append(str(col))
    return revised
def bluemap(map):
    revised = []
    for row in map:
        revised.append([])
        for col in row:
            revised[len(revised) - 1].append(blue(col))
    return revised
def redmap(map):
    revised = []
    for row in map:
        revised.append([])
        for col in row:
            revised[len(revised) - 1].append(red(col))
    return revised
def greenmap(map):
    revised = []
    for row in map:
        revised.append([])
        for col in row:
            revised[len(revised) - 1].append(green(col))
    return revised
def purplemap(map):
    revised = []
    for row in map:
        revised.append([])
        for col in row:
            revised[len(revised) - 1].append(purple(col))
    return revised
def magentamap(map):
    revised = []
    for row in map:
        revised.append([])
        for col in row:
            revised[len(revised) - 1].append(magenta(col))
    return revised
def cyanmap(map):
    revised = []
    for row in map:
        revised.append([])
        for col in row:
            revised[len(revised) - 1].append(cyan(col))
    return revised
def darkcyanmap(map):
    revised = []
    for row in map:
        revised.append([])
        for col in row:
            revised[len(revised) - 1].append(darkcyan(col))
    return revised
def yellowmap(map):
    revised = []
    for row in map:
        revised.append([])
        for col in row:
            revised[len(revised) - 1].append(yellow(col))
    return revised

def bluereplace(map, charecter):
    revised = []
    for row in map:
        revised.append([])
        for col in row:
            if col == charecter:
                revised[len(revised) - 1].append(blue(col))
            else:
                revised[len(revised) - 1].append(col)
    return revised
def redreplace(map, charecter):
    revised = []
    for row in map:
        revised.append([])
        for col in row:
            if col == charecter:
                revised[len(revised) - 1].append(red(col))
            else:
                revised[len(revised) - 1].append(col)
    return revised
def greenreplace(map, charecter):
    revised = []
    for row in map:
        revised.append([])
        for col in row:
            if col == charecter:
                revised[len(revised) - 1].append(green(col))
            else:
                revised[len(revised) - 1].append(col)
    return revised
def purplereplace(map, charecter):
    revised = []
    for row in map:
        revised.append([])
        for col in row:
            if col == charecter:
                revised[len(revised) - 1].append(purple(col))
            else:
                revised[len(revised) - 1].append(col)
    return revised
def magentareplace(map, charecter):
    revised = []
    for row in map:
        revised.append([])
        for col in row:
            if col == charecter:
                revised[len(revised) - 1].append(magenta(col))
            else:
                revised[len(revised) - 1].append(col)
    return revised
def cyanreplace(map, charecter):
    revised = []
    for row in map:
        revised.append([])
        for col in row:
            if col == charecter:
                revised[len(revised) - 1].append(cyan(col))
            else:
                revised[len(revised) - 1].append(col)
    return revised
def darkcyanreplace(map, charecter):
    revised = []
    for row in map:
        revised.append([])
        for col in row:
            if col == charecter:
                revised[len(revised) - 1].append(darkcyan(col))
            else:
                revised[len(revised) - 1].append(col)
    return revised
def yellowreplace(map, charecter):
    revised = []
    for row in map:
        revised.append([])
        for col in row:
            if col == charecter:
                revised[len(revised) - 1].append(yellow(col))
            else:
                revised[len(revised) - 1].append(col)
    return revised