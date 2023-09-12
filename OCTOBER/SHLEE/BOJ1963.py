import math
import sys
from collections import deque

input = sys.stdin.readline


def prime(n):
    if n < 2:
        return 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1


def bfs(start, end):
    if start == end:
        return 0
    q = deque()
    q.append([start, 0])
    used = set()

    while q:
        x, lev = q.popleft()
        used.add(x)
        lst = []
        ans = list(map(int, str(x)))

        for i in range(4):
            for j in range(10):
                if i == 0 and j == 0: continue
                if ans[i] == j: continue
                new_ans = ans[:]
                new_ans[i] = j
                num = int(''.join(map(str, new_ans)))  # 수정: 변수명 변경 ans -> new_ans
                if num >= 1000 and prime(num) == 1:
                    lst.append(num)
        for i in lst:
            if i == end:
                return lev + 1
            if i in used: continue
            q.append([i, lev + 1])

    return 'Impossible'


T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    ret = bfs(a, b)
    print(ret)
