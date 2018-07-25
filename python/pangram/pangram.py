from string import ascii_lowercase

ALPHABET = set(ascii_lowercase)


def is_pangram(sentence):
    """sentence = sentence.lower().replace(' ', '')
    my_dict = {}
    for c in sentence:
        if not c.isalpha():
            continue
        my_dict[c] = my_dict.get(c, 0) + 1
        # print(my_dict)
    return len(my_dict.keys()) == 26
    """
    return ALPHABET.issubset(sentence.lower())
