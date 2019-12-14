# Write your always_false function here:
def always_false(num):
  if num in [1,2] and num not in [1,2]:
      # We can use 'in' for comparision with the items in list and
      #'not in' for excluding things from list.
    return True
  else:
    return False
# Uncomment these function calls to test your always_false function:
print(always_false(0))
# should print False
print(always_false(-1))
# should print False
print(always_false(1))
# should print False
