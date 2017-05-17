def main():
    s="This is a {} string".format(40);
    rawString = r"This is a \nraw string";
    stringVal = "This is not a \n raw string";
    python2String = "%s val" % 42;

    multiLine = '''\
    Line after line
    Blah Blah Blah
    Stuff...

    '''

    #strings in themselves are immutable
    #All operations on strings return new objects.

    print(s);
    print(rawString);
    print(stringVal);
    print(python2String);
    print(multiLine);

    print(("Common String Methods".capitalize()))

    print(s.capitalize())
    print(s.upper())
    print(s.lower())
    print(s.swapcase())
    print(s.find('is'))
    print("\n")

    # s.strip() will remove spaces before and after string and also newline character
    # s.rstrip(arg) will remove the arg from the string.
    print("Trying out the format method\n")

    #format() method
    a,b = 5,42
    print(a,b)

    print("This is {nemo} and that is {dory}".format(nemo="Nemo",dory="Dory"))
    print("{{This is inside curly braces}}".format())

    stringSplit = "Santhoshkrishnachaitanya Chelikavada is my full name"
    print(stringSplit.split())
    print(stringSplit.split('a'))
    splitList = stringSplit.split()
    print(splitList)
    joinList = ','.join(splitList)
    print(joinList)

main()
