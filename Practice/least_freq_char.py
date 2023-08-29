from collections import Counter
def least_freq_char(str1):
    d = Counter(str1)
    print(min(d, key=d.get))

def most_freq_char(str1):
    d = Counter(str1)
    print(max(d, key=d.get))


least_freq_char("GeeksforGeeks")
most_freq_char("GeeksforGeeks")