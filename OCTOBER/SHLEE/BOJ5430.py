from collections import deque

t = int(input())

for _ in range(t):
    p = input()
    n = int(input())
    x = input()[1:-1].split(',')
    q = deque(x)

    ans = 0
    flag = 0

    if n == 0:
        q = []

    for i in p:
        if i == 'R':
            ans += 1
        else:
            if len(q) == 0:
                print('error')
                flag = 1
                break
            elif ans % 2 == 1:
                q.pop()
            else:
                q.popleft()

    if not flag:
        if ans % 2 == 1:
            q.reverse()
        print('[' + ','.join(q) + ']')
