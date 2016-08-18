

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.


numdict = {
0:"",
1:"one", 
2:"two",
3:"three",
4:"four",
5:"five",
6:"six",
7:"seven",
8:"eight",
9:"nine",
10:"ten",
11:"eleven",
12:"twelve",
13:"thirteen",
14:"fourteen",
15:"fifteen",
16:"sixteen",
17:"seventeen",
18:"eighteen",
19:"nineteen",
20:"twenty",
30:"thirty",
40:"forty",
50:"fifty",
60:"sixty",
70:"seventy",
80:"eighty",
90:"ninety",
}
 # zero one two three four five six seven eight nine ten
 # eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen
 # twenty thirty forty fifty sixty seventy eighty ninety|;

totallen = 0

for i in range(1,1001):
	name = ""
	if i in numdict:
		name = numdict[i]
	else:
		numstr = str(i)
		if i == 1000:
			name = numdict[1] + "thousand"
		if len(numstr) == 3:
			name += numdict[int(numstr[0])] + "hundred"
			if numstr[1:] != "00":
				name += "and"
			if int(numstr[1:]) in numdict:
				name += numdict[int(numstr[1:])]
			else:
				name += numdict[int(numstr[1])*10]
				if i%10 != 0:
					name += numdict[i%10]
		elif len(numstr) == 2:
			name += numdict[int(numstr[0])*10]
			if i%10 != 0:
				name += numdict[i%10]

	print name
	totallen += len(name)

print totallen








