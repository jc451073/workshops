Instruction = 'Welcome to our program.\nInput negative number of items to quit'
print('Instruction')


numOfItems = 1
while numOfItems > 0:
   numOfItems = int(input('Please input the number of items:'))
   costperItems = float(input('The shipping cost for each item: $'))
   totalshipcost = numOfItems * costperItems;
   if totalshipcost > 100:
      totalshipcost = totalshipcost  * 0.9
   print('Total cost for delivering your products is: ',totalshipcost)
