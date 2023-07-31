time = list(map(int, input().split()))
minute = int(input())

times = time[0] * 60 + time[1]
lst_time = times + minute

lst_hour, lst_minute = divmod(lst_time, 60)
lst_hour %= 24 
print(lst_hour, lst_minute)