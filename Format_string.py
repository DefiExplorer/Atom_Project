f = str(input('Enter your name: '))
l = str(input('Enter your last name: '))

output = 'Hello, {} {}'.format(f, l)
#Change in order
out = 'Welcome Mr. {1} {0}'.format(f, l)
#Yet another way
out2 = f'How are you?, {f} {l}'

print (output)
print (out)
print (out2)
#More on format at site https://pyformat.info/
