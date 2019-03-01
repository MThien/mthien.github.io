int0 = input("")
int0 = int(int0)
count = int(0)
stringfinal = str("")
for l in range (0, int0, 1):
	string = input("")
	for thing in range (0, len(string), 1):
		if (len(string) != thing):
			if (string[thing] == string[thing + 1]):
				stringfinal =stringfinal + string[thing + 1]
				count = count + 1
			else:
				print(count + string[thing])