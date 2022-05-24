from ast import Lambda


# Lambda function - Anonymous function
l1 = (1,2,3,4,5)
squares = list(map(lambda x: x*x, l1))
# print(squares)

# Another sample
def get_longest_word(sentence=''):
    words = tuple(sentence.split(' '))
    print(words)
    # output: ('Python', 'is', 'very', 'awesome')

    max_len = len(max(words, key=len))
    print(max_len)
    return list(filter(lambda x: len(x) == max_len, words))

print(get_longest_word("Python is very awesome"))