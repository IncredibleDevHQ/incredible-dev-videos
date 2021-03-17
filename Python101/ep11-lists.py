# Beyond variables 
vowel = 'a'
vowel = 'e'
print(vowel) # Output : 'e'

vowels = ['a','e','i']
nums = [1 , "two" , 3 , "four" ]

vowels.append("d") # ['a', 'e', 'i', 'd']
vowels.remove("d") # ['a', 'e', 'i']
vowels.extend(["o","u"]) # ['a', 'e', 'i', 'o', 'u']
print( dir(vowels) )
#  [...,'clear','copy','count','index','insert',
#   'pop','reverse','sort', ... ]
