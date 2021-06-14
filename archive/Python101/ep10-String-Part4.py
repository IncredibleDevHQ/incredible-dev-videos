# Strings Part 4 - String Formatting 
r = "red"
b = "blue"
g = "green"

s = "My favorite colors are {0}, {1} and {2}".format(r , g , b)
print(s) # 'My favorite colors are red, green and blue'

s = f"My favorite colors are  {r} , {g} and {b}"
print(s) # 'My favorite colors are red, green and blue'