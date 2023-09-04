n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
path = [''] * m


def abc(level):
    if level == m:
        for i in range(m):
            print(path[i], end=' ')
        print()
        return
    for i in lst:
        path[level] = i
        abc(level + 1)


abc(0)
