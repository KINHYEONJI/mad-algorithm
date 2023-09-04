n, m = map(int, input().split())
path = [''] * m


def abc(level,start):           #for문의 시작점 바꾸기 위한 start
    if level == m:
        for i in range(m):
            print(path[i], end=' ')
        print()
        return
    for i in range(start,n):
#        if level>0 and (path[level -1] >= i+1):
#           continue            # 이전 자릿수의 숫자가 더 클 경우
        path[level] = i + 1
        abc(level+1, i+1)       #for문 범위를 이전에 입력받은 수 이상으로!

abc(0,0)