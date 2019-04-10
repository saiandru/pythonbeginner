age=24
#str is converting the bracket inside value to string
print("my age is " + str(age) + "years")

#here {0} takes the value from format like array kind of thing i.e 0:str pointing
print("my age is {0} years".format(age))

#output for below is thee are 31 days in jan,mar,may,jul,aug,octanddec
print("thee are {0} days in {1},{2},{3},{4},{5},{6}and{7}".format(31,"jan","mar","may","jul","aug","oct","dec"))

#below kind of procediure introduced in python3
print("""Jan:{2}
feb:{0}
mar:{2}
apr:{1}""".format(28,30,31))


#below is old formt of strings and d mean decimal i.e %s acts a placeholder for a string while %d acts as a placeholder for a number.
print("my age is %d years" %age)
#below multiple replacements can be done here %s is string 
print("my age is %d %s, %d %s" % (age,"years",6,"months"))

#in the below %2d mean add 2 spaces and %4d mean add 4 spaces in the output so that output looks neat in format
for i in range(1,12):
    print("no.%2d squared is %4d and cubed is %4d" %(i,i ** 2,i ** 3))

#we can get precise output as %12.50 means upto 50 decminal points print the output and f mean floating indication
print("Pi is approx %12.50f" %(22/7))

#go to site for more on string formating docs.oython.org/2.4 we get more for older version python2

#in below output {0:2} mean 0 is the value of i and 2 is the width likewise for {1:4} mean 1 is the value of i**2 and 4 is the width
for i in range(1,12):
    print("no. {0:2} squared is {1:4} and cubed is {2:4}".format(i,i ** 2,i ** 3))


#in the below <4 mean numbers always start on lefthand side
for i in range(1,12):
   print("no. {0:2} squared is {1:<4} and cubed is {2:<4}".format(i,i ** 2,i ** 3))

#below is the new format to old format replacement fields of using format 
print("Pi is approx {0:12.50}".format(22/7))

#here below is auto matically asumes 1st is in first and second is in seconf and so on in python3
for i in range(1,12):
    print("no. {} squared is {} and cubed is {:4}".format(i,i ** 2,i ** 3))

