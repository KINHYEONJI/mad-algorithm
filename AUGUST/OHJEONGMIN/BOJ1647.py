def findboss(member):
    global arr
    if arr[member] == 0:
        return member
    ret = findboss(arr[member])
    arr[member] = ret
    return ret

def union(a,b):
    global arr
    fa,fb = findboss(a),findboss(b)
    if fa==fb:
        return 1
    arr[fb] = fa

n,m = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(m)]
lst.sort(key=lambda x:x[2])         # cost가 적은 순대로 정렬

arr = [0]*(n+1)
cost= 0
cnt=0
visited = [0]*(n+1)
for i in range(m):
    ret = union(lst[i][0],lst[i][1])
    if ret!=1:      #두 마을의 boss가 같지 않알때만 cost와 cnt더해주기
        cost+= lst[i][2]
        cnt+=1
    if cnt==n-1:  # 마을을 두 개로 분리하기 위해서 제일 비싼 마을 쪼개기
        cost-=lst[i][2]
        break

print(cost)
