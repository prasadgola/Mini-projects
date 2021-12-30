def rotate(l, x):
  return l[-x:] + l[:-x]
l = [1,2,3,4,5,6,7]
print(rotate(l,1))
