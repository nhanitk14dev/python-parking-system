import sys

# a = tuple(range(10))

# print(id(a))
# print(a)
# print(sys.getsizeof(a))


if __name__ == '__main__':
    import timeit as ti

    print(ti.timeit("x = (i for i in range(100))"))