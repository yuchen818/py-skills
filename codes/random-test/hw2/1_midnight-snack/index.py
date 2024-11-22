names = input().split()
prices = list(map(int, input().split()))
money = int(input())

for i in range(len(prices)):
  for j in range(i + 1, len(prices)):
    if prices[i] + prices[j] == money:
      print(names[i], names[j])
      break
