num = int(input())

pos = 1
cnt = 1
line = -1

while True:
    pos += cnt
    cnt += 1
    line += 1
    if pos > num:
        cnt -= 1
        pos -= cnt
        break

if line % 2 == 0:
    print(str(cnt-(num-pos)) + '/' + str(1+(num-pos)))

else:
    print(str(1 + (num - pos))+ '/' + str(cnt - (num - pos)))