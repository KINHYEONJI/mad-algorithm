N=list(map(int,input())) #교수님꺼 따라쳤습니다 ..
bucket =[0 for _ in range(10)] #버킷만들어줍니다

for i in range(len(N)):
    bucket[N[i]] +=1

# for i in range(len(bucket)):
max=-21e8

for i in range(10):
    if i ==6 or i==9: continue #우선 6,9는 제외하고 버킷 담아서 구해주기
    if bucket[i]>Max:
        Max=bucket[i]

six_or_nine=bucket[6]+bucket[9]
six_or_nine=(six_or_nine//2)+(six_or_nine%2) #6과9를 하나로 취급하여 세트수 구해줍니다 세트스 구할땨 // 과 % 를 써서 오류 없게

if Max>six_or_nine:
    ans=Max 
else:
    ans=six_or_nine
print(ans)