def string_reverse_sort(x):
  str_list = x.split()

  sorted_list = sorted(str_list, key=lambda s: s[::-1])
  
  return sorted_list
    
n = str(input())

print(string_reverse_sort(n))

# lambda - 自動傳回後排序