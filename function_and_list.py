#Write your function here
def double_index(lst, index):
  if len(lst)>index and index>=0:
    lst[index]*=2
    return lst
  else:
    return lst
print(double_index([3, 8, -10, 12], 2))
