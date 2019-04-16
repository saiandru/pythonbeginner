name = input("please enter your name")
#below we have given number instead of string as if we dont use int then only input("how old are you,{0}?".format(name) then this is like string
#to have specific data type we used int as to represent the age in number
age = int(input("how old are you,{0}?".format(name)))
print(age)

if age >= 18:
    print("your are old enough to vote")
    print("please put an X in the box")
else:
    print("please come back in  {0} years to vote".format(18-age))


print("please guess anumber between 1 and 10: ")
guess = int(input())

#below if and else condition used indentation is very important 
#guess<5 and guess==5 are part of one if and elif another as identation is important
#we can do more of if,else blocks based on code complexity
if guess < 5:
    print("please guess higher")
    guess = int(input())
    if guess == 5:
        print("well done, you guessed it")
    else:
        print("sorry,you have not guessed correclty")
elif guess > 5:
    print("please guess lower")
    guess = int(input())
    if guess == 5:
        print("welldone,you have guessed it")
    else:
        print("sorry, you ave not guessed correclty")
else:
    print("you got it first time")

if guess != 5:
    if guess <5:
        print("please guess higher")
    else: #guess must be greater than 5
        print("please guess lower.")

#below new guess mentioned is not indentatio of above code
    guess = int(input())
    if guess ==5:
        print("well done, you have guessed coreectly")
    else:
        print("sorry,you ave not guessed correctly")
else:
    print("you got it first time")
