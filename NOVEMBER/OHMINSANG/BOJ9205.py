"""
23 / 11 / 01 알고 스터디
맥주 마시면서 걸어가기
"""
import sys
def input(): return sys.stdin.readline().rstrip()


def recursive(x, y):
    if abs(x - rx) + abs(y - ry) <= 1000:
        return 1
    else:
        for lst in enumerate(arr):
            i, (xx, yy) = lst
            if visited[i] == 1: continue
            if abs(x - xx) + abs(y - yy) <= 1000:
                visited[i] = 1

                # 재귀 호출 값이 1일때만 리턴받기
                if recursive(xx, yy): return 1
    return 0


TC = int(input())
for _ in range(TC):
    n = int(input())
    hx, hy = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    rx, ry = map(int, input().split())
    visited = [0] * n
    ans = recursive(hx, hy)
    if ans == 1: print('happy')
    else: print('sad')