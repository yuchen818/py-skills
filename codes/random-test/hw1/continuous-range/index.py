def count_segments(x):
  count = 0
  prev_char = '0'

  for char in x:
    # 判斷是否與前一個不同
    if char == '1' and prev_char == '0':
      count += 1
    prev_char = char

  return count

n = input()

print(count_segments(n))