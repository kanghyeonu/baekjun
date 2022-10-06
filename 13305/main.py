import sys

N = int(sys.stdin.readline())

distance = list(map(int, sys.stdin.readline().split()))
prices = list(map(int, sys.stdin.readline().split()))

price = prices[0]
answer = distance[0] * price
for i in range(1, N - 1):
    if price > prices[i]:
        price = prices[i]
    answer += price * distance[i]

print(answer)