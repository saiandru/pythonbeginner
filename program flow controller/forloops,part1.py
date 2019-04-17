#the range of output goes from 1 to 19 not 20
#the last value specifed not included
for i in range(1,20):
    print("i is now {}".format(i))

#above format is the latest way to indication and below is old model of decimanl reperesntation
for i in range(1,20):
    print("i is now %d" %(i))



number="9,223,372,036,854,775,807" 
for i in range(0,len(number)): #len means links of string 
    print(number[i])


number = "9,223,372,036,854,775,807"
for i in range(0, len(number)):  # len means links of string
    if number[i] in '0123456789':  # with this we excluded comma in this
       # print(number[i])  
# here print is automatically skippng to next line
# this made the automatically skipping to next line to end in one single line
        print(number[i], end='')
    #we have overwrtiten the basic and modified according to our output. now the output in one single integer

#to convert a string to integer having numberical
#here we have done concatenation


number = "9,223,372,036,854,775,807"
cleanednumber = '' #here the value of interget getting stored in string format 

for i in range(0, len(number)):
    if number[i] in '0123456789':
        cleanednumber = cleanednumber + number[i]

newnumber = int(cleanednumber)
print("/n")
print("the nummber is {}".format(newnumber)) #now we get proper interget format output 

extra='123244'
#or extra="12344"
rawthing=int(extra) #here we are converting above string character to integer with single notation 
print("the number is {}".format(rawthing))
