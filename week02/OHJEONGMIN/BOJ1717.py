def findboss(member):
    global arr
    if arr[member] == -1:
        return member
    ret = findboss(arr[member])
    arr[member] = ret
    return ret
def union(a,b):
    global arr
    fa,fb = findboss(a),findboss(b)
    if fa==fb:
        return
    arr[fb] = fa
def check(a,b): #같은 집합인지 확인할 수 있는 함수 생성
    global arr
    fa, fb = findboss(a), findboss(b)
    if fa == fb:
        return 1

n,m = map(int,input().split())
arr = [-1]*(n+1)  # a,b의 범위가 0부터기 때문에 -1로 초기화
for i in range(m):
    cal,a,b = map(int,input().split())
    if cal==0:
        union(a,b)
    else:
        if check(a,b)==1:
            print('yes')

        else:
            print('no')
