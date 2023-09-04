switch = int(input())
switch_status = list(map(int, input().split()))
student = int(input())

for _ in range(student):
    gender, number = map(int, input().split())

    if gender == 1:
        for i in range(switch):
            if (i+1)%number == 0:
                if switch_status[i] == 0:
                    switch_status[i] = 1
                else:
                    switch_status[i] = 0
    else:
        max_index = min(number,(switch+1)-number)
        if switch_status[(number - 1)] == 0:
            switch_status[(number - 1)] = 1
        else:
            switch_status[(number - 1)] = 0

        for i in range(1,max_index):
            if switch_status[(number-1)-i] == switch_status[(number-1)+i] == 0:
                switch_status[(number - 1) - i] = 1
                switch_status[(number - 1) + i] = 1
            elif switch_status[(number-1)-i] == switch_status[(number-1)+i] == 1:
                switch_status[(number - 1) - i] = 0
                switch_status[(number - 1) + i] = 0
            else:
                break

part = switch//20
if part > 0:
    cnt = 0
    for i in range(part):
        print(*switch_status[20*i:20*(i+1)])
        cnt += 1
    print(*switch_status[cnt*20:])
else:
    print(*switch_status)