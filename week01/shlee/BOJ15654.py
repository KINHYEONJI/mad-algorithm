n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
path = [0] * m
used = [0] * n


def P(lev):
    if lev == m:
        for i in range(m):
            print(path[i], end=' ')
        print()
        return

    for i in range(n):
        if used[i] == 1: continue
        path[lev] = lst[i]
        used[i] = 1
        P(lev + 1)
        used[i] = 0


P(0)
