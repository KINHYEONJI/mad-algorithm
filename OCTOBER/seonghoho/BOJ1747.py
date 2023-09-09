N = int(input())    # N보다 커야 된다.

n = int(2000000)    # 200만까지 찾기
check = [0]*(n+1)   # 체크 리스트 만들어서 소수 판별
for i in range(2,n+1):  # 2에서 n+1까지 중에
    if check[i]==1: continue # 체크되면 패스
    for j in range(i+i,n+1,i): # i+i부터 i씩 띄어서 체크하기. 배수는 다 체크 
        check[j] =1

lst = []    # 빈 리스트에 체크 안된 소수 넣기
for i in range(2,n+1):
    if check[i]==0:
        lst.append(i)

for i in range(len(lst)):
    if lst[i] <10:  # 소수가 한 자릿수 이면
        if lst[i] >=N:  # N보다 크거나 같은 소수일 때
            print(lst[i])   # 출력
            break
    else:
        cnt = 0
        lst_num = list(str(lst[i])) # i번째 소수를 문자로 만들어 리스트만들어서 자릿수 센다
        for j in range(1,int(len(lst_num)/2)+1):
            if lst_num[j-1] == lst_num[-j]: # 맨 앞자리, 맨 뒷자리 비교해서 같으면 cnt+=1
                cnt += 1
        if int(len(lst_num)/2) == cnt: # 자릿수 돈 만큼 cnt 쌓이면 펠린드롬이므로
            if lst[i] >= N: # N보다 크거나 같을 때 출력
                print(lst[i])
                break
