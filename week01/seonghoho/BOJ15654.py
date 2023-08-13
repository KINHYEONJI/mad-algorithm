n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()                      # 두 번째 줄에 입력 받은 수를 오름차순으로 정렬
path = [''] * m
used = [0] * len(lst)           # 입력 받음 문자 갯수만큼 used 생성


def abc(level):
    if level == m:
        for i in range(m):
            print(path[i], end=' ')
        print()
        return
    for i in range(len(lst)):
        if used[i] == 1:        # 사용중이면 건너띄기
            continue
        path[level] = lst[i]
        used[i] += 1
        abc(level+1)
        used[i] -= 1
abc(0)
