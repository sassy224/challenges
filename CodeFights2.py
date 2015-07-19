"""
You are given a digital number written down on a sheet of paper. 
Your task is to figure out if you rotate the given sheet of paper by 180 degrees would the number still look exactly the same.

input: "1"  
output: false

input: "29562"  
output: true

input: "77"  
output: false
"""

def digital_number(number):
	"""
	>>> digital_number('1')
	False
	>>> digital_number('29562')
	True
	>>> digital_number('77')
	False
	>>> digital_number('000')
	True
	
	The trick here is you need to understand what rotation is:
	https://en.wikipedia.org/wiki/Seven-segment_display_character_representations
	In short:
	0 -> 0
	2 -> 2
	5 -> 5
	6 -> 9
	8 -> 8
	9 -> 6
	Other numbers can't be rotated into another number
	"""
	rule = {'0':'0', '2':'2', '5':'5', '6':'9', '8':'8', '9':'6'}
	new_str = [rule.get(digit, "x") for digit in number ]
	return number == "".join(new_str[::-1])
	
if __name__ == "__main__":
	import doctest
	doctest.testmod()