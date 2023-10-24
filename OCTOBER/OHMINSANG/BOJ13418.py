"""
23 / 10 / 24 알고 스터디
학교 탐방하기
"""
import sys
def input(): return sys.stdin.readline().rstrip()


def find(x):
    if visited[x] == x:
        return x
    visited[x] = find(visited[x])
    return visited[x]


def union(a, b, c):
    fa, fb = find(a), find(b)
    if fa == fb:
        return 0

    if fa > fb:
        visited[fb] = fa
    else:
        visited[fa] = fb
    if c == 1:
        return 0
    else:
        return 1


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m+1)]

# 최대 신장 트리
arr.sort(key= lambda x:x[2])
visited = [i for i in range(n + 1)]
Max = 0
for a,b,c in arr:
    Max += union(a, b, c)

# 최소 신장 트리
arr.sort(key= lambda x:-x[2])
visited = [i for i in range(n + 1)]
Min = 0
for a,b,c in arr:
    Min += union(a, b, c)

print(Max ** 2 - Min ** 2)