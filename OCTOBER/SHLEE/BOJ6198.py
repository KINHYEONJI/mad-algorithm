import sys

input = sys.stdin.readline
n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))

cnt = 0
stack = []
for x in lst:
    # stack에는 현재 건물을 바라 볼 수 있는 건물들만 남도록 반복한다.
    while stack:
        # 현재 건물의 높이가 stack의 top 보다 크거나 같으면, 이전 건물에서 현재 건물을 바라볼 수 없다.
        if x >= stack[-1]:
            stack.pop()
        # 현재 건물의 높이가 stack의 top 보다 작으면, 현재 건물을 바라 볼 수 있다.
        else:
            # 따라서, stack의 길이(현재 건물을 바라볼 수 있는 건물의 개수)를 더해준다.
            cnt += len(stack)
            break

    stack.append(x)

print(cnt)