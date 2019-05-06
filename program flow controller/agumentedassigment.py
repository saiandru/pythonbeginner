number = "9,223,372,036,854,775,807"
cleanednumber = '' #here the value of interget getting stored in string format 

for i in range(0, len(number)):
    if number[i] in '0123456789':
        cleanednumber += number[i] #agumentedassignmenet happened here in python its more effiecient and we can save resorces

newnumber = int(cleanednumber)
print("/n")
print("the nummber is {}".format(newnumber))


x=23
x += 1
print(x)

x -= 4
print(x)

x *= 5
print(x)

x /= 4
print(x)

x **=2 #here its indicates power of
print(x)

x %= 60 #chekcing for remainder
print(x)


greeting="good"
greeting += "morning"
print(greeting)

greeting *=5
print(greeting)




