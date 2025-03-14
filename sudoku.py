import sys, time, copy
sys.path.append("../useful_functions.py")
from useful_functions import *
with open ('_data/test_data', 'r') as casefile:
    lines = casefile.read().splitlines()
startTime = time.time()
count = 0





print(Colors.green("count: " + str(count)))
timerstop(startTime)