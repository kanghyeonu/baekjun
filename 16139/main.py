import sys

string = sys.stdin.readline().strip()
#keys = list(set(string))
q = int(sys.stdin.readline().strip())

for _ in range(q):
    char, s, e = sys.stdin.readline().split()
    s, e = int(s), int(e)
    if char == string[0]:
        dp = [0, 1]
    else:
        dp = [0, 0]
    for i in range(1, len(string)):
        if char == string[i]:
            dp.append(dp[i-1] + 1)
        else:
            dp.append(dp[i-1])
    print(dp[e+1] - dp[s])

