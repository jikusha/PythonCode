from collections import Counter

def duplicate_chars(str1):
    chars = Counter(str1)
    l = []
    for k, v in chars.items():
        if v>1:
            l.append(k)

    print(l)

duplicate_chars("hello")