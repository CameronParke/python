#Basic - Print all integers from 0 to 150.
x = 0
for x in range (0, 151):
    print(x)



#Multiples of Five - Print all the multiples of 5 from 5 to 1,000
x = 5
for x in range (5, 1001, 5):
    print(x)



#Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
x = 1
for x in range (1, 101):
    if x % 5 == 0 and x % 10 == 0:
        print("Coding Dojo")
    if x % 5 == 0 and x % 10 != 0:
        print("Coding")
    elif x % 5 != 0 and x % 10 !=0:
        print(x)



#Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
x = 1
sum = 0
for x in range (1, 500000, 2):
    sum = x + sum
print(sum)




#Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
x = 2018
for x in range (2018, 0, -4):
    print(x)



#Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lowNum = 3
highNum = 16
mult = 4
x = 3
for x in range (3,17):
    if x % mult == 0:
        print(x)