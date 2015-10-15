# classify numbers by if even or odd # of divisors, what is pattern, divisior function\
# write fcn to compute number divisors from like 1-50 and look for patterns

#dont use same var inside/out fcn
#avoid name shadowing (var in and out have same name - can't see outside)

import pprint #via http://stackoverflow.com/questions/20181899/how-to-make-each-key-value-of-a-dictionary-print-on-a-new-line
import math
numbers = range(2,51) #range returns list in Python2, in Python3 uses generator (like xrange in Python2), allows you to not have to wait
#started at 2 bc sqrt 1 is 1 (fuck this shit)

def count_divisors(numbers): #ignorant little man lives here
	numbers_divisors = []
	for i in numbers:
		divisors = 0
		for less in range(1, int(math.ceil(math.sqrt(i)))): #more eff. to count both sides of the pair, so use sqrt
			if i % less == 0:
				divisors += 2
		numbers_divisors.append(divisors) #trying to use var on 19 if don't pass in num_div on line 10 or whatever
	numbers_divisors = dict(zip(numbers, numbers_divisors))
	return numbers_divisors
#can test with range that contains single element

#eric's suggestion
#def divisor_function(n):
#   count = 0
#   for i in range(1, n + 1):
#       if n % i == 0:
#           count += 1
#   return count
#but I like mine better, frankly
#fine bc more modular, can call each time you want it to 
#good because easier to test, can test with signle number

def even_or_odd(numbers_divisors):
	even_divisors = {}
	odd_divisors = {}
	for k in numbers_divisors:
		if numbers_divisors[k]%2 == 0:
			even_divisors[k] = numbers_divisors[k] #shouldn't be on outside and inside unless pass in
		else:
			odd_divisors[k] = numbers_divisors[k]

####check that even+odd=total
	print (("Number of even divisors up to %s is " + str(len(even_divisors))) %len(numbers))
	print (("Number of odd divisors up to %s is " + str(len(odd_divisors))) %len(numbers))
	print ("Numbers and their (even) number of divisors: ")
	print (pprint.pprint(even_divisors)) 
	print ("Numbers and their (odd) number of divisors: ")
	print (pprint.pprint(odd_divisors)) #why printing "none" and why not taking row per entry
#stores in var x so python knows output count_div goes into as input of even or odd

#even_or_odd(count_divisors(numbers))

#the numbers with the odd number of divisors are all perfect squares. wondering if there is a way I could have \
#determined this is I didn't know what a perfect square was or if (as I did) I looked at the list and didn't reconize \
#that they were perfect squares. Intersted because of general "how do I get more information out of this data?" desiresnumbers_divisors_prime = {}

def find_prime_factors(numbers):
	numbers_divisors_prime = {}
 	for i in numbers: #interating i
 		divisors_prime = []
 		maybe_small_factor = list(range(2, int(math.ceil(math.sqrt(i)+1)))) #don't have to go any further than the sqrt of i -> what if sqrt isn't an int? 
 		current_number = i
# 		divisors_prime.append(1) #need prime 
 		for f in maybe_small_factor:
			#print divisors_prime
			#small_primes = [2, 3, 5, 7, 9]
			#for primes in small_primes:
			#	if current_number%primes == 0:
			#		divisors_prime.append("I am prime") 
			while current_number%f == 0:
		 		divisors_prime.append(f) 
				current_number = current_number/f #changing i, shouldn't interate and change
#		divisors_prime.append(i)
		numbers_divisors_prime[i] = divisors_prime
		#print numbers_divisors_prime
	print ("Numbers and their divisors: ")
	print (pprint.pprint(numbers_divisors_prime))
#if prime, print "I am prime"

find_prime_factors(numbers)
#				if large_factor%f == 0: #check if large_factor can be factered by the same maybe_small_factor a second time (eg. 2, 2, 3, 5 for 60)
#	 				divisors_prime.append(large_factor) #how do I make this recursive?
#	return divisors_prime
	 			
# def count_prime_factors(numbers):
#  	numbers_divisors_prime = {}
#  	divisors_prime = find_prime_factors(numbers)
# 	numbers_divisors_prime[i] = divisors_prime #dict[key] = value
#	print ("Numbers and their divisors: ")
#	print (pprint.pprint(numbers_divisors_prime))

#count_prime_factors(numbers)
			