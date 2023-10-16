import sys

n, p, q = map(int, sys.stdin.readline().split())

dict = {} #메모이제이션 딕셔너리로 활용
dict[0] = 1

def solution(n):

    if (n in dict):
        return dict[n]

    else:
        dict[n] = solution(n//p) + solution(n//q) 
        return dict[n]

print(solution(n))