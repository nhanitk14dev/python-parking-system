a = "global-"

def func_1():
    """Sameple function 1"""
    global a

    a *= 2 
    # The result is: global-global-
    print("func_1 - value of a:", a)

# func_1()
#
def sum_two(x=1, y=0):
    return x + y

def get_sum(n=0):
    s = 0
    for i in range(n):
        s += i
    return s

sum = sum_two(11, 1)
print(get_sum(10))

