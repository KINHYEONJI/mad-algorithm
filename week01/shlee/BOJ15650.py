n, m = map(int, input().split())
path = [0] * m

def combi(lev, start):
    if lev == m:
        for i in range(m):
            print(path[i], end=' ')
        print()
        return

    for i in range(start, n):
        path[lev] = i + 1
        combi(lev + 1, i + 1)

combi(0, 0)
