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