def remove_ith(s, i):
    new_str = ''
    for j in range(0, len(s)):
        if j!=i-1:
            new_str += s[j]

    print(new_str)

remove_ith("Kamal Pandey", 8)


def remove_letter(s, l):
    new_str = s.replace(l,'')
    print(new_str)
    new_str = s.replace(l,'',1)
    print(new_str)

remove_letter("malayalam",'m')


def remove_ith_1(s, i):
    new_str = ''.join([s[j] for j in range(0,len(s)) if j!=i-1])
    print(new_str)

remove_ith_1("Kamal Pandey", 8)
