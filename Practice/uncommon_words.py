def uncommon_words(str1, str2):
    words1 = set(str1.split(' '))
    words2 = set(str2.split(' '))
    uncommons = list(words1.difference(words2).union(words2.difference(words1)))
    print(uncommons)

uncommon_words("Geeks for Geeks", "Learning from Geeks for Geeks")
uncommon_words("apple banana mango", "banana fruits mango")
