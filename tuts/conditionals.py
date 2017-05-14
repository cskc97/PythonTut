a,b=5,1;
if a<b:
    print('a {} is less than b {}'.format(a,b));
else:
    print('b {} is less than a {}'.format(b,a));

print("foo" if a<b else "bar");

# Testing fibonacci now...

a=0
b=1
n=50
print(a)
print(b)
counter=1
while(counter<n):
    d=a+b
    a=b
    b=d
    print(d)
    counter=counter+1
print("DONE!")





