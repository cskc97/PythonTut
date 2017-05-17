class Animal:
	def __init__(self):
		print("Animal Created")

	def animal(self):
		print("I am an animal")



class Duck(Animal): #Duck inherits from Animal
	def __init__(self,duckName):
		self.name = duckName
		super(Duck, self).__init__() #constructor needs to be explicitly
									# if required.

	def quack(self):
		print("Quack!")
		self.animal()
	def walk(self):
		print("Duck Walking!")



def main():
	donald = Duck("Donald The Duck")
	print("Created {}".format(donald.name))
	donald.quack()
	donald.walk()

#NOTE: There are NO access modifiers in Python. So there's no 
# explicit way of creating private members or anything like that.
#Also, python child classes don't call the constructor or the destructor
# of the parent classes automatically. 

main();
