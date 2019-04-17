number = "9,223,372,036,854,775,807"
cleanednumber = ''

for char in number: #reduced the amount of code char in number and we are not using "i" number anymore
    #here variavle char has list of numbers
    if char in '0123456789':
        cleanednumber = cleanednumber + char

newnumber = int(cleanednumber)
print("the number is {}".format(newnumber))

for state in ["not pining'","no more","a stiff","berefit of lift"]: #give in array format to the variable state 
    #here range we are sequence type
    print("this parrot is"+ state)
    #print("this parrot is {}".format(state))


for i in range(0,100,5): #here 5 is step a head kind
    print("i is {}".format(i))

#here we can do nested for loops as well.
for i in range(1,13):
    for j in range(1,13):
        print("{1} times {0} is {2}".format(i,j,i*j))
        #print("{1} times {0} is {2}".format(i,j,i*j, end='\t')) here we get in horizantal mode
        #print('') this thing give spaces and empty string
    print("==================")

#fo specific table multiplication in python
j=int(2)
for i in range(1,13):
    print("{1} times {0} is {2}".format(i,j,i*j))
print("==================")



