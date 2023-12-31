'''
1~9인 9개는 한자릿수, 10~99인 90개는 두자릿수,
100~999인 900개는 세자릿수, 1000~9999인 9000개는 네자릿수.... 규칙 발견!

1. while문으로 N의 자릿수를 구한다.
2. if문을 사용해 한 자릿수면 바로 출력한다.
3. 한 자릿수가 아니면 자릿수 만큼 반복하는데,
   N에서는 9*(10**i)개를 빼고, 총 자릿수 num에서는
   9*(10**i)*(i+1)를 더한다. 
4. 남은 N에 (jari+1)를 곱해서 더한다.
'''
N = int(input())
n = N
jari = 0  #1
while n//10 !=0:
    n //= 10
    jari+=1
 
num = 0
if jari != 0:  #2
    for i in range(jari):  #3
        N -= 9*(10**i)
        num += 9*(10**i)*(i+1)
    num += N*(jari+1)  #4
    print(num)
else:
    print(N)