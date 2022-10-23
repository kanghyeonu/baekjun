from collections import deque
import sys

while True:
    string = sys.stdin.readline()
    if string[0] == '.':
        break
    q = deque()
    for char in string:
        if char == '(' or char == '[':
            q.append(char)

        elif char == ')' or char == ']':
            if len(q) > 0:
                pop = q.pop()
            else:
                q.append(')]')
                break
            if (char == ')' and pop == '(') or (char == ']' and pop == '['):
                continue
            else:
                q.append(')]')
                break
    if q:
        print('no')
    else:
        print('yes')