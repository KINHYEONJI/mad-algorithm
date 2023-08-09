num = int(input())
for i in range(num-1):
    print('* ' *i + '*' * (1 + 4 * (num - i - 1)) + ' *' * i)
    print('* ' * (i + 1) + ' ' * (1 + 4 * (num - i - 2)) + ' *' * (i + 1))
print('* ' * (2 * num - 1))
for i in range(num -1):
    print('* ' * (num -i -1) + ' ' * (1 + 4 * i) + ' *' * (num -i -1))
    print('* ' * (num -i -2) + '*' * (1 + 4 * (i + 1)) + ' *' * (num -i -2))