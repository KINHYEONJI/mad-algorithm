import sys

input = sys.stdin.readline
sys.setrecursionlimit(100010)


def dfs(x):
    global result
    cycle.append(x)
    num = lst[x]
    visited[x] = 1
    if visited[num] == 1:
        if num in cycle:
            result += cycle[cycle.index(num):]
        return
    else:
        dfs(num)


for i in range(int(input())):
    n = int(input())
    lst = [0] + list(map(int, input().split()))
    visited = [0] * (n + 1)
    result = []

    for i in range(1, n + 1):
        cycle = []
        if visited[i] == 0:
            dfs(i)

    print(n - len(result))