N = int(input())
lst = list(map(int, input().split()))
new = sorted(set(lst))

dic = {}
for i in range(len(new)):
  dic[new[i]]=i
  
for i in lst:
  print(dic[i],end=' ')