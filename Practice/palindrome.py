def palindrome(s):
    rev_str_1 = ''
    for i in range(len(s)-1,-1,-1):
        rev_str_1 = rev_str_1+s[i]

    if s==rev_str_1:
        print("Palindrome")
    else:
        print("Not a palindrome")

def palindrome_1(s):
    n = len(s)
    flag = 0
    if n%2 == 0:
        mid = n//2
    else:
        mid = n//2 + 1

    i = 0
    j = n-1

    while i < mid < j:
        if s[i] == s[j]:
            i+=1
            j-=1
        else:
            flag = 1
            break

    if flag == 0:
            print("Palindrome")
    else:
            print("Not a palindrome")



palindrome("malayalam")
palindrome_1("blabla")
