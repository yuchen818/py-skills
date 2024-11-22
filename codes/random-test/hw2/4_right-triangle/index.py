# def right_angled(a, b, c):
#   return (a * a + b * b == c * c)

# long = int(input())
# short = list(map(int, input().split()))

# print(right_angled(short[0], short[1], long))

# 勘誤: 是判斷 y-z 中是否有兩個整數滿足 c^2，不是直接判斷 y、z 是否滿足
def is_right_triangle(c, y, z):
  c_squared = c * c

  lower = min(y, z)
  upper = max(y, z)
  
  # 由 a 與 b 進行計算遇到符合的就直接返回結果
  for a in range(lower, upper + 1):
    for b in range(lower, upper + 1):
      if a * a + b * b == c_squared:
        return True
  
  return False

c = int(input())
y, z = map(int, input().split())

print(is_right_triangle(c, y, z))
