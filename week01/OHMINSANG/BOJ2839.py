n = int(input())
cnt = 0
# 무한 루프 형성
while 1:
    if n % 5 == 0:
        cnt += n // 5
        break
    # 입력값이 5로 안나누어 떨어지면 -3 하고 카운트 +1
    n -= 3
    cnt += 1
    # n이 0보다 작아질경우 -1 고정
    if n < 0:
        cnt = -1
        break
print(cnt)
