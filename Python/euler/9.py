

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2

# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import math

for a in range(10, 500):
	for b in range(10, 500):
		c = math.sqrt(a*a + b*b)
		if (a + b + c) == 1000:
			print a, b, c
			print a*b*c