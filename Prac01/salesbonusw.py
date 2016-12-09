

sales = float(input("Enter your sale"))
while sales > 0:
    if (sales < 1000):
      Bonus = 0.1 * sales
      print('Bonus is :', Bonus)
    else:
      Bonus = 0.15 * sales
      print('Bonus is :', Bonus)
    sales = float(input('Enter sales: $'))