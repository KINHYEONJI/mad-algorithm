n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
path = [0] * m


def C(lev, start):
    if lev == m:
        for i in range(m):
            print(path[i], end=' ')
        print()
        return

    for i in range(start, n):
        path[lev] = lst[i]
        C(lev + 1, i + 1)


C(0, 0)
