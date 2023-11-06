import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
dic = {}
for i in arr:
    for j in arr:
        if dic.get(i+j,0) == 0:dic[i+j] = 1
ans = 0
for i in arr:
    for j in arr:
        if dic.get(i-j,0): ans = max(ans,i)
print(ans)