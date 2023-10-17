'''
옥상 정원 꾸미기
stack으로 오른쪽을 보는 것이 아닌, stack의 높이를 생각해보자.
'''

import sys
input = sys.stdin.readline

N = int(input())
lst = []
for i in range(N):
    lst.append(int(input()))

cnt = 0
stack = []
'''
lst에서 하나씩 꺼내서 보는데, stack이 차 있고 lst에서 꺼낸 값이 stack의 맨 위(맨 뒤)보다 크면 
맨 위 값 pop, 이 작업 반복하고 더이상 없으면 이 꺼낸 값 stack에 추가한다.
stack의 길이 -1한 값 cnt에 반복해서 더하면 된다.
'''
for i in lst:
    while stack and i >= stack[-1]:
        stack.pop()
    stack.append(i)

    cnt += len(stack) - 1
print(cnt)