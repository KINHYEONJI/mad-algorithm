import sys
input = sys.stdin.readline


def dfs(lv, a):
    if lv == L:
        j, m = 0,0
        for i in range(L):
            if pw[i] in ['a', 'e', 'i', 'o', 'u']:
                m += 1
            else:
                j += 1

        if j >= 2 and m >= 1:
            print(*pw, sep='')
        return

    for i in range(a, C):
        pw.append(lst[i])
        dfs(lv + 1, i + 1)
        pw.pop()


L, C = map(int, input().split())  #L,C받아주기
lst = list(input().split())
lst.sort()
pw = []
dfs(0, 0)
