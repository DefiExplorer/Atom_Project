# Nested
a = int(input("Enter 1st-integer number"))
b = int(input("Enter 2nd-integer number"))
c = int(input("Enter 3rd-integer number"))
# symbolic execution ~ is testing using one variable of program.
if a>b:
    if a>c:
        print (a, 'is greatest')
    else:
        print (c, "is greatest from line 9")
elif b>c:
    print (b, 'is greatest')
else:
    print (c, 'is greatest from line 13')
# It's better when 'if' is written once in for a block, use 'elif' if required.
