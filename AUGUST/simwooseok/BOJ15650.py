N, M = map(int, input().split())
path = [''] *M
used = [0] * N
def abc(level):
    if level == M:
        for i in range(len(path)):
            print(path[i], end = ' ')
        print()
        return
    
    for i in range(N):
        if level > 0 and path[level-1] > i+1: continue
        if used[i] == 1: continue
        used[i] = 1
        path[level] = i + 1
        abc(level + 1)
        used[i] = 0
abc(0)