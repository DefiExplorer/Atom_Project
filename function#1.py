# More on functions
# Getting user name and age, also printing the number of letters in their name.
def get_(name, age):
    print ('Name:', name.title()) #no matter how user enters their name.
    print ('Age:', age)

N = str(input('Type name : '))
A = int(input('Type age in Yrs only : '))
print (get_(N, A)) #function call

def count(name): #counts the length of name
    return len(name)
    # Tried nested function- but didn't work

def space(name): #function to minus spaces from name length.
    return name.count(' ')
y = count(N) - space(N)
print ('The number of letters in the given name is', y, 'The previous count was', count(N), 'which is incorrect as it includes spaces.')
# We can define as many functions as we want to.
# Ask why the output prints 'none' after Age...in next line?
