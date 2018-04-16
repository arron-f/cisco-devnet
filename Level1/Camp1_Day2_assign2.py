#Libraries and Functions always come in handy to developers by allowing reusability of existing code. There are certain well known inherent libraries that you have access to after installing python. By using these libraries and functions in them, write a program (in Python 3) to guess a randomly generated number between 1 and 10. 
#For Example: 
#
#Guess the number: 4
#Wrong, try again! 
#
#Guess the number: 8
#Correct! 

#Hint: Figure out which library the randint function belongs to.  

import random

try:
  guess = random.randint(1,10)

  myinput=int(input('Guess the number: '))
  while ((myinput >= 1) and (myinput <= 10)):
   if guess == myinput:
     print("Correct!")
     guess = random.randint(1,10)
     print("Regenerating guess, to exit type 0 or any other key")
   else:
     print("Wrong, try again!")

   myinput=int(input('Guess the number: '))

except ValueError:
  print("Not a number exiting")



