n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
path = [0] * m


def Pi(lev):
    if lev == m:
        for i in range(m):
            print(path[i], end=' ')
        print()
        return

    for i in range(n):
        path[lev] = lst[i]
        Pi(lev + 1)


Pi(0)
