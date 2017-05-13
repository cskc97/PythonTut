def main():
    s="This is a {} string".format(40);
    rawString = r"This is a \nraw string";
    stringVal = "This is a \n raw string";
    python2String = "%s val" % 42;
    multiLine = '''\
    Line after line
    Blah Blah Blah
    Stuff...

    '''

    print(s);
    print(rawString);
    print(stringVal);
    print(python2String);
    print(multiLine);

main()
