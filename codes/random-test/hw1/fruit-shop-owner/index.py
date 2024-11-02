def fruit_pyramid(x):
  total = 0
  for i in range(1, x + 1):
      total += i * i
  return total

n = int(input())

print(fruit_pyramid(n))