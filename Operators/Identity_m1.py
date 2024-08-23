x=["apple","banana"]
y=["apple","banana"]
z=x
print(x is z)
print(x is y)
# To demonstrate the diff. b/w "is" and "==": 
# This comparision returns true bcz x is equal to y
print(x == y)
print(x is not y)
print(x is not z)
