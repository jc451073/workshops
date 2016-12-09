
sale = float(input("Enter your sale"))

if (sale < 1000):
    bonus = 10/100 * sale
    print ("Your bonus is: {}".format(bonus))
elif (1000<=sale):
    bonus = 15/100 * sale
    print ("Your bonus is: {}".format(bonus))