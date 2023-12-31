'''
1 ~ 9 --> 1자리       9개           9 * 1
10 ~ 99 --> 2자리     2 * 90개     18 * 10
100 ~ 999 --> 3자리   3 * 900개    27 * 100
1000 ~ 9999 -->4자리  4 * 9000개   36 * 1000
--> [9, 180, 2700, 36000, ..., 9n(10^n-1)]
따라서, n 자리 수이면, n-1 인덱스 까지 다 합하고 나머지 계산
'''
# N 숫자 입력 후 자릿수를 N_length에 할당
N = int(input())
N_length = len((str(N)))
# N이 해당 자릿수의 최대값을 가질때 자리수에 대한 합을 lst에 할당
lst = []
for n in range(0, N_length):
    lst.append(9 * n * (10 ** (n - 1)))
'''
각 자리수의 최대값의 합을 구한 뒤 입력값 +
입력값보다 1자리 수 적은 10^n 빼고 1 더한 뒤 자릿수 만큼 곱셈
예를 들어 524를 입력 받았다면 (9+180) + 2(524 - 100 + 1)
'''
N_sum = sum(lst) + (abs(N + 1 - (10 ** n)) * N_length)
print(int(N_sum))
