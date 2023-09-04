a,b = map(int,input().split())
measure_a = []
measure_b = []
for i in range(1,a+1):
    if a % i == 0:
        measure_a.append(i)
for i in range(1,b+1):
    if b % i == 0:
        measure_b.append(i)

same_lst = []
for i in range(len(measure_a)):
    for k in range(len(measure_b)):
        if measure_a[i]==measure_b[k]:
            same_lst.append(measure_a[i])

GCD = max(same_lst)
LCM = (a*b)//GCD
print(GCD)
print(LCM)