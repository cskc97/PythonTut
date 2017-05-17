def main():
	x=(1,2,3) #this is a tuple and is immutable. It can't be changed
	listVal = [1,2,3] # this is a list and can be appended

	print(x)
	print(listVal)
	print("Appending to list")
	listVal.append(10);
	print(listVal);

	str = "string";
	print(str[2]); #prints 
	print(str[1:4]); #prints tri. This is called slicing. It prints indices 1 to 4-1 = 3

	tupleVal = range(0,100);
	for val in tupleVal:
		print(val+1,"Prints things 100 times");
	print(tupleVal);

	#tuples are created with ()
	#lists are created with []

	#tuples are IMMUTABLE and so they can't be changed
	#lists are MUTABLE and so they can be changed
	
main()
