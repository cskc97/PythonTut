def main():
	dictionary = {"one":1, "santhosh":"isAwesome"};
	sortedDictionary = sorted(dictionary.keys());
	print(dictionary);

	for key in dictionary:
		print(key,dictionary[key]);

	print("Now for the sorted dictionary");

	for key in sortedDictionary:
		print(key,dictionary[key]);

	dictionaryUsingDict = dict(
		one=1,
		two=900,
		three="I am awesome"

		) #no need to type in quotes anymore. 

	print("Using Dict");
	print(dictionaryUsingDict);

main();