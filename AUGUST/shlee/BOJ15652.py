n, m = map(int, input().split())
path = [0] * m

def H(lev, start):
    if lev == m:
        for i in range(m):
            print(path[i], end=' ')
        print()
        return

    for i in range(start, n):
        path[lev] = i + 1
        H(lev + 1, i)

H(0, 0)
