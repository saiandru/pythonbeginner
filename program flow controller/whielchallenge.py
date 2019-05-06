# import random

# highest = 10
# answer = random.randint(1,highest)

# print("please guess a nuber between 1 and {}".format(highest))
# guess = int(input())
# if guess !=answer:
#     if guess < answer:
#         print("please guess higher")
#     else:
#         print("please guess lower")
#     guess = int(input())

#     if guess == answer:
#         print("well done,you giuessed it")
#     else:
#         print("sorry, you have not guessed correctly")
# else:
#     print("you got it first time")


import random

highest = 10
answer = random.randint(1,highest)

print("please guess a nuber between 1 and {}".format(highest))
guess = 0 #initlaize to any number outosiude of the valid range
while guess !=answer:
    guess = int(input())
    if guess == 0:
        break
    if guess < answer:
        print("please guess higher")
    elif guess > answer:
        print("please guess lower")
    else:
        print("well done,you guessed it")
else:
    print("you got it first time")
