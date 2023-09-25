n = int(input())
lst = list(map(int, input().split()))
dic = {num: i for i, num in enumerate(sorted(set(lst)))}
for i in range(n):
    idx = dic[lst[i]]
    print(idx, end=' ')

# 처음 풀이 - 시간 초과

# n = int(input())
# lst = list(map(int, input().split()))
# lst2 = list(set(sorted(lst)))
# for i in range(n):
#     idx = lst2.index(lst[i])
#     print(idx, end=' ')