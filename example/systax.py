import math
# from math import pi

def greeting(name=''):
    """Output a greeting message"""
    print(f'Hello, {name}')
    print('{}, {}, {}'.format('Hello', name, 'again'))
    print('Have a nice journey with Python.')
    print('-----End----------')

def get_pi_number():
    return math.pi

# Input
name_input = input('Please input your name: ')

# Call function 
greeting(name_input)

print('Pi number value =', get_pi_number())