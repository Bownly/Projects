

# The following iterative sequence is defined for the set of positive integers:

# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

numdict = dict()

def collatz(n):
	if n % 2 == 0:
		n = n / 2
	else:
		n = n * 3 + 1

	if n in numdict:
		return 1 + numdict[n]
	elif n == 1:
		return 1
	else:
		return collatz(n) + 1


for i in range(1, 1000000):
	numdict[i] = collatz(i)

# numdict[13] = collatz(13)

# print max(numdict)
print max(numdict.iterkeys(), key=(lambda key: numdict[key]))
print numdict[max(numdict.iterkeys(), key=(lambda key: numdict[key]))]
# print numdict
