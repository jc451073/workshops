finished = False
result = 0
while not finished:
 try:
     result = int(input("Enter the integer"))
     finished = True
 except :
   print("Please enter a valid integer.")
print("Valid result is:", result)
