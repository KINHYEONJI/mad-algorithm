import sys, heapq
input = sys.stdin.readline

dir = [[0,1],[0,-1],[1,0],[-1,0]]

def dik(y,x):
    q = []
    heapq.heappush(q, (arr[y][x], [y,x]))
    result[y][x] = arr[y][x]
    while q:
        cost, [r,c] = heapq.heappop(q)

        if [r,c] == [n-1,n-1]:
            return print(f'Problem {tc}: {cost}')
        
        for i in range(4):
            dy = r + dir[i][0]
            dx = c + dir[i][1]
            if dy < 0 or dx < 0 or dy > n-1 or dx > n-1: continue
            price = cost + arr[dy][dx]
            if price < result[dy][dx]:
                result[dy][dx] = price
                heapq.heappush(q, (price, [dy,dx]))

tc = 1
while 1:
    n = int(input())
    if n == 0: break
    arr = [list(map(int,input().split())) for _ in range(n)]
    result = [[21e8]*n for _ in range(n)]
    dik(0,0)
    tc += 1