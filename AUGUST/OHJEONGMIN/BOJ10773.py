N = int(input())
lst = []
for i in range(N):
    num = int(input())
    if num == 0:
        lst.pop()
        continue
    lst.append(num)

print(sum(lst))
