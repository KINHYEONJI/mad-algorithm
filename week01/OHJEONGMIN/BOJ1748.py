num  = int(input())
st_num = str(num)
cnt = 0

for i in range(len(st_num)-1): #1~9n까지 합친 문자열의 길이 ex : 1~99 -> 189
    cnt += 9*10**i*(i+1)

remain = (num-10**(len(st_num)-1)+1)*len(st_num) # 10n부터 끝까지 문자열의 길이
print(cnt+remain)

