#to execute block of code
for i in range(10):
    print("i is now {}".format(i))


# the above output we can produce with while loop

i=0 #conditon instilaized
while i<10:
    print("i is now {}".format(i))
    i += 1 #incremented to stop infinte looping and to make condition to false after certain. 

#while loop importance below
#one application is to read  data from a file.
available_exits = ["east", "northeast", "south"]

chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("please choose a direction: ")
    if chosen_exit == "quit":
        print("game over")
        break 
else:
    print("arent you glad you got out of thjere!")

