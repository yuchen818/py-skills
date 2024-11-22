def who_is_a_popular_king(list):
  name_count = {}
  for name in pudding_list:
    if name in name_count:
      name_count[name] += 1
    else:
      name_count[name] = 1
  
  max_count = max(name_count.values())

  # 建立嘻嘻人對應的布丁數量，找出與 max_count 相符的人 (可優化)
  popular_names = [name for name, count in name_count.items() if count == max_count]
  return max(popular_names)

pudding_list = list(map(str, input().split()))

print(who_is_a_popular_king(pudding_list))