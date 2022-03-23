case = int(input())
cnt = 0
for i in range(case):
    string = input()
    s = set()
    for j in range(len(string) - 1):
        if string[j] == string[j + 1]:
            s.add(string[j])
        else:
            if string[j+1] in s:
                cnt -= 1
                break
            else:
                s.add(string[j])
    cnt += 1

print(cnt)

