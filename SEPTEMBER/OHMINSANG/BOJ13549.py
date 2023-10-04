import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

n, k = map(int, input().split())

if n == k:
    print(0)

elif n > k:
    print(n - k)

elif n == 1 and k == 2:
    print(0)
# 위에 조건문은 전부 예외 처리

# n < k 일때
else:
    # 만약 n이 1이면 n=2로 바꾼 뒤 bfs 시행
    if n == 1:
        n = 2
    used = [0] * (2 * k)
    chk = 0
    q = deque()
    q.append(n)
    while q:
        n = q.popleft()
        dx = [n, -1, 1]
        for i in range(3):
            if i == 0:
                nn = n + dx[i]
                if 0 <= nn <= (1.5 * k):
                    if used[nn] != 0:
                        continue
                    used[nn] = used[n]
                    q.append(nn)
                if nn == k:
                    print(used[nn])
                    q = []
                    break
            else:
                nn = n + dx[i]
                if 0 <= nn <= (1.5 * k):
                    if used[nn] != 0:
                        continue
                    used[nn] = used[n] + 1
                    q.append(nn)
                    chk += 1
                if nn == k:
                    print(used[nn])
                    q = []
                    break
