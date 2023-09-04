n, m = map(int, input().split())  # n: 브랜치, m: lev
path = [0] * m
used = [0] * n

def permutation(lev):
    if lev == m:
        for i in range(m):
            print(path[i],end=' ')
        print()
        return

    for i in range(n):
        if used[i] == 1: continue

        path[lev] = i + 1   # 1: 인덱스와 자연수의 차이
        used[i] = 1         # 사용 기록 남기기
        permutation(lev + 1)
        used[i] = 0         # 다시 초기화

permutation(0)
