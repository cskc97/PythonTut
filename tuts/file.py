def main():

    buffersize = 1000;
    file = open("raven.txt","r");
    outfile = open('new.txt',"w")

    buffer = file.read(buffersize)

    while len(buffer)>0:
        print(buffer)
        buffer = file.read(buffersize) #basically 'incrementing' the buffer.
    #
    # for line in file.readlines():
    #     print(line,file=outfile)
    #
    # for line in file.readlines():
    #     print(line)


    #Now using buffers





main()
