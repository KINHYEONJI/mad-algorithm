n = int(input())
matrix = [[0]*100 for _ in range(100)]
arr = [list(map(int, input().split())) for _ in range(n)]

for i in arr:
    for j in range(10):
        for k in range(10):
            matrix[i[0]+j][i[1]+k] = 1
cnt = 0
for i in matrix:
    for j in i:
        if j == 1:
            cnt += 1

print(cnt) 