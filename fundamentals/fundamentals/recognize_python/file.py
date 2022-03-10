num1 = 42 #variable declaration, data type:  primitive: numbers
num2 = 2.3 #variable declaration, data type: primitive: numbers
boolean = True #variable declaration, data type: primitive: boolean
string = 'Hello World'#variable declaration, data type: primitive: string 
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']# variable declaration, data type: composite: list of strings: initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration, data type: composite: dictionary initialize with keys of strings and values of data type: string, string, number, boolean
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration, data type: composite: initialize a tuple of strings

print(type(fruit)) #log statement type check of tuple fruit
print(pizza_toppings[1])#log statement accessing value of the first index of pizza_toppings list
pizza_toppings.append('Mushrooms') #adding value of a string named 'Mushrooms' to the end of the pizza_toppings list
print(person['name']) #log statement accessing the dictionary called person for the value that corresponds to the key 'name'
person['name'] = 'George' #changing the value in the dictionary called person that corresponds with the key 'name' to 'George'
person['eye_color'] = 'blue' #adding the value in the dictionary called person that corresponds with the key 'eye_color_ to 'blue'
print(fruit[2]) #log statement accessing the value in the 2nd index of the tuple called fruit, which is banana

if num1 > 45: #conditional if statement for variable num1
    print("It's greater") #log statement of a string if conditional statement on previous line is met
else: #conditional else statement that is run if previous conditional statement isn't met
    print("It's lower") #log statement of a string if the if conditional statement isn't met

if len(string) < 5: #conditional if statement with a length check of the variable string, will run if length of string is less than 5
    print("It's a short word!") #log statement if conditions of the above if statement are met will log this string
elif len(string) > 15: #conditional else if statement with a length check of the variable string, will run if the first conditional statement isn't met and these conditions are met
    print("It's a long word!") #log statement if conditions of the above else if statement are met will log this string
else: #conditional else statement that will run if the first two conditional statements aren't met 
    print("Just right!") #log statement if conditions of the above if and else if statement aren't met it will log this string

for x in range(5): #for loop for a variable x, starting at 0, running as long as x is less than 5, incrementing by 1
    print(x) #log statement will log value of x for every time the loop runs and the conditions of the loop are met
for x in range(2,5): #for loop for a variable x, starting at 2, running as long as x is less than 5, incrementing by 1
    print(x) #log statement will log value of x for every time the loop runs and the conditions of the loop are met
for x in range(2,10,3): #for loop for a variable x, starting at 2, running as long as x is less than 10, incrementing by 3
    print(x) #log statement will log value of x for every time the loop runs and the conditions of the loop are met

x = 0 #variable declaration date type: primitive: numbers
while(x < 5): #while loop for a variable x, starting at 0, running as long as x is less than 5, incrementing by 1
    print(x) #log statement will log value of x for every time the loop runs and the conditions of the loop are met
    x += 1 #increment x by 1 before running the loop again

pizza_toppings.pop() #using the pop function with no parameter so default to removing the last value in the list pizza_toppings, which is olives
pizza_toppings.pop(1) #using the pop function, will remove the value in the first index of the list pizza_toppings, which is sausage

print(person) #log statement for the dictionary called person
person.pop('eye_color') #using the pop function to remove the key eye_color and it's corresponding value from the dictionary called person
print(person) #log statement for the dictionary called person

for topping in pizza_toppings: #for loop that runs through the topping values in the list pizza_toppings
    if topping == 'Pepperoni': #conditional if statement that is met is the topping value is pepperoni 
        continue #continue keyword to end the current iteration of the for loop and continue directly on to the next iteration 
    print('After 1st if statement') #log statement of a string that will log if the topping value in the pizza_toppings list is not pepperoni
    if topping == 'Olives': #conditional if statement that is met is the topping value is olives 
        break #break keyword to end the for loop when this break line is met

def print_hello_ten_times(): #defining a function with no parameter
    for num in range(10): #for loop for a variable called num starting at 0, running as long as num is less than 10, incrementing by 1
        print('Hello') #log statement of a string that will log every time the conditions of the for loop are met

print_hello_ten_times() #calls the function while passing on no arguments, will log the print statement as many times as defined by the for loop in the function

def print_hello_x_times(x): #defining a function that will pass in a value for the parameter x
    for num in range(x): #for loop for a variable called num starting at 0, running as long as num is less than x, incrementing by 1
        print('Hello') #log statement of a string that will log every time the conditions of the for loop are met

print_hello_x_times(4) #calls the function while passing in the number 4 as an argument that will take the place of x, will log the print statement as many times as defined by the for loop in the function

def print_hello_x_or_ten_times(x = 10): #defining a function that will pass in a value for the parameter x where x = 10
    for num in range(x): #for loop for a variable called num starting at 0, running as long as num is less than x which is 10, incrementing by 1
        print('Hello') #log statement of a string that will log every time the conditions of the for loop are met

print_hello_x_or_ten_times() #calls the function while passing on no arguments, will log the print statement as many times as defined by the for loop in the function
print_hello_x_or_ten_times(4)#calls the function while passing in the number 4 as an argument taking the place of x = 10, will log the print statement as many times as defined by the for loop in the function

#line below starts a multiline comment
""" 
Bonus section
"""
#line above the the multiline comment

#all bonus material is commented out with single line comments, for purpose of this exercise I will uncomment them out making them active so comments can be applied
print(num3) #log statement produces a NameError: name <variable name> is not defined, the variable num3 is not defined and cannot be printed
num3 = 72 #variable declaration, data type: primitive: numbers. sets num3 to be 72, but will not help previous line run as it needs to be defined before it is printed
fruit[0] = 'cranberry' #trying to change a tuple value, TypeError: 'tuple' object does not support item assignment, fruit is a tuple and tuples are immutable
print(person['favorite_team']) #log statement trying to access dictionary key that does not exist  KeyError: 'favorite_team' the favorite team key does not exist and cannot be accessed to print from
print(pizza_toppings[7]) #log statement IndexError: list index out of range, the list pizza_toppings only has indices 0-3, cannot access index 7 because it does not exist
    print(boolean) #log statement with improper indentation, IndentationError: unexpected indent,
fruit.append('raspberry') #fruit is a tuple and cannot be appended to add a value to, AttributeError: 'tuple' object has no attribute 'append'
fruit.pop(1) #fruit is a tuple and cannot be popped to remove a value from it, AttributeError: 'tuple' object has no attribute 'pop'
