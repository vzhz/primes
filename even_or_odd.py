import pprint 
import math
numbers = range(2,51) 

def count_divisors(numbers): 
	numbers_divisors = []
	for i in numbers:
		divisors = 0
		for less in range(1, int(math.ceil(math.sqrt(i)))): #more eff. to count both sides of the pair, so use sqrt
			if i % less == 0:
				divisors += 2 #only even bc counting pairs, so never handle perfect squares
		numbers_divisors.append(divisors) 
	numbers_divisors = dict(zip(numbers, numbers_divisors))
	return numbers_divisors
#can test with range that contains single element

def even_or_odd(numbers_divisors):
	even_divisors = {}
	odd_divisors = {}
	for k in numbers_divisors:
		if numbers_divisors[k]%2 == 0:
			even_divisors[k] = numbers_divisors[k] #shouldn't be on outside and inside unless pass in
		else:
			odd_divisors[k] = numbers_divisors[k]

####check that even+odd=total <-- would that be a good test?
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
 		maybe_small_factor = list(range(2, int(math.ceil(math.sqrt(i))))) #don't have to go any further than the sqrt of i -> what if sqrt isn't an int? 
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
				current_number = current_number/f #changing i, careful not to both interate and change
		numbers_divisors_prime[i] = divisors_prime
	print ("Numbers and their divisors: ")
	print (pprint.pprint(numbers_divisors_prime))
#if prime, print "I am prime"

find_prime_factors(numbers)
