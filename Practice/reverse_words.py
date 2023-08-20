def rev_words(s):
    words = s.split(' ')
    rw = ''
    for i in range(len(words)-1, -1, -1):
        rw = rw + words[i] + ' '

    print(rw.strip())



rev_words("my name is jiku")
rev_words("my")
rev_words("my name")