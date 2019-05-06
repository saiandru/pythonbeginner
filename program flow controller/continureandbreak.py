shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
for item in shopping_list:
    if item == 'spam':
        # print("iam ignoting"+ item)
        continue  # here it bypasses or stops processing that particular block of code if match is found
    print("Buy" + item)

shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
for item in shopping_list:
    if item == 'spam':
        # print("iam ignoring"+ item)
        break  # here it breaks the for loops and exitis out of loop
    print("Buy" + item)


meal=["egg","bacon","spam","sausages"]

for item in meal:
    if item == 'spam':
        nasty_food_item=item
        break #here break is useful to stop the matching iteration out of loop and go to next step
        #if we have thousand of items to search and breaking is useful in this to stop for perfect matching and exiting the loop
        #to terminate loop earlier for matching condition.

if nasty_food_item:
    print("cant I have anything without spam in it")


meal = ["egg", "bacon", "tomato", "sausages"]
nasty_food_item = '' #if we mention a vaibale outside of loop of befre we can correct the code for no match below
for item in meal:
    if item == 'spam':
        nasty_food_item = item
        break

if nasty_food_item:
    print("cant I have anything without spam in it")
else:
    print("choose one")


meal = ["egg", "bacon", "beans", "sausages"]
nasty_food_item = '' #if we mention a vaibale outside of loop of befre we can correct the code for no match below
for item in meal:
    if item == 'spam':
        nasty_food_item = item
        break

else: #here else works only if never breaks from above block 
    print("I'll have a plat of that,then,please")

if nasty_food_item == "spam":
    print("cant I have anything without spam in it")

