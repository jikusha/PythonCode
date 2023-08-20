from collections import OrderedDict

def remove_dups(s: str):
    s1 = set(s)
    new = ''.join(s1)
    print(new)

    d1 = OrderedDict.fromkeys(s)
    new = ''.join(d1.keys())
    print(new)

remove_dups("geeksforgeeks")
