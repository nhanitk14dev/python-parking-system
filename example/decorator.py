"""
Decorator usage: Take in a function, adds some functionally and return it
	- Can be used for validating input data
	- Can be used for filtering, mapping output data
	- Can be used to act like a middleware / interceptor
"""
def make_pretty(input_func):
	def decorate():
		print("I got additional decoration.")
		input_func()

	return decorate

def ordinary():
	print("I am ordinary.")

@make_pretty
def another_ordinary():
	print("I am an another ordinary")

# ordinary()
# pretty = make_pretty(ordinary)
# print(pretty())

another_ordinary()