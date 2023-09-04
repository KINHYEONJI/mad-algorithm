def factorial(x) :
  value = 1
  for i in range(2, x+1) :
    value *= i
  return value

n, k = map(int, input().split())

result = factorial(n) // (factorial(n-k) * factorial(k))
print(result)