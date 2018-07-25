def is_isogram(string):
    my_dict = {}
    for c in string:
        my_dict[c.lower()] = my_dict.get(c.lower(), 0) + 1
    not_isogram = {k: v for (k, v) in my_dict.items()
                   if v > 1 and k.isalpha()}
    return not_isogram == {}
