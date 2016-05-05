"""
n=1
while n <= 20:
    print n
    n = n+1

n=1
print "******"
print "Only the odds now..."
while n <= 20:
    if n%2==1:
        print n
    n = n+1
"""

# FizzBuzz
n = 1
while n <= 100:
    if n % 15 == 0:
        print "FizzBuzz!"
    elif n % 5 == 0:
        print "Buzz"
    elif n % 3== 0:
        print "Fizz"
    else:
        print n
    n = n +1

print "*********"

# Program that counts down from an arbritrary number
n= input("What number would you like me to start at? \n")
while n > 0:
    print n
    n = n -1
print "Blastoff"

import math
print sum(range(0,input('What numer would you like to sum \n')+1))

# make something that prints out only the factors of a number input
number = input("What number would you like the factors of? \n")
for n in range(1,number+1):
    if number%n==0:
        print n
        n=n+1