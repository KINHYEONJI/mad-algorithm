t=int(input())

for tc in range(t):
    a,lst=input().split()
    print(a,lst)
    for i in range(lst):
        a=lst[i]
        if ord('A') <= ord(a) <= ord('F'):
            a=ord(a)-ord('A')+10
            print(a)