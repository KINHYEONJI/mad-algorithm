import sys
input = sys.stdin.readline
n,k,b = map(int,input().split())
arr = [1]*n
for _ in range(b): arr[int(input())-1] = 0
cnt = 0
for i in range(k): cnt += arr[i]
res = []
for i in range(n-k):
    cnt += arr[i+k]
    cnt -= arr[i]
    res.append(k-cnt)
print(min(res))