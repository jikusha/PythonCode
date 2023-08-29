def matching_chars(str1, str2):
    s1 = set(str1)
    s2 = set(str2)

    s3 = s1.intersection(s2)
    print(len(s3))




matching_chars("abcdef", "defghia")
matching_chars("aabcddekll12@", "bb22ll@55k")
