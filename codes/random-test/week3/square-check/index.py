def square_check(x):
  if x == 1:
    return 0
  
  for i in range(x-1, 0, -1):
    num_sqrt = i ** 0.5
    if num_sqrt.is_integer():
      return i

n = int(input())

print(square_check(n))


# range(N+1)[::-1] - 耗時
# isinstance - 平方根後為 float 無法有效判斷