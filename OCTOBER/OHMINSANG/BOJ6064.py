import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for _ in range(T):
    m, n, x, y = map(int, input().split())
    Max = m * n
    i = 0
    year = -1
    if y == n: y = 0
    while 1:
        if ((m * i) + x) % n == y:
            year = (m * i) + x
            break
        if (m * i) + x > Max: break
        i += 1
    print(year)
