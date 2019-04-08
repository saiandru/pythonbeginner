greeting="bruce"
#above varibale is like box and name it contains is bruce
#valid variables are
_myname="tim"
tim45="good"
tim_aws_57="hello"

age=24
print(age)

#print(greeting + age)
#above doesnt print as string cant concatenate with integer

#python got many data types
#string being sequence types

a=12
#above is integer number
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
#in pyuthon it generates float numer genrallyu in aboe type of cases so we use double slashes
print(a//b)
print(a%b)

#range needs an integer if we use 4 inplace of a/b 4.0 output above doenst work so only we use a//b
for i in range(1,4):
    print(i)
    exec
#in python works based on higher value of operator
print(a + b /3 -4 * 12)
print(8*3/2)
print((((a+b)/3)-4)*12)

#we can split abve into different variables and get output as we desire
c=a+b
d=c/3
e=d-4
print(e*12)



#data types
parrot="Norwegian blue"
print(parrot)
#the count generally starts at 0 so we get W here as output
print(parrot[3])
print(parrot[0])
#the below we get error as its out of string value given
#print(parrot[14])

#we can print backwards from ened to start
print(parrot[-1])

#we can print string from the avalable string and gives till before the last postion mentioned here n-1
print(parrot[0:6])
#or 
print(parrot[:6])
#belo gives output till end starting from position 6
print(parrot[6:])
#the below one doenst give any output as negative to postiviit
print(parrot[-4:2])
#the belo we get outpt and same indication
print(parrot[-4:-2])

#to skip the sequence and down 6 is marking till the end of it and it skips 2 charcater till 6 position exclusinf n-1
print(parrot[0:6:2])

print(parrot[0:6:3])
#below are the stirng in nukbers accordingly 
number="9,223,372,036,854,755,807"
print(number[1::4])

numbers="1,2,3,4,5,6,7,8,9"
print(numbers[0::3])

string1="he's "
string2="probably "
print(string1+string2)
print("he's" "probably" "pining")
#the below hello is printed 5 times
print("hello" *5)
#use below to get desired output
print("hello" * (5+4))
#as string and integer cant be addeed make the integer as string using notations
print("hello" * 5 + "4")

today="friday"
#we get boolean output as "in" checks the value in today and gives boolean output of true or false
print("day" in today)
print("fri"in today)
print("thu" in today)
print("parrot" in today)



