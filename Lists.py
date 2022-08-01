def separator():
    print( "******\n")

my_list = ["Cherry", "Apple"]

print(f"the initial list {my_list}")
separator()
# Add an item to the list
my_list.append("Pear")

print(f"adding a pear {my_list}")
separator()
# get the first Item
print(f"The first item in the list is {my_list[0]}")

# print the last item in the list
print(f"The last item in the list is {my_list[-1]}")
separator()
# remove to assignment from list
print(f"the current list {my_list}")
print(f"get the second item :{my_list.pop(1)}")
print(f"The new list {my_list}")
separator()
additional_list = ["pineapple", "coconut", "lemon"]

# add one list to another to the right
print(f"initial list {my_list}")

my_list.extend(additional_list)
print(f"The updated list {my_list}")
separator()
# add to the left
my_list[:0] = ['avocado', 'grapes']
print(f"added to the left {my_list}")
separator()
# insert one somewhere
my_list.insert(3, "strawberry")
print(f"Added strawberry to position 4 : {my_list}")
separator()
# iterate over a list
for fruit in my_list:
    print(f"a fruit is : {fruit}")
separator()

# sort the list
print(f"unsorted list is {my_list}")

print(f"sorted list is {sorted(my_list)}")
# can you determine the sort that was used

print("Sorting can also be done with lambda functions")
my_list.sort(key = lambda fruit : len(fruit))
print(my_list)
separator()

# Methods that come with lists
print(f"is there a banana in there {'banana' in my_list}")
print(f"Is there NO banana in there {'banana' not in my_list}")
separator()

#finding things in there
print("Can look at lists to get information out ")
print(f"there are {len(my_list)} fruits in the list, there is "
      f"{my_list.count('strawberry')} strawberry(s) in there and can be found at index {my_list.index('strawberry')}")
separator()

print("Looking at list comprehension")

# Syntax for list comprehension
# newlist = [expression for item in iterable if condition == True]

# The following uses the for loop and squares the value and loads it into a new list
print("using a for loop to pass to a square operation ")
squared_list = [num ** 2 for num in range(1, 11)]
print(f"The squared list is {squared_list}")
separator()
# given a list of numbers make a new list of evens

just_evens = [value for value in squared_list if value % 2 == 0]
print(f"Getting the even values from the list {just_evens}")
separator()

#Concatonating strings being passed from a loop
my_list = ['tasty ' + fruit for fruit in my_list]
print(f"Looking at the change on the first element {my_list[0]}")
separator()


#slicing
print(f"original list {my_list}")
print(f"slicing , the original is to return a value at index: {my_list[0]}")
print(f"my_list[1:2] :{my_list[1:2]}")
print(f"my_list[0:3:2] :{my_list[0:3:2]}")
print(f"my_list[0:4:2 : {my_list[0:4:2]}")
print(f"my_list[0:5:2 : {my_list[0:5:2]}")
print(f"my_list[::-1] :{my_list[::-1]}")
print(f"my_list[::-2] :{my_list[::-2]}")
separator()

#Using map with list
print("using maps with list ")
string_list = ['1','4','55', '7', '888', '9']
print(f"the list of strings to convert : {string_list}")
numbers_list = list(map(int, string_list))
print(f"the resultant of the map operation, converted back to list : {numbers_list}")