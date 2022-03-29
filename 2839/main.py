suger = int(input())
cnt = 0
# 3kg 5kg 봉다리
while True:
    if suger < 0:
        print(-1)
        break
    elif suger % 5 == 0:
        print(cnt + suger // 5)
        break
    suger -= 3
    cnt += 1