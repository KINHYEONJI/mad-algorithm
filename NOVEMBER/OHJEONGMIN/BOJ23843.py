import heapq

n,m = map(int,input().split())
charge = list(map(int,input().split()))
time = [0]*m
charge.sort(reverse=True)
index = 0
#제일 큰거부터 뽑아 놓고 그 값과 같아질때까지 ++
for i in range(n):
    if i==0:
        time[0] +=charge[i]
        continue
    if time[0]>=time[index]+charge[i]:
        time[index]+=charge[i]
    else:
        if index+1>m-1:
            index = 0
            time[index]+=charge[i]
        else:
            index+=1
            time[index]+=charge[i]
print(time[0])

