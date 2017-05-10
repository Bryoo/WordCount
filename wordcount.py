from collections import Counter


def words(string):
    word_list1 = string.split()
    word_list = []
    for elem in word_list1:
        try:
            word_list.append(int(elem))
        except Exception:
            word_list.append(elem)

    word_dict = dict(Counter(word_list))
    return word_dict


dady = "i love love being t t"
mom = dady.split()
print(mom)

my_dict = words("4 eye 21 list you you")
print(my_dict)




