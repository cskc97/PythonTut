class Duck(): #Duck inherits from Animal
        def __init__(self,duckName,**kwargs):
            self.name = duckName
            super().__init__() #constructor needs to be explicitly
                                        # if required.
            self.kwargDict = kwargs

        def printKwargs(self):
            for key in self.kwargDict:
                print(key,self.kwargDict.get(key))

        def quack(self):
            print("Quack!")
            self.animal()

        def walk(self):
            print("Duck Walking!")

        @property
        def color(self):
            return self.kwargDict.get("color")

        @color.setter
        def color(self,c):
            self.kwargDict['color'] = c
            print("Called Setter")

        @color.deleter
        def color(self):
            del self.kwargDict["color"]

def main():
    donald =  Duck("Donald Duck")
    donald.color="blue"
    print(donald.color)


main()


