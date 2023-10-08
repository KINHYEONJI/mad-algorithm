"""
23 / 09 / 07 알고 스터디
Z
"""
import sys
def input(): return sys.stdin.readline().rstrip()

def z(n, r, c):
    if n == 0:
        return 0
    n = 2 * (r % 2) + (c % 2) + 4 * z(n - 1, r // 2, c // 2)
    return n


n, r, c = map(int, input().split())
print(z(n, r, c))
