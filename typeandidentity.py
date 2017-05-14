# everything in Python is an object
# including ints and floats
# 42 for example has its own id within python
# x = 42 will make x hold the same id as 42
#id(x) -> will provide x's id and type(x) -> will provide the class of x
# equality -> x==y
# to check if two things are the same (same id's that is) you do "x is y"
# BUT, for mutable objects such as a dictionary, the id's will change. x = dict(x=42)
# y =dict(x=42). x == y but x is y will be False as dictionaries are mutable. 

# bool, int, float, tuple, str, frozenset are all immutable objects. 
# In java on the other hand int, float, and so on are fundamental data types and are not objects. 
