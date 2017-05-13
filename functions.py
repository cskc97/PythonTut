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

