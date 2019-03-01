int1 = input("")
int1 = int(int1)

int2 = input("")
int2 = int(int2)

int3 = input("")
int3 = int(int3)

int4 = input("")
int4 = int(int4)

int5 = input("")
int5 = int(int5)

int6 = input("")
int6 = int(int6)

intfinal1 = (int1 * 3 + int2 * 2 + int3)

intfinal2 = (int4 * 3 + int5 * 2 + int6)

if intfinal1 < intfinal2:
		print("B")

if intfinal2 < intfinal1:
		print("A")

if intfinal1 == intfinal2:
		print("T")