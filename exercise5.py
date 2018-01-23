import re
from collections import Counter


# 5
def read_text():
    words = re.findall(r'\w+', open('anything.txt').read().lower())
    print('These are the individual words lowercase:', words)
    return words


# 5.1
def occurence_dict(words_list):
    dict = Counter(words_list).most_common()
    print('This is the dictionary & no of occ:', dict)
    return dict


# 5.2
def most_occurence(words_list):
    mo = Counter(words_list).most_common(1)
    print('The word with most occ:', mo)
    return mo


words = read_text()
occurence_dict(words)
most_occurence(words)

