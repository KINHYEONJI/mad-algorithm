hour, minute = map(int,input().split())
cook_min = int(input())
hour += cook_min//60
minute += cook_min-60*(cook_min//60)

if minute >=60:
    minute_cnt = minute//60
    minute %= 60
    hour+=minute_cnt
    
if hour >= 24:
    hour %= 24

print(f'{hour} {minute}')