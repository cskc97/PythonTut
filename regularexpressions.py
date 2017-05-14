# regular expressions are for matching patterns in text
# they are also called regexes. 

import re

def main():
	fh = open("raven.txt");
	for line in fh:
		if re.search('(Len|Neverm)ore',line):
			print(line);
			print("Now Replacing");
			print(re.sub('(Len|Neverm)ore','###',line))


	print("After Replacement")
	fh.seek(0); #resets the file pointer

	for line in fh:
		print(line);
	else:
		print("End Reached");

	fh.seek(0);
	pattern = re.compile('(Len|Neverm)ore',re.IGNORECASE);
	for line in fh:
		if re.search(pattern,line):
			print(line);
			print(pattern.sub('###',line))





main();
