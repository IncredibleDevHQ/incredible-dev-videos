# Operators in Python - Part 3
# Logical Operators
Alice , Bob = 12 , 27
# and 
print( Alice>10 and Alice<20) # True and True = True
print( Alice>10 and Bob<20) # True and False = False
# True only if both are true , else false

# or 
print( Alice>10 or Alice<20) # True or True = True
print( Bob<20  or Alice<20 ) # False or True = True
print( Bob<20 or Alice<10 )  # Flase or False = False

# not 
print(not Alice<10) # not (False) = True
print(not Bob>20) # not (True) = False