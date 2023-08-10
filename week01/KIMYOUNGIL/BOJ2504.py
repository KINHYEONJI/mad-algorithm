st = list(input())
n = len(st)

if st[0] == ']' or st[0] == ')':
    print(0)

else:
    arr = [0]
    res = 0
    a = 0
    for i in range(n):
        if st[i] == '(' or st[i] =='[':
            arr.append(st[i])
            a = 0
        elif st[i] == ']':
            if arr[-1] == '[':
                arr.pop()
                if a == 0:
                    a += 3
                else:
                    a *= 3
                res += a
            else:
                print(0)
                break

        elif st[i] == ')':
            if arr[-1] == '(':
                arr.pop()
                if a == 0:
                    a += 2
                else:
                    a *= 2
            else:
                print(0)
                break