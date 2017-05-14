class Duck:
	def __init__(self,duckName):
		self.name = duckName
	def quack(self):
		print("Quack!")
	def walk(self):
		print("Duck Walking!")

def main():
	donald = Duck("Donald The Duck")
	print("Created {}".format(donald.name))
	donald.quack()
	donald.walk()

#NOTE: There are NO access modifiers in Python. So there's no 
# explicit way of creating private members or anything like that. 

main();