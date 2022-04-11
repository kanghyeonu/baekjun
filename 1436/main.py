num = int(input())

cnt = 0
doom = 665

while cnt != num:
    doom += 1
    if '666' in str(doom):
        cnt += 1

print(doom)