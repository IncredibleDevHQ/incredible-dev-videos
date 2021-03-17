# Strings Part 3 - String Formatting
location = "the zoo"
newString = "I visit %s every year." % location
print(newString) 
# output : 'I visit the zoo every year.'

newString = "It took me %d hours to get here on %s " %(2,"Tuesday")
print(newString) 
# output : 'It took me 2 hours to get here on Tuesday '

float_string = "%f" % (1.23)
print(float_string) # output : '1.230000'

float_string2 = "%.2f" % (1.23)
print(float_string2) # output : '1.23'

float_string3 = "%.2f" % (1.237)
print(float_string3) # output : '1.24'