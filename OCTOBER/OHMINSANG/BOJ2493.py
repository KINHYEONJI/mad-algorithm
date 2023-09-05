import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
lst = list(map(int, input().split()))
stack = []
used = [0]* n
for i in range(n):
    while stack:
        """
        q의 최상단에 입력된 값이 lst의 인덱스번호가 된다.
        q의 해당 인덱스 값과 lst[i]를 비교해서  lst가 더 크면 pop
        """
        if lst[stack[-1][1]] < lst[i]:
            stack.pop()
        else:
            used[i] = stack[-1][1] + 1    # 출력 되야 하는 값 입력
            break
    stack.append([lst[i], i])   # 스택 쌓기
print(*used)