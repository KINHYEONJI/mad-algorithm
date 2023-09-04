N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
path = [''] * M
used = [0] * len(arr)
def abc(level):
    if level == M:
        for i in range(len(path)):
            print(path[i], end = ' ')
        print()
        return
    
    for i in range(N):
        path[level] = arr[i]
        abc(level + 1)

abc(0)