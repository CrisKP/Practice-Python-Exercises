#http://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
#Odd or Even

#Ask the user for a number. Print a message stating if the number is even or odd.
#Then print a message saying if it is a multiple of 4 or not.

number = int(input('Choose a number: '))
if number % 2 == 1:
  print("You chose an odd number")
else:
  print("You chose an even number")
if number % 4 == 0:
  print("Your number is a multiple of 4")
else:
  print("Your number is not a multiple of 4")
  