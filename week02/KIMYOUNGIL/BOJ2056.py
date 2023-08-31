import sys
input = sys.stdin.readline

n = int(input())
time,arr = [0]*(n+1), [[] for _ in range(n+1)]

for i in range(1,n+1):
    lst = list(map(int,input().split()))
    time[i] = lst[0]
    for j in range(2,lst[1]+2): arr[i].append(lst[j])
    
for i in range(2,n+1):
    plus = time[i]
    for j in arr[i]:
        if time[i] < plus + time[j]: time[i] = time[j] + plus

print(max(time))