import math
import sys

stack = []

x = sys.stdin.read()
for line in x.split('\n'):
    for n in line.split():
        if n:
            stack.append(math.sqrt(int(n)))

while len(stack) != 0:
    print('%.4f' % stack.pop())
