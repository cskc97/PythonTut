#trying out functions in python

def fooNoArgs():
    print("Random Foo No Args")

def isPrime(n):
    if n==1:
        print("1 is special")
    elif n==2:
        print("2 is prime")
    else:
        for x in range(2,n):
            if n % x ==0:
                print("not prime - {}".format(n))
                return False
            else:
                print("Prime - {}".format(n))
                return True


for n in range(1,20):
    isPrime(n)


def passFunc():
    pass
# the above function does nothing. pass is a keyword that 
# lets you create an empty function. 
#None will let you create an optional argument
def testFunc(*args):
    # *args is a way of saying there is an optional list of arguments
    print(args)
    #args now becomes a tuple and is thus immutable. 

testFunc(12,3,4)

def kwargsfunc(**kwargs):
    print(kwargs["one"])
kwargsfunc(one=1);

#kwargs func is defining named arguments from the call which are then 
# retrieved from the functions. kwargs is actuaally a dictionary. 

#*args will preserve order as it is a list and **kwargs probably
# wont because it is a dictionary (also called a map)