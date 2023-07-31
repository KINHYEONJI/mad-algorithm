a, b = map(int, input().split())
 
arr=[]
for i in range(1,min(a,b)+1):
    if a%i == 0 and b%i ==0:
        arr.append(i)
max_ = max(arr)
m_max = (a//max_)*(b//max_)*max_

print(f'{max_}\n{m_max}')