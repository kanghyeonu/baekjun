import sys
from collections import deque

n = int(sys.stdin.readline().strip())
melody = deque(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline().strip())
dream_melody = deque(list(map(int, sys.stdin.readline().split())))

