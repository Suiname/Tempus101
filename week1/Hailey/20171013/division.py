# Division for Elementary School

# Create a python (.py) file named division.py inside your folder. Inside this file solve the following problem: In elementary school, when you divide you typically use division and have to report the remainder. Create a function named "elementary_division" that returns a string. It will accept two arguments: a number, and a number to divide that number against. The returned string should state what the result is and the remainder, in a format like this "The result is 2 and the remainder is 4". You will likely need to use the / and the % operators.

def elementary_division(numerator, denominator):
	remainder = str(numerator % denominator)
	rounded_result = str(numerator/denominator)
	return "The result is " + rounded_result + " and the remainder is " + remainder
	

print(elementary_division(14,5))