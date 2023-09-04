
L, R = input().split()
cnt = 0 
flag = False

if len(L) != len(R):  # 두 숫자의 길이가 다르면 10의 제곱만큼 차이가 나므로
# 8을 가질 수 있는 가장 큰 수(맨앞자리)가 바뀌는 범위가 항상 포함되므로 8이 포함되지 않는 경우가 항상 존재
    flag = True 
else: # 두 숫자의 길이가 같으면 (10의 제곱자리수가 같으면)
    for i in range(len(L)):  # 인덱스 
        if L[i] == R[i]:   # 두 수의 각 자리값이 같으면
            if L[i] == '8': # 그 값이 8이라면 ( 가장 큰 값을 포함한 범위를 가지므로 최소 8이 1개 이상 있음) 
                cnt += 1  
        else: # 가장 큰 값이 서로 다르면 8을 포함하지 않는 경우의 수가 생기므로 
            break # 8은 0개가 되는 경우가 항상 있음 

if flag:
    print(0)
else:
    print(cnt)
    
            