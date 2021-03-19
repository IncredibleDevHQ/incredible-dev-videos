# Strings Part-1 - Definition,casting and indexing
my_string = "Python101!"
another_string = 'Welcome '
# quoting the quote !
dialog = 'He asked , "But sir, python is a snake?!" '
reply = "Monty replied , 'Of course it is.' " 

# Casting!
txt_num = str(123)
print(txt_num) # output : '123'

# Indexing
letter = my_string[0]
print(letter) # output : 'P'
print(my_string[3],my_string[7]) # output : h 0
my_string[0] = "p" 
# TypeError: 'str' object does not support item assignment !