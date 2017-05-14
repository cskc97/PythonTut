try:
    print("trying")
except:
    print("Exception")


try:
	fh=open('nofilelikethis.txt')
except IOError as e:
	print(e, "This is an exception");
else:
	#this will run if fh successfully opens nofilelikethis.txt
	print("Opened successfully");




