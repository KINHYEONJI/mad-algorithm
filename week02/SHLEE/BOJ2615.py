import sys

input = sys.stdin.readline

arr = [[0] * 21] + [[0] + list(map(int, input().split())) + [0] for _ in range(19)] + [[0] * 21]
dt = [(0, 1), (1, 0), (1, 1), (-1, 1)]
for i in range(1, 20):
    for j in range(1, 20):
        if arr[i][j] != 0:
            for a, b in dt:
                if i + a * 4 > 21 or j + b * 4 > 21 or 1 > i + a * 4 or 1 > j + b * 4:
                    continue
                lst = [arr[i + a * k][j + b * k] for k in range(-1, 6)]
                if len(set(lst[1:6])) == 1 and len(set(lst[0:5])) == 2 and len(set(lst[1:7])) == 2:
                    print(arr[i][j])
                    print(i, j)
                    sys.exit()
print(0)
