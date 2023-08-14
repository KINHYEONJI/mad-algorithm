n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
path = ['']*m
used = [0]*len(lst)

def abc(level):
    if level == m:
        for i in range(m):
            print(path[i],end = ' ')
        print()
        return
    for i in range(len(lst)):
        if level>0 and (path[level-1]> lst[i]):
            continue
        if used[i] == 1:
            continue
        path[level] = lst[i]
        used[i] += 1
        abc(level+1)
        used[i] -= 1
abc(0)