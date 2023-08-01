cycle = list(map(int, input()))
if len(cycle) == 1:
    cycle.insert(0, 0)
count = 0
total_cycle = 0
start_cycle = cycle[:]
while True:
    count += 1
    total_cycle = 0
    for i in range(2):
        total_cycle += cycle[i]
    cycle.remove(cycle[0])
    cycle.append(total_cycle % 10)
    if start_cycle == cycle:
        break

print(count)

