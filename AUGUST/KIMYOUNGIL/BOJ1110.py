n=int(input())

if n < 10:
    n *= 10
    
num1 = n//10+n%10
num2 = (n%10)*10+(num1%10)
cnt = 1

while num2 != n:
    nump = num2//10+num2%10
    num2 = (num2%10)*10+(nump%10)
    cnt += 1

print(cnt)