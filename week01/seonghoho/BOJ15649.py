n, m = map(int, input().split())
path = [0] * m          # m 자릿수
used = [0] * (n + 1)    # index n까지의 used 생성

def abc(level):
    if level == m:                  # m자릿수 도달하면 stop
        for i in range(m):
            print(path[i], end=' ')
        print()
        return
    for i in range(1, n + 1):       # used의 범위를 1~n으로 만듦
        if used[i] == 1:            # 사용한 번호는 건너띄기
            continue

        path[level] = i
        used[i] = 1
        abc(level + 1)
        used[i] = 0

abc(0)
