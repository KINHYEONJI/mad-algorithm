"""
23 / 10 / 24 알고 스터디
학교 탐방하기
"""
import sys
def input(): return sys.stdin.readline().rstrip()


def find(x, visited):
    if visited[x] == x: return x
    visited[x] = find(visited[x], visited); return visited[x]


def union(a, b, c, visited):
    fa, fb = find(a, visited), find(b, visited)
    if fa == fb: return 0

    visited[fb] = fa
    if c == 1: return 0
    else: return 1

def clac():
    visited = [i for i in range(n + 1)]
    ans = 0
    for a, b, c in arr:
        ans += union(a, b, c, visited)
    return ans

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m+1)]

# 최대 신장 트리
arr.sort(key= lambda x:x[2])
Max = clac()
# 최소 신장 트리
arr.sort(key= lambda x:-x[2])
Min = clac()

print(Max ** 2 - Min ** 2)