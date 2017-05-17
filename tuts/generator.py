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



def primes(n=1):
    while(True):
        if isPrime(n): yield n #yield is like return but it appends the result
        n+=1


# for val in primes():
#     if val>100: break
#     print(val)

class inclusive_range:
    def __init__(self,*args):
        numargs = len(args)
        if(numargs<1):
            raise TypeError("Requires at least one argument")
        elif numargs==1:
            self.stop=args[0]
            self.start=0
            self.step=1

        elif numargs==2:
            self.stop=args[1]
            self.start=args[0]
            self.step=1


        elif numargs==3:
            (self.start,self.stop,self.step)=args

        else:
            raise TypeError("No More than 3 arguments")


    def __iter__(self): # will make the inclusive_range object iterable
        i = self.start
        while i<=self.stop:
            yield i #it returns i and then with the next call of the function it picks up from i+=self.step
            i+=self.step


def main():
    o=inclusive_range(5,25,5)
    for i in o:
        print(i)

main()




