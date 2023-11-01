"""
23 / 11 / 01 알고 스터디
맥주 마시면서 걸어가기
"""
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()


def recursive(x, y):
    if abs(x - rx) + abs(y - ry) <= 1000:
        print('happy')
        return
    else:
        if arr:
            xx, yy = arr.popleft()
            if abs(x - xx) + abs(y - yy) <= 1000:
                recursive(xx, yy)
            # 편의점까지 못가면
            else:
                print('sad')
        # 편의점 다 돌았는데도 못가면
        else:
            print('sad')
        # 편의점을 팝 하지말고 편의점 포문 돌아서 되는 조건으로 하고 방문 편의점 방문 체크

TC = int(input())
for _ in range(TC):
    n = int(input())
    x, y = map(int, input().split())
    arr = deque([list(map(int, input().split())) for _ in range(n)])
    rx, ry = map(int, input().split())
    recursive(x, y)