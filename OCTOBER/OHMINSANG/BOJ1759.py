"""
23 / 10 / 06 알고 스터디
암호 만들기
"""
import sys
def input(): return sys.stdin.readline().rstrip()


def DFS(lv, idx):
    if lv == L:
        wkdma, ahdma = 0, 0  # 자음, 모음 개수 카운트
        for i in range(L):
            if pw[i] in AEIOU:
                ahdma += 1
            else:
                wkdma += 1

        if wkdma >= 2 and ahdma >= 1:
            print(*pw, sep='')
        return

    for i in range(idx, C):
        pw.append(lst[i])
        DFS(lv + 1, i + 1)
        pw.pop()


L, C = map(int, input().split())
lst = list(input().split())
lst.sort()
AEIOU = ['a', 'e', 'i', 'o', 'u']
pw = []
DFS(0, 0)
