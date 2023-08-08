n = int(input())
cnts = []

for i in range(n // 3+1):
    for j in range(n // 5+1):
        if 3 * i + 5 * j == n:  # 3의배,5의배수로 순서쌍 찾기
            cnt = i+j
            cnts.append(cnt)

if not cnts:            # 빈 배열(순서쌍이 없을 떄)이면 -1 출력
    print(-1)
else:
    print(min(cnts))