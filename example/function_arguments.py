# https://www.programiz.com/python-programming/function-argument
# Python Function Arguments
# https://www.geeksforgeeks.org/default-arguments-in-python/
#Python Default Arguments
def greet(name, msg="Good morning!"):
    """
    This function greets to
    the person with the
    provided message.

    If the message is not provided,
    it defaults to "Good
    morning!"
    """

    print("Hello", name + ', ' + msg)


# greet("Kate")
# greet("Bruce", "How do you do?")