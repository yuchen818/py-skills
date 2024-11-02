def check_moon_cake(pack_id, exp_date, single_price, amount):
  prices = {60, 70, 80}
  amounts = {3, 6, 9, 12}
  
  # 1. 檢查數量及單價
  if single_price not in prices or amount not in amounts:
    return f"{pack_id} has labeling problem!"
  
  # 2. 定義相關日期
  expired = [2023, 9, 26]      # 9/26（不含）前過期
  discount_80 = [2023, 10, 7]  # 10/7（含）至 10/13 八折
  full_price = [2023, 10, 14]  # 10/14（含）後原價
  
  # 3. 計算售價 (單價*數量)
  base_price = single_price * amount
  
  # 4. 按日期比較確認售價
  if exp_date <= expired:
    return f"{pack_id} has expired, it should not be sold."
  elif exp_date >= full_price:
    pack_price = base_price
  elif exp_date >= discount_80:
    pack_price = int(base_price * 0.8)
  else:
    pack_price = int(base_price * 0.6)
  
  return f"{pack_id} should be sold at price {pack_price}."

def main():
  t = int(input())

  if not (1 <= t <= 8):
    return "Hint: 1 ≤ t ≤ 8"
  
  for _ in range(t):
    # 1. 拆分內容
    pack_id, exp_date, single_price, amount = input().split(',')

    # 2. 日期轉換為列表便於後續比較
    y, m, d = map(int, exp_date.split('-'))

    if (y < 0 or m < 0 or d < 0):
      return "Hint: y, m, d ≥ 0"
    
    exp_date = [y, m, d]

    if (int(single_price) < 0 or int(amount) < 0):
      return "Hint: single_price, amount ≥ 0"
    
    result = check_moon_cake(pack_id, exp_date, int(single_price), int(amount))
    print(result)

if __name__ == "__main__":
  main()