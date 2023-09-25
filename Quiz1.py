# Question 1
x = float(input())

# Add code below...
import numpy as np

y_Numer = (10 + np.sin(x) + pow(x,2) + np.cosh(pow(x,2) + 1))
y_Denomin = (np.sinh(x) + pow(x,3) + 3 * pow(x,4)+ np.exp(x))
y = y_Numer / y_Denomin

Y = round(y,3)

# Question 2
speed_mph = float(input())

# Add code below...
speed_ms = round(speed_mph * 1609.34 / 3600)# rounded to the nearest integer.

# Question 3
my_string = input()

# Add your code below...
L = len(my_string)
first = my_string[0]
second_to_last = my_string[-2]

# Question 4
n = int(input())

# Add code below...

#To judge if the input satisfies the multiples of 3, 5, 7
isMultiple_3 = (n%3==0) #define boolean variable
isMultiple_5 = (n%5==0)
isMultiple_7 = (n%7==0)

#using placeholder to insert number and boolean.
print("Is %d a multiple of 3? %s" % (n, isMultiple_3))
print("Is %d a multiple of 5? %s" % (n, isMultiple_5))
print("Is %d a multiple of 7? %s" % (n, isMultiple_7))