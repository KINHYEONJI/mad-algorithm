N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr2 = sorted(arr)
path = ['']*M
used = [0]*len(arr)
def abc(level):
    if level == M:
        for i in range(len(path)):
            print(path[i],end=' ')
        print()
        return
    for i in range(len(arr)):
        if level>0 and path[level -1] > arr2[i] : continue
        if used[i]== 1:continue
        used[i]=1
        path[level]=arr2[i]
        abc(level + 1)
        used[i]=0
abc(0)