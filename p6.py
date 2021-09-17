# wapp to find sum of first "n" +ve integers

num = int(input(" enter +ve integer "))
if num < 0:
	print("invalid number")
else:
	sum = 0
	i = 1
	while i <= num:
		sum = sum + i
		i = i + 1
	print(" sum = ", sum)	
	