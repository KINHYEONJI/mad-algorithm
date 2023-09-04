n = input()

len = len(n) - 1

result = 0

for i in range(len):
    result += 9 * (10 ** i) * (i + 1)
    i += 1
result += ((int(n)-(10**len))+1)* (len+1)

print(result)