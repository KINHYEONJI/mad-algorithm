def max_num(level):
    if level == len(path):
        new_lst.append(''.join(map(str,path)))
        return
    for i in range(len(k)):
        path[level] = k[i]
        max_num(level+1)

new_lst=[]


N,K = map(int,input().split())
st_N = str(N)
k = list(map(int,input().split()))
result_lst= []
# path = ['']*len(k)
path = [0] * (len(st_N))
max_num(0)

for i in new_lst:
    if int(i) <= N:
        result_lst.append(int(i))

if int(new_lst[0])>N:
    path = [0] * (len(st_N)-1)
    new_lst=[]
    max_num(0)
    for i in new_lst:
        if int(i) <= N:
            result_lst.append(int(i))
    print(max(new_lst))
else:
    for i in new_lst:
        if int(i) <= N:
            result_lst.append(int(i))
    print(max(result_lst))

