digits = [1,2,3,4]
for i in  range(0,len(digits)):
    digits[i] = str(digits[i])
d = "".join(digits)
w = int(d) + 1
print (str(w))