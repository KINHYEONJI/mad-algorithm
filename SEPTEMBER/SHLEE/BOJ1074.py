N, r, c = map(int, input().split())

ans = 0  # 4분할 왼쪽 상단(2사분면) 값
while N > 0:
    k = 2 ** (N - 1)

    # 제 2 사분면
    if r < k and c < k:
        ans += 0

    # 제 1 사분면
    elif r < k and c >= k:
        ans += k * k
        c -= k

    # 제 3 사분면
    elif r >= k and c < k:
        ans += k * k * 2
        r -= k

    # 제 4 사분면
    else:
        ans += k * k * 3
        r -= k
        c -= k

    N -= 1

print(ans)
