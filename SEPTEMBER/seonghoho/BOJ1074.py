N, r, c = map(int, input().split())
# 사분면으로 나누어 while문 실행
# 찾으려는 좌표 값이 2 **(N-1) 한 값보다 큰지, 작은지 비교해서 사분면 위치 파악
ans = 0
while N > 0:
    a = 2 ** (N - 1)

    if r < a and c < a:  # 2사분면
        ans += 0

    elif r < a and a <= c:  # 1사분면
        ans += a * a
        c -= a

    elif c < a and a <= r:  # 3사분면
        ans += a * a * 2
        r -= a
    elif r >= a and c >= a:  # 4사분면
        ans += a * a * 3
        c -= a
        r -= a

    N -= 1
print(ans)
