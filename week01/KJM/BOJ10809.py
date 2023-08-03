'''
a~z를 아스키코드값으로 순회
index로 해당 문자열에서의 위치를 추출
에러 방지를 위해 있는 경우만 족너
'''
str_ = list(input()) 

for i in range(97,123): # 97~122 , a~z
    
    if chr(i) in str_: 
        print(str_.index(chr(i)),end=' ')
        
    else:
        print(-1,end=' ')
    