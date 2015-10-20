import math

test = range(2,101)

for j in test:
	divisors_prime = []
	f = 2
	i = j
	while i != 1 and f**2 <= i:
		while i%f == 0:
			divisors_prime.append(f)
			i = i/f
		f = f+1
	if i != 1:
		divisors_prime.append(i)

		#exits loop once i is not divisable by f
	#if no f goes evenly into i, print "I am prime!"
	print j
	print divisors_prime