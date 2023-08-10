N, K = map(int, input().split())            # N과 K 입력
lst = list(map(int, input().split()))       # K개의 숫자 입력
n = len(str(N))                             # N의 자릿수 확인
path = [''] * n                             # 재귀에서의 자릿수를 위한 path 생성
lst2 = []
lst.append(0)

def recursion(level):                       # 재귀 함수 생성
    if level == n:
        num = ''.join(map(str, path))       # path에 입력된 숫자를 문자열로 변경 후 단어로 만듬
        lst2.append(num)                    # 만든 단어의 집합
        return

    for i in range(len(lst)):
        path[level] = lst[i]
        recursion(level + 1)

recursion(0)                            # 재귀 함수 실행
int_lst = []                            # 새로운 문자열 생성
for i in lst2:
    ns = i.replace('0','')
    if ns != '':
        int_lst.append(int(ns))

ilst = []
for j in int_lst:
    if j <= N:
        ilst.append(j)

print(max(ilst))                     # 그 중 가장 큰 숫자 출력
