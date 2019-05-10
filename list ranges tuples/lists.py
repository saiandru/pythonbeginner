# python provides 6 different types built in sequnces
#  1. list
#  2. ranges
#  3. tuples
#  4. 3 binary sequence types

ipadress = input("please enter an ipadress: ")
print(ipadress.count("."))

#here above count syntax working procedure is s.count(x) total number of occurence of x in s

#list is a sequence of things similar to strings
parrot_list = ["non pinin", "no more", "a stiff", "berefet of live"]
parrot_list.append("A norwegian blue") #it appends to above list and oiutput will be in last 
for state in parrot_list:
    print("this parrot is" + state)



even = [2,4,6,8]
odd = [1,3,5,7,9]

numbers = even + odd #here we have numbers list
# numbers.sort() #it returns sort list 
print(numbers)
# print(numbers.sort()) #we wont get noting as output as none this doenst work ...it works on exsisting object doenst create new object

# print(sorted(numbers)) #buitl in function it chnegs the output object its different to .sort() 

numbers_in_sorted = sorted(numbers)
print(numbers_in_sorted)

if numbers == numbers_in_sorted:
    print("lists are equal")
else:
    print("the lists are not queal")

if numbers_in_sorted == sorted(numbers):
    print("the lists are queal")
else:
    print("the liast are not queal")


# ---------------------------
# more on lists

list_1 = []
list_2 = list()

print("list 1: {}".format(list_1))
print("list 2: {}".format(list_2))

if list_1 == list_2:
    print("the lists are equal") #here we are passing parameteres in to print argument

#all sequcnec built in to python are iterable

print(list("the lists are equal"))

#the constructors are created list in above 

even = [2,4,6,8]
another_even = even
#another_even = sorted(even, reverse=True) even tis is valid type
#another_even = list(even)  #now below print gives false output
print(another_even is even) #here it gives boolean value true or fale as output
another_even.sort(reverse=True)
print(even) #here both are  even and another_even is same and we havent updated even directly indirectly updated through another_even
#another_even refere to exact same list


even = [2,4,6,8]
odd = [3,5,7,9]
numbers = [even, odd] # gives two lists in one list
for number_set in numbers:
    print(number_set)

    for value in number_set:
        print(value)



