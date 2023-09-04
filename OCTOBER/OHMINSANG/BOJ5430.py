import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for _ in range(T):
    Fuction = list(input())
    n = int(input())
    lst = input()
    print(Fuction)
    for i in lst:
        print(i, end=' ')
    print(len(lst))
    print()