a = "global"

def outer():
    a = "local"

    def inner():
        nonlocal a
        a = "non-local"
        print("Inner - value of a:", a)

    inner()
    print("Outer - value of a:", a)


outer()
print("global:", a)