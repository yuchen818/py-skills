def sort_sum_number(x):
  sorted_list = sorted(x, key=lambda num: sum(int(digit) for digit in str(num)))
  return sorted_list
    
n = list(map(int, input().split()))

print(sort_sum_number(n))