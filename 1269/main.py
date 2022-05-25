import sys

sys.stdin.readline()

A = set(map(int, sys.stdin.readline().split()))
B = set(map(int, sys.stdin.readline().split()))

A_ = A - B
B_ = B - A

print(len(A_ | B_))