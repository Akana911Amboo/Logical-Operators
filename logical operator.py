# Example 1
x = 5
print(x < 3 and x < 10) # True because both conditions are true

# Example 2
y = 12
print(y > 10 and y % 5 == 0) # False because the second condition is false 

# Example 1
x = 5 
print(x < 3 or x > 10) # False because bith the condition are false

#Example 2
y = 12
print(y < 10 or y % 2 == 0 ) # True because the second condition is true

# Example 1
x = 5
print(not(x > 10 and x % 5 == 0 )) # True because the condtions inside the not is false 

# Example 2
y = 12 
print(not(y > 3 and y < 10 )) # False because the condition inside the not is true   