#http://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
#Odd or Even Extras

#Ask the user for two numbers: one number to check (num) and one number to divide by (check). 
#Print a message stating if the number is even or odd.
#Then print a message saying if it is a multiple of 4 or not.
#If check divides evenly into num, tell that to the user. If not, print a different appropriate message.


num = int(input("Choose a number to check: "))
check = int(input("Choose a number to divide it by: "))

if num % 2 == 0:
	print("Your number is even")
else:
	print("Your number is odd")

if num % 4 == 0:
	print("Your number is a multiple of 4")
else:
	print("Your number is not a multiple of 4")

remainder = int(num % check)
if remainder == 0:
	print(num, "divides evenly by", check)
else:
	print("After the division, you have a remainder of " + str(remainder))
