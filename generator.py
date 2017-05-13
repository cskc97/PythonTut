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


for val in primes():
    if val>100: break
    print(val)

