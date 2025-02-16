# when declaring string,you can use both single or double quotes

#print("I'am going on a run")

#print(len('hello'))

# mystring = 'Hello World'
# print(mystring[0])
# print(mystring[8]) #indexing
# print(mystring[-2]) #reverse indexing

# mystring = "abcdefghijk"
# print(mystring[2])
# print(mystring[2:]) # slicing from index 2 to end of the string
# print(mystring[:3]) # index 3 ('d') is not included in the slice
# print(mystring[3:6]) # 'def'
# print(mystring[::]) # it takes all string - all the way from beginning to end with stepsize 1 (default)
# print(mystring[::2]) # all the way from beginning to end with stepsize 2
# # [start:end:stepsize]
# print(mystring[::-1]) # reverse string - good trick :)

#Immutability
# name = "Sam"
# #name[0] = 'E' #TypeError: 'str' object does not support item assignment
# last_letters = name[1:]
# print('P' + last_letters) #String concatenation

# letter = 'z'
# print(letter*10) # String multiplication

# x = 'Hello World'
# print(x.upper()) #it does not change the original one
# print(x)
# x = x.upper() #now original one is changed
# print(x)
# print(x.lower())
# print(x.split())

# x = 'Hi this is a string'
# print(x.split('i')) # split according to given character
# #split() -> create lists
# x = "This is a string {}"
# print("This is a string {}".format('INSERTED'))
# print(x.format('INSERTED')) # it does not insert the original string
# print(x)

# print('The {2} {1} {0}'.format('brown','fox','quick'))
# # 'The quick fox brown'
# print('The {0} {0} {0}'.format('brown','fox','quick'))
# # 'The fox fox fox'
# print('The {one} {two} {three}'.format(one='brown',two='fox',three='quick'))
# # 'The brown fox quick'

# result = 100 / 177 
# print(result) # 0.5649717514124294
# print("The result was {r:1.3f}".format(r=result)) # 0.565

# new_result = 104.12345
# print('the result was {r:1.2f}'.format(r=result))
# # 104.52

# name = 'Ege'
# print(f'Hello, my name is {name}')
# # Hello, my name is Ege

# name = 'Sam'
# age = 3
# print(f'{name} is {age} years old')

