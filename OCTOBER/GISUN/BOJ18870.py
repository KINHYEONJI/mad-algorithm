# 실패 lst.index()  로 for 문으로 찾다 실패하였음 시간복잡도 o(n)
# 딕셔너리에 넣어서 해결

n=int(input())
lst=list(map(int,input().split()))
lst2=sorted(list(set(lst)))

dic={lst2[i]:i for i in range(len(lst2))}

for i in lst:
    print(dic[i],end= ' ')

