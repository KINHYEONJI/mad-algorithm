N, M = map(int, input().split())
path = ['']*M
def abc(level):
    if level == M:
        for i in range(len(path)):
            print(path[i], end = ' ')
        print()
        return
    for i in range(N):
        if level > 0 and path[level-1] > i + 1:continue
        path[level] = i+1
        abc(level + 1)
abc(0)