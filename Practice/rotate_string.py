def rotate_string(str1, n):
    print("Left Rotation: ", str1[n:]+str1[0:n])
    print("Right Rotation: ", str1[len(str1) - n: ] + str1[0: len(str1) - n])

rotate_string("GeeksforGeeks", 2)

rotate_string("qwertyu", 2)
