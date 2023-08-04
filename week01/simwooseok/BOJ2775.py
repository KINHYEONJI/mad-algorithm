T = int(input())
for i in range(T):
    floor = int(input())
    ho = int(input())
    first_ho = [i for i in range(1, ho + 1)]

    for k in range(floor):
        for i in range(1, ho):
             first_ho[i] += first_ho[i-1]
    print(first_ho[-1])

