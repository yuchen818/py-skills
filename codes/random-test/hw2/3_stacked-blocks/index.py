N = int(input())  # 總層數
k = int(input())  # 最上層積木數量

# 積木分類
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"

result = []
# 各種類積木索引
upper_index = lower_index = number_index = 0

# 逐層堆積算法
for i in range(N):
  # 計算該層所需積木
  blocks_needed = i + k
    
  # 根據層數餘數選擇積木種類
  if (i + 1) % 3 == 1:
    current_layer = "".join(
      upper[(upper_index + j) % len(upper)] for j in range(blocks_needed)
    )
    upper_index += blocks_needed
  elif (i + 1) % 3 == 2:
    current_layer = "".join(
      lower[(lower_index + j) % len(lower)] for j in range(blocks_needed)
    )
    lower_index += blocks_needed
  else:
    current_layer = "".join(
      numbers[(number_index + j) % len(numbers)] for j in range(blocks_needed)
    )
    number_index += blocks_needed

  result.append(current_layer)


print("\n".join(result))
