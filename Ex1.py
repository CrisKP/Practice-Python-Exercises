#http://www.practicepython.org/exercise/2014/01/29/01-character-input.html
#Character Input

#ask the user to enter their name and age. Print out a message that tells them the year that they will turn 100 years old.

name = input("What\'s your name?: ")
print("Hi " + name)
age = int(input("What\'s your age?: "))
year = int(2017-age + 100)
message = (name + " will be 100 years old in the year " + str(year))
print(message)

#ask the user for a number and print out that many copies of the previous message on separate lines.
number = int(input("Choose a random number: "))
print(number * (message + "\n"))

#print(type(message))