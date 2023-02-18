a = int(input("Enter required number of terms "))

x, y = 0, 1
count = 0

if a <= 0:
   print(" enter a positive integer")

else:
   print("Fibonacci sequence:")
   while count < a:
       print(x)
       F = x + y

       x = y
       y = F
       count += 1
