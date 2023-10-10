"""
23 / 10 / 10 알고 스터디
계란으로 계란치기
"""
import sys
def input(): return sys.stdin.readline().rstrip()

n = int(input())
arr_S_W = [list(map(int, input().split())) for _ in range(n)]

"""
내구도 0 되면 깨짐. 내구도 까지는건 상대 편 무게만큼
"""