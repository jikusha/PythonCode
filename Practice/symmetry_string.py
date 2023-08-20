def symmetry(s):
    n = len(s)
    if n%2 == 0:
        s1 = s[0:n//2]
        s2 = s[n//2:n]
        if s1 == s2:
            print("Symmetry")
    else:
        print("Not symmetry")


def symmetry_1(s):
    n = len(s)
    flag = 0
    if n%2 == 0:
        mid = n//2
        i = 0
        j = mid

        while i < mid and j< n:
            if s[i] == s[j]:
                i+=1
                j+=1
            else:
                flag = 1
                break

        if flag == 0:
            print("Symmetry")
        else:
            print("Not symmetry")
    else:
        print("Not symmetry")

symmetry("khokho")
symmetry_1("pp")