arr = [[0] * 21] + [[0] + list(map(int, input().split())) + [0] for i in range(18)] + [[0] * 21]
used = [[0]*21 for _ in range(21)]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]
dx = [1, 1, 1, 0, -1, -1, -1, 0]

for y in range(21):
    for x in range(21):
        if arr[y][x] !=0:
            for i in range(8):
                ny = y +dy[i]
                nx = x +dx[i]
                if 0 <= ny <21 and 1<= nx<21:

for i in arr:
    print(*i)
