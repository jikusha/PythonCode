def all_vowels(str1):
    vowels = ['a', 'e', 'i', 'o', 'u']
    se = set()
    for s in str1:
        if s.lower() in vowels:
            se.add(s.lower())

    l = list(se)
    l.sort()

    print(l)
    print(se)

    if l == vowels:
        print("Accepted")
    else:
        print("Not Accepted")

all_vowels("geeksforgeeks")
all_vowels("ABeeIghiObhkUul")