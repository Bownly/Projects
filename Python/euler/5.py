

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import math

def isDivisble(num, myrange):
	for i in range(1, myrange+1):
		if num/i != math.floor(num/i):
			return False
	return True

num = 1.0
count = 1
while count < 20:
	if isDivisble(num, count) == True:
		print(num)
		count += 1
	num += count-1

# print(isDivisble(2520, 10))




# product = 11*12*13*14*15*16*17*18*19*20
# # print(product, isDivisble(product, 20))

# for i in range(1, 21):
# 	if isDivisble(product/(20-i), 20):
# 		print product/(20-i)
# 	print False
