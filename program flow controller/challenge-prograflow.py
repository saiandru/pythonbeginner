# create a program that takes an ip address enteres at the keyboard and prints
# out the number of segements it contains and length of each segment 
# and validity of ip address

ipadress = input("please enter an ip adress")
if ipadress[-1] != '.':
    ipadress += '.'
segment = 1
segment_length = 0
# adress = '' #or ""

for adress in ipadress:
    if adress == '.':
        print("segment {0} is segmentlength is {1}".format(segment,segment_length))
        segment += 1
        segment_length = 0
    else:
        segment_length += 1
#unless the final character in the string was a . then we havent pornted the last segment
# in python output of forloop can be utlized in below if condition
# if adress != '.':
#     print("segment {} is segmentlength is {}".format(segment,segment_length))

#to split a line in () of input we can use \ this backslash and split the line. 


