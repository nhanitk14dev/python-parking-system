
from operator import le


def get_longest_string(sentence=''):
    """
    Return a list of word that have the longest length in  the sentence.
    """
    words = sentence.split(' ')
    if len(words) == 1:
        return words
    else:
        max_length = 0
        result = []
        for word in words:
            if len(word) > max_length:
                result.clear()
                max_length = len(word)
                result.append(word)
            elif len(word) == max_length:
                result.append(word)

    return result

result = get_longest_string("I'm study Python Program")
print(result)
# Input: I'm study Python Program

# Ouput: ['study', 'Python', 'Program']