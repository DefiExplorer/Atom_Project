# User defined function
def add(a, b): # Function definition, where a and b are parameters
    return a + b # Function declaration_or what it does
def sub(a, b): #don't forget to put colon ':'
    p = a-b
    return p
p = float(input('Enter any +ve number ')) # No problem using the same variable name if previously defined in function.
q = float(input('Enter other +ve number '))

print ('Your entries are ', p, q)

r = add(p, q) # called the function defined above
print (r)
print (sub(p, q))
