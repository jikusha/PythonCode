def word_frequency(s: str):
    words = s.split(' ')
    d = {key: words.count(key) for key in words}
    print(d)

word_frequency("geeks for geeks")

from collections import Counter

def word_frequency_1(s: str):
    words = s.split(' ')
    res = Counter(words)
    print(dict(res))

word_frequency_1("geeks for geeks")