

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


def palindrome(num):
	string = str(num)
	for i in range(0, len(string)):
		if (string[i] != string[-(i+1)]):
			return False
	return True

palindromes = []

for i in range(100, 1000):
	for j in range(100, 1000):
		if palindrome(i*j) == True:
			palindromes.append(i*j)

winner = 0
for i in range(0, len(palindromes)):
	if palindromes[i] > winner:
		winner = palindromes[i]

print winner


