# 1. TASK: print "Hello World"
from inspect import BlockFinder
from sys import builtin_module_names
from urllib.request import parse_keqv_list


print("Hello World")
# 2. print "Hello Cameron!" with the name in a variable
name = "Cameron"
print("Hello", name, "!")	# with a comma
print("Hello" + name + "!")	# with a +
# 3. print "Hello 13!" with the number in a variable
name = 13
print("Hello", name, "!")	# with a comma
print("Hello" + str(name) + "!")	# with a +	-- this one should give us an error!
# 4. print "I love to eat fried chicken sandwiches and cheeseburgers." with the foods in variables
fave_food1 = "fried chicken sandwiches"
fave_food2 = "cheeseburgers"
print("I love to eat {} and {}." .format(fave_food1, fave_food2)) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}.") # with an f string

first_name = "Cameron"
last_name = "Parke"
age = 33
eye_color = "blue"
hair_color = "blond"
home = "Worcester, Massachusetts"
live_in = "Chicago, Illinois"
print ("My name is {} {} and I am {} years old. I have {} hair and {} eyes. I am from {}, but I currently live in {}".format(first_name, last_name, age, hair_color, eye_color, home, live_in))