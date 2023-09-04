h,m = map(int, input().split()) # 입력 시, 시간/분
needT = int(input())

Whole_m = (h*60) + m + needT # 총 계산 후, 분
Trans_h = Whole_m // 60 # 총 계산 후, 시

if 0 <= needT <= 1000:
  if 0 <= m <= 60:  
    m2 = Whole_m % 60 # 남은 분 변환 from 전체시간
    
  if 0 <= h <= 23:  # 0시 부터 23시 사이 입력받으면 
    h2 = Trans_h    # 출력은 계산 후 시간
    
    if (h2 % 24) == 0: #만약 출력시간이 24시의 배수가 되면 
      h2 = 0           # 0으로 출력
            
    if Trans_h >= 24:          #만약 총 계산 후 시간이 24를 초과한다면 
      h2 = Trans_h - (24 * (Trans_h//24) )   # 초과된 시간에서 24시간을 뺀다
                                          # 단, 0~24 사이가 되도록 24시간 주기 싸이클 적용
    print(h2,m2)