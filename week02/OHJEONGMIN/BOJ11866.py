from collections import deque

q = deque()
N, K = map(int, input().split())
for i in range(1, N + 1):
    q.append(i)
lst = []
while q:
    for i in range(K - 1):  # K번째 숫자 빼내야 되기 때문에 k-1까지
        a = q.popleft()
        q.append(a)
    num = q.popleft()
    lst.append(num)

print('<', end='')
for i in range(N - 1):
    print(f'{lst[i]}, ', end='')
print(f'{lst[N - 1]}>')
