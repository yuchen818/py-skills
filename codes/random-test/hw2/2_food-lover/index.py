stomach_capacity = int(input())
prices = []
capacities = []
for _ in range(3):
  prices.append(int(input()))      # 食物價格
  capacities.append(int(input()))  # 食物所需容量

eat_counts = [0, 0, 0]
total_value = 0

# 吃飯算法
for i in range(3):
  while stomach_capacity >= capacities[i]:
    stomach_capacity -= capacities[i]
    eat_counts[i] += 1
    total_value += prices[i]

# 計算折扣後餐費
normal_meal_cost = 450
total_items = sum(eat_counts)
if total_items >= 20:
  normal_meal_cost *= 0.8
if total_items >= 30:
  total_value += 900

profit = total_value - normal_meal_cost

# format
print(*eat_counts)
print(f"{profit:.1f}")
