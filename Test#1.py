a = 'alpha Numeric string is 12345'
print (a.isalnum()) # AlphaNumeric string dosen't contain space, So this will result in FALSE.
print(a.count('i'))
Num = int(input('Enter any integer value: '))
print ('You entered', Num)
sum = Num + a.count('i')
print (sum)
m = a.split(' ')
print (m, 'The number of elements in this list m is: ', len(m))

s = 'R a h u l '
print ('The length of the string is: ', len(s))
#space is counted in the string count using len.
