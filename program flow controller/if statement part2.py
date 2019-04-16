age = int(input("how old are you?"))

#if (age >=16) and (age<=65):#here its looking in range of 16 and 65
#using paranthesis makes it easir to undertsand the code
#if 16 <= age <= 65:
    #or if 15< age < 66:
 #   print("have a good day at work")
if (age < 16) or (age>65):
    print("enjoy your free time")
else:
    print("have a good day")


#in python boolean false and true are set withj condtion parameters
x= input("please enter sometext ")
if x:
    print("you entered '{}'".format(x))
else:
    print("you did not enter anything")


#print(not False) # this gives output as true 
#print(not True)

if not(age<18): #here checks the false of true inverse here not acts as boolena here to check the string/sequec of characters
    print("you are old enough to vote")
    print("please put an xin the box")
else:
    print("please come back in {0}".format(18 - age))


parrot ="norwegain blue"

letter=input("enter an character: ")
if letter in  parrot: #here check the value entered in letter to parrot in string format 
    #above can be like this also "if letter not in parrot:" then need to chnange the below print reverse
    print("give me an {},bob".format(letter))
else:
    print("i dont need that letter")
