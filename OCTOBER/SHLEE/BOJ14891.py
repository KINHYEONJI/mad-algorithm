arr = [list(map(int, input())) for _ in range(4)]
K = int(input())
for _ in range(K):
    num, dt = map(int, input().split())
    lst = [num - 1]
    for i in range(num - 1, 0, -1):
        if arr[i][6] != arr[i - 1][2]:
            lst.append(i - 1)
        else:
            break
    for i in range(num - 1, 3):
        if arr[i][2] != arr[i + 1][6]:
            lst.append(i + 1)
        else:
            break
