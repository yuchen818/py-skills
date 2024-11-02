def multiply_four(numbers):
  x = len(numbers)
  if x < 4:
    return 'Need four numbers.'
  
  # 情況1, 全部取最大4個數
  multiple_1 = numbers[x-1] * numbers[x-2] * numbers[x-3] * numbers[x-4]
  
  # 情況2, 取最小兩個數和最大兩個數
  multiple_2 = numbers[0] * numbers[1] * numbers[x-1] * numbers[x-2]

  # 情況3, 取最小4個數
  multiple_3 = numbers[0] * numbers[1] * numbers[2] * numbers[3]
  
  return max(multiple_1, multiple_2, multiple_3)

n = list(map(int, input().split()))

print(multiply_four(n))