import sys
input = sys.stdin.readline

n = int(input())
arr =[int(input())]
for _ in range(n-1):
    p = int(input())
    if p == 0:
        arr.pop()
    else:
        arr.append(p)

print(sum(arr))