import sys

students = set([i for i in range(1, 31)])

for _ in range(28):
    students.remove(int(sys.stdin.readline().strip()))

ans = list(students)
print(min(ans))
print(max(ans))