from collections import deque
n,k = map(int,input().split())

if n >= k:
    print(n-k)
    for i in range(n,k-1,-1):
        print(i,end=" ")
else:
    q = deque([n])
    visited = [0]*100001
    visited[n] = 1
    path = [0]*100001
    while q:
        p = q.popleft()
        if p == k:
            print(visited[p]-1)
            lst = [p]
            idx = p
            while idx != n:
                lst.append(path[idx])
                idx = path[idx]
            lst.reverse()
            print(*lst)
            break

        if 0 <= p*2 <= 100000:
            if visited[2*p] == 0:
                visited[p*2] = visited[p] + 1 
                path[2*p] = p
                q.append(p*2)

        if 0 <= p+1 <= 100000:
            if visited[p+1] == 0:
                visited[p+1] = visited[p] + 1
                path[p+1] = p
                q.append(p+1)
        
        if 0 <= p-1 <= 100000:
            if visited[p-1] == 0:
                visited[p-1] = visited[p] + 1
                path[p-1] = p
                q.append(p-1)