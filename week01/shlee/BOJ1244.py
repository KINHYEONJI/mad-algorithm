N = int(input())
lst = list(map(int, input().split()))
n = int(input())


for _ in range(n):
    gender, num = map(int, input().split())
    if gender == 1:
        for i in range(1,N):
            lst[i] = 1 -lst[i]
    else:
        lst[num] = 1 - lst[num]
        i = 1
        while num - i > 0 and num + i <= N and lst[num - 1 + i] == lst[num - 1 - i]:
            lst[n-1+i] = 1- lst[n-1+i]
            lst[n - 1 + i] = 1 -  lst[n - 1 + i]
            i += 1


for i in range(N):  # 20개씩 출력
    print(lst[i], end=' ')
    if not (i + 1) % 20:
        print()


def switch(x):
    return 0 if x == 1 else 1

def process_switches(lst, num, gender):
    if gender == 1:
        for i in range(num - 1, len(lst), num):
            lst[i] = switch(lst[i])
    else:
        for i in range(len(lst)):
            left, right = i - 1, i + 1
            while left >= 0 and right < len(lst) and lst[left] == lst[right]:
                lst[left] = switch(lst[left])
                lst[right] = switch(lst[right])
                left -= 1
                right += 1

N = int(input())
lst = list(map(int, input().split()))
n = int(input())

for _ in range(n):
    gender, num = map(int, input().split())
    process_switches(lst, num, gender)

# Output the final state of the switches
for i in range(N):
    print(lst[i], end=' ')
    if (i + 1) % 20 == 0:
        print()  # Move to the next line after printing 20 switches
