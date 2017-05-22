def readAndWriteBinary(inFileName):
    file = open(inFileName,"rb");
    outfile = open("outfile.png","wb")

    buffersize = 1000;
    buffer = file.read(buffersize)
    while len(buffer)>0:
        outfile.write(buffer)
        buffer = file.read(buffersize)


def main():
    readAndWriteBinary("wellnesslogo.png")

if __name__=="__main__":
    main()




