from collections import Counter


def words(string):
    word_list = string.split()
    word_dict = dict(Counter(word_list))
    return word_dict

dady = "i love love being t t"
mom = dady.split()
print(mom)

my_dict = words("eye eye list list you you")
print(my_dict)


