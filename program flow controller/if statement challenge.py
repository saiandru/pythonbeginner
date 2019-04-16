#write a small program to asm for a name and age
#when both values have been entered ,check if the person 
#is the right age to go an 18-30 holiday(they must be
# over18 and under 31)
#if they are ,welcome them to the holiday,otherwise print
#a (polite) message refusing them entry.
name = input("please enter your name")
age = int(input("how old are you?"))

if (age < 18) or (age>31):
    print("you cant go for holiday {0}".format(name))
else:
    print("you can go for holiday {0}".format(name))
