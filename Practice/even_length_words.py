def even_length_words(s):
    words = s.split(' ')
    event_length_words = list(filter(lambda w: len(w)%2 == 0, words))
    for w in event_length_words:
        print(w, end = ' ')
    print()

even_length_words("This is a python language")
even_length_words("i am laxmi")