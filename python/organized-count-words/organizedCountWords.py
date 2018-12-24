def count_words(word_list):
    my_dict = {}
    for word in word_list:
        if word not in my_dict:
            my_dict[word] = 0
        my_dict[word] += 1
    return my_dict


def organized_count_words(word_list):
    my_dict = {}
    for word in word_list:
        # if key does not exist, add key and value
        if len(word) not in my_dict:
            my_dict[len(word)] = {word: 1}
        # if key exist, add to value(if child key does not exist)
        elif word not in my_dict[len(word)]:
            my_dict[len(word)][word] = 1
        # if key exist, add to value(if child key exist)
        else:
            my_dict[len(word)][word] += 1
    return my_dict


word_list_test = ["the", "seething", "sea", "ceaseth",
         "and", "thus", "the", "seething", "sea", "sufficeth", "us"]
print(organized_count_words(word_list_test))
