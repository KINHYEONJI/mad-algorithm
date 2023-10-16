"""
23 / 10 / 14 알고 스터디
무한 수열
"""
import sys
from collections import defaultdict


def input(): return sys.stdin.readline().rstrip()


def dfs(n):
    if n == 0: return 1
    # dict --> 키값 없으면 에러 발생
    # defaultdict --> 키값이 없으면 자체생성
    # 속도는 dict보다 느림
    # 백트래킹 때문에 사용
    if seq[n]: return seq[n]

    div1 = n // p
    div2 = n // q

    seq[n] = dfs(div1) + dfs(div2)
    return seq[n]


n, p, q = map(int, input().split())
seq = defaultdict(int)

print(dfs(n))
