n = int(input())
for test_case in range(n):
    animal = dict()
    lst = []
    crawling = list(input().split())
    while 1:
        a = input()
        if a == 'what does the fox say?':
            break
        x,y = a.split(' goes ')
        while y in crawling:
            crawling.remove(y)
    print(*crawling)