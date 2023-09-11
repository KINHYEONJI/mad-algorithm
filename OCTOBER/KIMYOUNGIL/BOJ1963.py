from collections import deque

check = [0]*10000
for i in range(2,100):
    if check[i] == 1: continue
    for j in range(2*i,10000,i): check[j] = 1

prime = []
for i in range(2,10000):
    if check[i] == 0: prime.append(i)

def bfs(x):
    q = deque([[x,0]])
    visited = [0]*10000
    visited[x] = 1
    while q:
        p,c = q.popleft()
        if p == e: return print(c)

        for i in range(1,10):
            n1 = p%1000 + 1000*i
            if visited[n1] == 0:
                visited[n1] = 1
                if n1 in prime: q.append([n1,c+1])
                    
        for i in range(10):
            n2 = (p//1000)*1000 + p%100 + 100*i
            if visited[n2] == 0:
                visited[n2] = 1
                if n2 in prime: q.append([n2,c+1])
                    
        for i in range(10):
            n3 = (p//100)*100 + p%10 + 10*i
            if visited[n3] == 0:
                visited[n3] = 1
                if n3 in prime: q.append([n3,c+1])
        
        for i in range(1,10,2):
            n4 = (p//10)*10 + i
            if visited[n4] == 0:
                visited[n4] = 1
                if n4 in prime: q.append([n4,c+1])

    return print('Impossible')

for _ in range(int(input())): s,e = map(int,input().split()); bfs(s)