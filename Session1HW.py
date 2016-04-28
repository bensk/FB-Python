"""
Homework Assignment #1



4.  Enhance the multiplication more by making it 5 questions.  Make a variable called total which starts as 0 (‘total=0’) and every time the user gets a correct answer, besides printing ‘you got it’ increase the value of total by doing ‘total=total+1’
"""

# 1.  Write a program that asks the user to type in a password.  If they enter ‘facebook’ it says ‘you are permitted to enter’.  Anything else, it says ‘incorrect password’.

password = raw_input("What's your password?")
if password == 'facebook':
    print "You are permitted to enter"
else:
    print 'Incorrect password'

# 2. Write a program that asks the user to multiply 5 * 7.  If they get it right, print “you got it”  If they get it wrong, print “not correct” and what the correct answer is.  Use variables a and b for the two numbers and variable c for the user’s guess.

multiply = input("What's 5 x 7?")
if multiply == 35:
    print 'You got it'
else:
    print 'Not correct. The answer is 35'

# 3. Enhance the multiplication game so that the two numbers are random between 1 and 10.  To do this, first put ‘from random import randint’ and then you can set the random numbers like ‘a=randint(1,10)’
upper_bound = int(raw_input("What's the largest number you'd like to choose?"))

from random import randint

answer = randint(0, upper_bound)

print "Ok, now choose a number between 1 and " + str(upper_bound)
guess = int(raw_input("What's your guess?"))
score = 0
while guess != answer:
    # Got it to give me feedback!
    if guess>answer:
        print "Your guess is too high!"
        score = score + 1
    else:
        print "Your guess is too low!"
        score = score + 1
    guess = int(raw_input("What's your guess?"))
score = score+1
print "Great job, " + user_name + ", the number was " + str(answer) + ". It only took you " + str(score) + " tries."
# print randint(0,upper_bound) so, that works
