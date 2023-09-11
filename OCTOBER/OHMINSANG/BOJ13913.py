import sys

sys.stdin = open('input.txt', 'r')

from collections import deque


# 경로 역추적 함수
def back_path(nn, k, used):
    path = [k]
    while used[nn] > 1:
        for nn in [k + 1, k - 1, k // 2]:
            if used[nn] == used[k] - 1:
                k = nn
                break
        path.insert(0, k)
    path.insert(0, original_n)
    return path


n, k = map(int, input().split())
original_n = n

#  위치 같을 때
if n == k:
    print(0)
    print(n)

# n이 k보다 앞에 있을 때
elif n > k:
    print(n - k)
    ans = n - k
    for i in range(ans + 1):
        print(n, end=' ')
        n -= 1

# n보다 k가 앞에 있을 때
else:
    used = [0] * (2 * (k + 1))
    q = deque()
    q.append(n)
    while q:
        n = q.popleft()
        dx = [-1, 1, n]
        for i in range(3):
            nn = n + dx[i]
            if 0 <= nn <= (1.5 * k):
                if used[nn] != 0:
                    continue
                used[nn] = used[n] + 1
                q.append(nn)
            if nn == k:
                print(used[nn])
                path = back_path(nn, k, used)
                print(*path)
                q = []
                break
