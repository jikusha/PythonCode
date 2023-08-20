def palindrome(s):
    rev_str = s[::-1]
    rev_str_1 = ''
    for i in range(len(s)-1,-1,-1):
        rev_str_1 = rev_str_1+s[i]

    if s==rev_str_1:
        print("Palindrome")
    else:
        print("Not a palindrome")

palindrome("malayalam")
