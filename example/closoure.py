# Python Closure
"""
	A nested function (inner function) defined inside a function
	  - Has access to a free variable in outer scope
	  - Returned from the enclosing function
"""

def make_power(expression):
	def pow_of(base):
		return pow(base, expression)

	return pow_of

square = make_power(2)
print(square(5))