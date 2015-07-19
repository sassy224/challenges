"""
Vanya gets bored one day and decides to enumerate a large pile of rocks. He first counts the rocks and finds out that he has n rocks in the pile, then he goes to the store to buy labels for enumeration. Each of the labels is a digit from 0 to 9 and each of the n rocks should be assigned a unique number from 1 to n.

 
If each label costs $1, how much money will Vanya spend on this project?

Input 1 (n) ? integer :
integer n (1<=n<=10^9) the number of rocks in the pile.

Output integer :
the cost of the enumeration
"""

def rocks(n):
	"""
	>>> rocks(13)
	17
	>>> rocks(36123011)
	277872985
	
	The trick here is to compute correctly the number of the digits from given n
	E.g,
	13 --> there're (13-9)*2 + 9 = 17 digits
	100 --> there're (100-99)*3 + (99-9)*2 + 9
	So you know the rule
	"""
	s = 0
	l = len(str(n))
	while l > 1:
		# the trick here is magic of python: '9'*3 = '999'
		s += (n - int('9'*(l-1))) * l
		n = int('9'*(l-1))
		l -= 1
	return s + 9 # don't forget to plus 9 at the end
	
	
if __name__ == "__main__":
	import doctest
	doctest.testmod()