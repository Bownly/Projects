


# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.


fibonacci = [1, 2]
while (fibonacci[-2] < 4000000):
	fibonacci.append(fibonacci[-1] + fibonacci[-2])

print(fibonacci[-1])

sum = 0
for i in fibonacci:
	if i % 2 == 0:
		print i
		sum += i

print sum