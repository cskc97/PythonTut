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

    # s.strip() will remove spaces before and after string and also newline character
    # s.rstrip(arg) will remove the arg from the string. 

main()
