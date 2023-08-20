def matching_chars(str1, str2):
    s = set()
    for c in str1:
        if c in str2:
            s.add(c)

    print(len(s))
    print(s)

matching_chars("jikusandilya","kamalpandey")

from collections import Counter

def matching_chars_1(str1, str2):
    s1 = set(Counter(str1))
    s2 = set(Counter(str2))

    print(s1.intersection(s2))
    print(len(s1.intersection(s2)))


matching_chars_1("jikusandilya","kamalpandey")