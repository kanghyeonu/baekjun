case = int(input())
num = list(map(int, input().split()))
# [+, -, x, /] 개수
op = list(map(int, input().split()))

min_num = 1000000000
max_num = -1000000000

def dfs(depth, result, plus, minus, multi, div):
    global min_num, max_num
    if depth == case:
        min_num = min(min_num, result)
        max_num = max(max_num, result)
        return

    if plus > 0:
        dfs(depth + 1, result + num[depth], plus-1, minus, multi, div)
    if minus > 0:
        dfs(depth + 1, result - num[depth], plus, minus-1, multi, div)
    if multi > 0:
        dfs(depth + 1, result * num[depth], plus, minus, multi-1, div)
    if div > 0:
        dfs(depth + 1, int(result / num[depth]), plus, minus, multi , div-1)

dfs(1, num[0], op[0], op[1], op[2], op[3])

print(max_num)
print(min_num)

