from collections import deque
n,k = map(int,input().split())

arr = [0]*100001
def bfs(x):
    q = deque()
    q.append(x)
    while q:
        a = q.popleft()
        if a == k:
            print(arr[a])
            break
        for i in [a-1,a+1,2*a]:
            if 0 <= i <= 100000 and arr[i] == 0:
                arr[i] = arr[a] + 1
                q.append(i)
bfs(n)