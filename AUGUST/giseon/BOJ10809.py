s=list(input())
lst=[-1 for _ in range(26)]

for i in range(26):
    a=chr(i+97)
    if a in s:
        lst[i]=s.index(a)
    else:
        continue

for i in lst:
    print(i,end=' ')