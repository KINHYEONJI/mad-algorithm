import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))
sort_lst = sorted(set(lst))

dic={}
for i in range(len(set(sort_lst))):
    dic[sort_lst[i]] = i


for i in range(len(lst)):
    print(dic.get(lst[i]),end=' ')