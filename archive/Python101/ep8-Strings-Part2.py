# Strings Part 2 - Concatenation and String functions
sub = "I love "
itm = "Python"
msg = sub + itm 
print(msg) # output : I love Python

# String Functions
print(msg.upper()) # output : 'I LOVE PYTHON'
print(msg.lower()) # output : 'i love python'
print(sub.islower()) # output : False

print( dir(str) )
""" Output : [ ... , 
'isalnum', 'isalpha','join', 'ljust', 'lower', 'lstrip',
 ....] """