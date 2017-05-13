# Python doesn't have switch - case but it can be mimicked:

def main():
	choices = dict(
		one='first',
		two="second",
		three="third")
	v = "three";
	print(choices[v]);

	print(choices[v],"this is a default when value for a key is unavailable");
	print("Switch Statements are mimicked by dictionaries.");

	print("Conditional Expression Now -- --- ");

	a,b=1,0;
	c = a if a<b else b; #conditional opreator.
	print(c); 

main();