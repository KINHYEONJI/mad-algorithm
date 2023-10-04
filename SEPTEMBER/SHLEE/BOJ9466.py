# 1. 풀이

import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline


def dfs(x):
    global cnt
    used[x] = 1
    i = arr[x]

    if used[i] == 0:
        dfs(i)
    else:
        if i not in check:
            idx = i
            while idx != x:
                cnt += 1
                idx = arr[idx]
            cnt += 1

    check.add(x)


T = int(input())
for _ in range(T):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    used = [0] * (n + 1)
    check = set()
    cnt = 0
    for i in range(1, n + 1):
        if not used[i]:
            dfs(i)

    print(n - cnt)



# 2. 블로그 참고 (더 좋은 구현인듯함.)

import sys
sys.setrecursionlimit(10**7)


def dfs(n):
    global used, cnt
    used[n] = 1
    check.append(n)

    if used[lst[n]] == 1:
        if lst[n] in check:
            cnt -= len(check[check.index(lst[n]):])

    else:
        dfs(lst[n])


T = int(input())
for _ in range(T):
    N = int(input())
    lst = [0] + list(map(int, input().split()))     # 인덱스와 차이를 해결하기 위해 처음에 0 추가
    used = [0] * (N + 1)
    cnt = N
    for i in range(1, N + 1):
        check = []              # 사이클을 확인하기 위한 리스트 생성
        if used[i] == 0:
            dfs(i)

    print(cnt)
