t, m = map(int,input().split())
m_1 = int(input())

m_2 = m +m_1

while m_2 >=60:
    m_2 -=60
    t +=1

if t >=24:
    t -= 24

print(t, m_2)

#!!